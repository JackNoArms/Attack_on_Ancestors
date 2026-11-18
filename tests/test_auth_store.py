import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import auth_store


class LocalCredentialStoreTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.path = Path(self.temp.name) / "users.json"
        self.env = patch.dict(os.environ, {"AOA_USERS_PATH": str(self.path)})
        self.env.start()

    def tearDown(self):
        self.env.stop()
        self.temp.cleanup()

    def test_registration_hashes_password_and_can_verify(self):
        assert auth_store.register("player_one", "long-safe-password-123", "player@example.test")
        self.assertFalse(auth_store.register("PLAYER_ONE", "another-long-pass123", "other@example.test"))
        self.assertTrue(auth_store.verify("player_one", "long-safe-password-123"))
        self.assertFalse(auth_store.verify("player_one", "incorrect-password"))
        text = self.path.read_text(encoding="utf-8")
        self.assertNotIn("long-safe-password-123", text)
        self.assertNotIn('"password":', text)
        record = json.loads(text)[0]
        self.assertEqual(record["iterations"], 300_000)
        self.assertEqual(len(record["salt"]), 32)
        self.assertEqual(len(record["password_hash"]), 64)

    def test_invalid_credentials_and_legacy_users_are_not_loaded(self):
        self.assertFalse(auth_store.verify("unknown", "anything"))
        self.assertFalse(self.path.exists())
        for name,password,email in [
            ("x", "long-safe-password-123", "x@example.test"),
            ("admin", "short", "x@example.test"),
            ("admin", "long-safe-password-123", "not-an-email"),
            ("../evil", "long-safe-password-123", "x@example.test"),
        ]:
            with self.assertRaises(ValueError):
                auth_store.register(name, password, email)
        self.assertFalse(self.path.exists())

    def test_password_salts_are_unique(self):
        auth_store.register("person_a", "long-safe-password-123", "a@example.test")
        auth_store.register("person_b", "long-safe-password-123", "b@example.test")
        records = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertNotEqual(records[0]["salt"], records[1]["salt"])
        self.assertNotEqual(records[0]["password_hash"], records[1]["password_hash"])


if __name__ == "__main__":
    unittest.main()
