# Segurança do protótipo Python

O código original de Attack on Ancestors utilizava `game_data/Usuarios.csv` para armazenar informações de cadastro, incluindo senhas em texto simples.

O fluxo atual de cadastro/verificação local utiliza `auth_store.py`, com derivação PBKDF2-HMAC-SHA256 e sal aleatório por usuário. Os dados são armazenados no diretório `.local/`, excluído do Git, e não são sincronizados com a demonstração web.

**Importante:**
- O arquivo `game_data/Usuarios.csv` foi removido da versão atual rastreada pelo Git, mas pode permanecer em commits históricos do repositório público. Apenas removê-lo na branch principal **não apaga o histórico**.
- Qualquer senha real que tenha sido utilizada nesse arquivo deve ser considerada comprometida e substituída nos serviços em que foi reutilizada.
- Senhas antigas não são migradas automaticamente para o cadastro novo.
- O login experimental faz apenas verificação local de credenciais: não estabelece sessão autenticada, não fornece controle de acesso a rotas e não foi projetado como serviço público.
- Para autenticação real, use uma solução de identidade aprovada, proteção contra tentativas excessivas, sessões seguras e revisão especializada.

A demonstração em `demo/` não acessa contas nem arquivos pessoais; ela usa dados e mecânicas fictícios.
