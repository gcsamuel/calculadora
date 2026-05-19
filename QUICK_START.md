# 🚀 Quick Start - Deploy em 5 Minutos

## Local (Docker Compose)

```bash
# 1. Build e start
docker-compose up --build

# 2. Em outro terminal, migrate
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# 3. Acesse: http://localhost:8000
```

---

## Heroku (Production)

```bash
# 1. Login e criar app
heroku login
heroku create seu-app-name

# 2. Adicionar banco de dados
heroku addons:create heroku-postgresql:essential-0 --app seu-app-name

# 3. Gerar SECRET_KEY
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 4. Configurar variáveis
heroku config:set DEBUG=False --app seu-app-name
heroku config:set SECRET_KEY=SUA_CHAVE_AQUI --app seu-app-name
heroku config:set ALLOWED_HOSTS=seu-app-name.herokuapp.com --app seu-app-name

# 5. Deploy
git push heroku main

# 6. Migrar banco
heroku run python manage.py migrate --app seu-app-name
heroku run python manage.py createsuperuser --app seu-app-name

# 7. Abrir
heroku open --app seu-app-name
```

---

## Arquivos Criados/Modificados

✅ **Dockerfile** - Imagem Docker com Python 3.11
✅ **.dockerignore** - Exclui arquivos desnecessários
✅ **docker-compose.yml** - Django + PostgreSQL local
✅ **Procfile** - Instruções para Heroku
✅ **runtime.txt** - Python 3.11.9
✅ **requirements.txt** - Dependências atualizadas
✅ **config/settings.py** - Configurado para produção
✅ **.env** - Variáveis locais (não commitar)
✅ **.env.example** - Template de variáveis
✅ **.gitignore** - Melhorado
✅ **DEPLOYMENT_GUIDE.md** - Guia completo
✅ **DOCKER_GUIDE.md** - Guia Docker

---

## 📊 O que muda entre Local e Produção

| Aspecto | Local | Produção |
|--------|-------|----------|
| Database | SQLite | PostgreSQL |
| Debug | True | False |
| Static Files | Django serve | WhiteNoise |
| SSL | Não | Sim |
| Secret Key | Default | Variável de ambiente |

---

## 🔗 Acessar Depois do Deploy

```
https://seu-app-name.herokuapp.com
https://seu-app-name.herokuapp.com/admin
```

---

## 📞 Troubleshooting Rápido

```bash
# Ver logs
heroku logs --tail --app seu-app-name

# Reset do banco
heroku pg:reset DATABASE --confirm seu-app-name
heroku run python manage.py migrate --app seu-app-name

# Ver variáveis
heroku config --app seu-app-name
```

---

🎉 **Pronto! Sua app está online!**
