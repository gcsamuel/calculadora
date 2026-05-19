# 🐍 PythonAnywhere - Guia Completo

## O que é PythonAnywhere?

**PythonAnywhere** é uma plataforma de hospedagem na nuvem **exclusiva para Python** e Django. É muito mais simples que Heroku para quem quer apenas hospedar uma aplicação Django.

### ✅ Vantagens
- ✨ Mais simples de configurar (sem Docker necessário)
- 💰 Free tier disponível (com limitações)
- 🎯 Feito especificamente para Python/Django
- 📊 Dashboard web intuitivo
- 🔧 Console Python integrado
- 🚀 Deploy super rápido
- 🔐 HTTPS automático

### ⚠️ Limitações do Free Tier
- Máximo 1 app
- 512 MB de storage
- CPU limitada
- Sem acesso a APIs externas (exceto whitelist)
- Sem processamento de background
- Sem MySQL/PostgreSQL nativo (só SQLite)

### 💰 Planos Pagos (começam em $5/mês)
- PostgreSQL/MySQL disponível
- Mais storage (10GB+)
- Mais poder de processamento
- Acesso a APIs externas ilimitado
- Email support

---

## 🚀 Passo a Passo: Deploy no PythonAnywhere

### PASSO 1: Criar Conta (2 minutos)

1. Acesse: https://www.pythonanywhere.com
2. Clique em **"Start running Python online"**
3. Escolha **Free account** (ou upgrade depois)
4. Preencha email, username, senha
5. Clique em **"Create a free account"**
6. Confirme email
7. Faça login

---

### PASSO 2: Preparar Código no GitHub (5 minutos)

Se não tiver no GitHub, adicione:

```bash
cd /home/devmobhis/calculadora

# Inicializar git (se não fez)
git init

# Adicionar tudo
git add .

# Commit
git commit -m "Calculadora Django - Pronto para PythonAnywhere"

# Adicionar origem (substitua seu-usuario)
git remote add origin https://github.com/seu-usuario/calculadora.git

# Push
git push -u origin main
```

**⚠️ Importante**: Certifique-se de que `.env` está em `.gitignore` (já está!)

---

### PASSO 3: Clonar Repositório no PythonAnywhere (2 minutos)

No **Dashboard do PythonAnywhere**:

1. Clique em **"Open Bash console"** (ou Web terminal)

2. Clone seu repositório:
```bash
git clone https://github.com/seu-usuario/calculadora.git
cd calculadora
```

3. Criar ambiente virtual (se não tiver):
```bash
mkvirtualenv --python=/usr/bin/python3.11 calculadora
# Isso cria e ativa o venv automaticamente
```

4. Ativar virtualenv (se não estiver ativado):
```bash
workon calculadora
```

5. Instalar dependências:
```bash
pip install -r requirements.txt
```

---

### PASSO 4: Ajustar settings.py para PythonAnywhere (3 minutos)

No PythonAnywhere bash:

```bash
# Editar settings.py
nano config/settings.py
```

Procure por `ALLOWED_HOSTS` e altere para:

```python
ALLOWED_HOSTS = ['seu-username.pythonanywhere.com', 'localhost', '127.0.0.1']
```

Se estiver configurando um domínio personalizado, adicione também:

```python
ALLOWED_HOSTS = ['seu-username.pythonanywhere.com', 'seu-dominio.com', 'localhost']
```

Salve: `Ctrl+X` → `Y` → `Enter`

---

### PASSO 5: Coletar Arquivos Estáticos (1 minuto)

```bash
workon calculadora
cd calculadora
python manage.py collectstatic --noinput
```

---

### PASSO 6: Fazer Migrações (1 minuto)

```bash
python manage.py migrate
```

---

### PASSO 7: Criar Superuser (1 minuto)

```bash
python manage.py createsuperuser

# Exemplo:
# Username: admin
# Email: seu-email@exemplo.com
# Password: (digite e confirme)
```

---

### PASSO 8: Configurar Web App no Dashboard (3 minutos)

1. No Dashboard, vá para **"Web"**
2. Clique em **"Add a new web app"**
3. Escolha seu domínio padrão: `seu-username.pythonanywhere.com`
4. Clique **"Next"**
5. Escolha **"Manual configuration"**
6. Escolha **Python 3.11**
7. Clique **"Next"**

---

### PASSO 9: Editar WSGI File (3 minutos)

1. No Dashboard → **Web** → clique em seu domínio
2. Na seção **"Code"**, encontre o arquivo WSGI
3. Clique no link do arquivo WSGI (ex: `/var/www/seu_username_pythonanywhere_com_wsgi.py`)
4. **APAGUE TUDO** e cole isto:

