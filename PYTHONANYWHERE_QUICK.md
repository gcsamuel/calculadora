# ⚡ PythonAnywhere Quick Start (5 minutos)

## Resumo Executivo

PythonAnywhere = Django hospedado na nuvem **sem Docker**, super simples.

---

## 🎯 O Essencial em 5 Passos

### 1️⃣ Criar Conta
👉 https://www.pythonanywhere.com → Free account

### 2️⃣ Clonar seu código
```bash
git clone https://github.com/seu-usuario/calculadora.git
cd calculadora
```

### 3️⃣ Setup ambiente
```bash
mkvirtualenv --python=/usr/bin/python3.11 calculadora
pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
python manage.py createsuperuser
```

### 4️⃣ Configurar web app
- Dashboard → Web → Add a new web app
- Manual configuration → Python 3.11
- Editar arquivo WSGI (veja abaixo ⬇️)
- Configurar Static Files mapping

### 5️⃣ Reload e Pronto! 🎉
- Clique em **Reload**
- Acesse: `https://seu-username.pythonanywhere.com`

---

## 📋 WSGI File (Cole Isto)

No Dashboard → Web → seu domínio → Editar WSGI:

```python
import os
import sys

path = '/home/seu-username/calculadora'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

⚠️ **Troque `seu-username` pelo seu username!**

---

## 📁 Static Files Mapping

No Dashboard → Web → seu domínio:

**URL**: `/static/`
**Directory**: `/home/seu-username/calculadora/staticfiles/`

---

## ⚙️ settings.py - Ajustar

```python
ALLOWED_HOSTS = ['seu-username.pythonanywhere.com', 'localhost']
```

---

## 🔄 Atualizar Código Depois

```bash
# No bash PythonAnywhere
cd calculadora
git pull origin main
workon calculadora
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Depois no Dashboard: Clique em Reload
```

---

## 🆘 Erros Comuns

| Erro | Solução |
|------|---------|
| 502 Bad Gateway | Checar Error log no Dashboard |
| CSS/JS não carrega | Refazer: `python manage.py collectstatic` |
| Banco não conecta | Refazer: `python manage.py migrate` |
| Admin não abre | Verifique ALLOWED_HOSTS em settings.py |

---

## ✨ URLs

- **App**: `https://seu-username.pythonanywhere.com`
- **Admin**: `https://seu-username.pythonanywhere.com/admin`

---

## 📚 Referência Completa

👉 [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) - Guia completo

---

**Pronto!** 🚀 Sua app está online em menos de 5 minutos!
