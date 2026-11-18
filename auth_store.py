"""Local credential storage for Attack on Ancestors prototype.

For local experimentation, not a production identity service.
Never migrates the legacy Users CSV or its cleartext passwords.
"""
from __future__ import annotations

import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import secrets
import tempfile
import threading

ITERATIONS = 300_000
_LOCK = threading.RLock()


def user_db_path() -> Path:
    override = os.getenv("AOA_USERS_PATH")
    return Path(override).expanduser().resolve() if override else Path(__file__).resolve().parent / ".local" / "users.json"


def _load(path: Path) -> list[dict]:
    if not path.exists():
        return []
    records = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(records, list):
        raise ValueError("Formato inválido do cadastro local.")
    return records


def _save(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp_name = None
    try:
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=path.parent, prefix=".users-", suffix=".tmp", delete=False) as temp:
            temp_name = temp.name
            json.dump(records, temp, ensure_ascii=False, indent=2)
            temp.flush()
            os.fsync(temp.fileno())
        os.replace(temp_name, path)
        try:
            os.chmod(path, 0o600)
        except OSError:
            pass
    finally:
        if temp_name and os.path.exists(temp_name):
            os.unlink(temp_name)


def register(username: str | None, password: str | None, email: str | None) -> bool:
    username = (username or "").strip()
    email = (email or "").strip()
    password = password or ""
    if not re.fullmatch(r"[A-Za-z0-9_-]{3,40}", username):
        raise ValueError("Usuário deve ter 3 a 40 caracteres (letras, números, _ ou -).")
    if len(password) < 12 or len(password) > 256:
        raise ValueError("A senha deve ter de 12 a 256 caracteres.")
    if not 5 <= len(email) <= 254 or not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
        raise ValueError("Informe um e-mail válido.")
    with _LOCK:
        path = user_db_path()
        records = _load(path)
        if any(str(u.get("username", "")).casefold() == username.casefold() for u in records):
            return False
        salt = secrets.token_bytes(16)
        hash_bytes = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, ITERATIONS)
        records.append({
            "username": username,
            "email": email,
            "salt": salt.hex(),
            "password_hash": hash_bytes.hex(),
            "iterations": ITERATIONS,
        })
        _save(path, records)
    return True


def verify(username: str | None, password: str | None) -> bool:
    username = (username or "").strip()
    password = password or ""
    if not username or not password:
        return False
    with _LOCK:
        records = _load(user_db_path())
        found = next((u for u in records if str(u.get("username", "")).casefold() == username.casefold()), None)
    if found is None:
        return False
    try:
        salt = bytes.fromhex(found["salt"])
        expected = bytes.fromhex(found["password_hash"])
        iterations = int(found["iterations"])
        if not 1 <= iterations <= 1_000_000:
            return False
        actual = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, iterations)
        return hmac.compare_digest(expected, actual)
    except (KeyError, ValueError, TypeError):
        return False