```python
import os
import sys

# Adicionar seu projeto ao path
path = '/home/seu-username/calculadora'
if path not in sys.path:
    sys.path.append(path)

# Configurar Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

⚠️ **Substitua `seu-username` pelo seu username do PythonAnywhere!**

5. Salve: `Ctrl+S`

---

### PASSO 10: Configurar Static Files (2 minutos)

No Dashboard → **Web** → seu domínio:

Na seção **"Static files:"**

Clique em **"Add a new static files mapping"**

Preencha:
- **URL**: `/static/`
- **Directory**: `/home/seu-username/calculadora/staticfiles/`

⚠️ **Substitua `seu-username`!**

---

### PASSO 11: Recarregar Web App (30 segundos)

1. No Dashboard → **Web**
2. Clique no botão **"Reload seu-username.pythonanywhere.com"** (verde, topo)
3. Aguarde ~10 segundos

---

### PASSO 12: Acessar Sua App! 🎉

1. Vá para: `https://seu-username.pythonanywhere.com`
2. Admin em: `https://seu-username.pythonanywhere.com/admin`

---

## 🔧 Configurações Adicionais

### Database (Upgrade Recomendado)

Se quiser PostgreSQL (plano pago):

1. Compre uma conta paga
2. No Dashboard → **Databases** → **Add a database**
3. Escolha PostgreSQL
4. Configure no `settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seu-username$banco_nome',
        'USER': 'seu-username',
        'PASSWORD': 'sua-senha',
        'HOST': 'seu-username.postgres.pythonanywhere-services.com',
        'PORT': '5432',
    }
}
```

Depois execute:
```bash
pip install psycopg2-binary
python manage.py migrate
```

---

### Email (SMTP)

Para enviar emails, no `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'seu-email@gmail.com'
EMAIL_HOST_PASSWORD = 'sua-senha-app'  # Use App Password se tiver 2FA
```

---

### Domínio Personalizado (Plano Pago)

1. Compre um domínio (GoDaddy, Namecheap, etc)
2. No Dashboard PythonAnywhere → **Web apps**
3. Adicione **Working directory** com seu domínio
4. Configure DNS apontando para PythonAnywhere

Detalhes: https://help.pythonanywhere.com/pages/OwnDomains/

---

## 🔄 Atualizar Código

Depois que estiver online, para fazer updates:

```bash
# No PythonAnywhere bash
cd calculadora
git pull origin main
workon calculadora
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Recarregar no Dashboard
# Dashboard → Web → Reload seu-username.pythonanywhere.com
```

---

## 📊 Monitorar a App

### Ver Logs

Dashboard → **Web** → **Log files**:
- **Server log**: Erros do servidor
- **Error log**: Erros do Django
- **Access log**: Requisições HTTP

### Diagnosticar Problemas

```bash
# No bash PythonAnywhere
cd calculadora
workon calculadora

# Testar consoleole
python manage.py shell

# Ver migrações
python manage.py showmigrations

# Checar configurações
python manage.py check
```

---

## 🆘 Troubleshooting

### Erro 502 Bad Gateway

1. Verifique o **Error log** no Dashboard
2. Comum:
   - Arquivo WSGI mal configurado
   - settings.py com erro
   - Virtualenv incorreto
   - Static files faltando

**Solução**: Verifique os logs e refaça os passos 8-11

### Static Files Não Carregam

```bash
# Recoletar
python manage.py collectstatic --noinput

# Verifique no Dashboard → Web → Static files
# URL deve ser /static/
# Directory deve ser /home/seu-username/calculadora/staticfiles/
```

### Banco de Dados Não Conecta

```bash
# Free tier usa SQLite (automático)
# Planos pagos: Verifique credentials de PostgreSQL

# Refaça as migrações
python manage.py migrate
```

### Admin não funciona

1. Verifique superuser:
```bash
python manage.py createsuperuser
```

2. Verifique ALLOWED_HOSTS em settings.py

3. Verifique static files estão carregando

---

## 📝 Resumo das Mudanças

| Aspecto | Heroku | PythonAnywhere |
|--------|--------|---|
| **Custo (Free)** | Sim | Sim |
| **Complexidade** | Docker necessário | Sem Docker |
| **Setup** | 15 min | 10 min |
| **Database Free** | PostgreSQL | SQLite |
| **Deploy Updates** | `git push` | Git + reload |
| **Controle** | Menos | Mais acesso |
| **Performance** | Melhor | Bom |

---

## 🎯 Próximos Passos

1. ✅ Criar conta PythonAnywhere
2. ✅ Seguir passos 1-12 acima
3. ✅ Acessar app em `https://seu-username.pythonanywhere.com`
4. ✅ Testar admin e funcionalidades
5. ✅ (Opcional) Comprar plano pago para PostgreSQL
6. ✅ (Opcional) Adicionar domínio personalizado

---

## 📚 Links Úteis

- [PythonAnywhere Help](https://help.pythonanywhere.com/)
- [PythonAnywhere Django](https://help.pythonanywhere.com/pages/DjangoWeb)
- [PythonAnywhere Troubleshooting](https://help.pythonanywhere.com/pages/Troubleshooting)

---

## ✨ Vantagem PythonAnywhere

**Você pode**: Acessar console bash, editar arquivos direto, ver logs em tempo real, e ter muito mais controle!

**Pronto?** Vá para https://www.pythonanywhere.com e comece! 🚀
