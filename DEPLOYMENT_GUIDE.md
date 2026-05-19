# Guia de Deployment: Docker + Heroku

## 📋 Pré-requisitos

1. **Heroku CLI**: [Instalar Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
2. **Docker**: [Instalar Docker Desktop](https://www.docker.com/products/docker-desktop)
3. **Git**: Verificar se está instalado com `git --version`
4. **Conta Heroku**: [Criar conta no Heroku](https://www.heroku.com)

---

## 🚀 Passo 1: Testar Localmente com Docker

### 1.1 Construir a imagem Docker
```bash
docker build -t calculadora:latest .
```

### 1.2 Usar Docker Compose (recomendado)
```bash
docker-compose up --build
```

A aplicação estará disponível em: `http://localhost:8000`

### 1.3 Executar migrações
```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

---

## 🌐 Passo 2: Deploy no Heroku

### 2.1 Login no Heroku
```bash
heroku login
```

### 2.2 Criar uma nova aplicação Heroku
```bash
heroku create seu-app-name
```

Substitua `seu-app-name` por um nome único (ex: `calculadora-app-12345`)

### 2.3 Adicionar PostgreSQL (banco de dados)
```bash
heroku addons:create heroku-postgresql:essential-0 --app seu-app-name
```

### 2.4 Configurar variáveis de ambiente
```bash
# Gerar uma SECRET_KEY segura
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Configurar no Heroku
heroku config:set DEBUG=False --app seu-app-name
heroku config:set SECRET_KEY=sua-secret-key-segura --app seu-app-name
heroku config:set ALLOWED_HOSTS=seu-app-name.herokuapp.com --app seu-app-name
```

### 2.5 Fazer deploy
```bash
git push heroku main
```

(Se seu branch principal se chama `master`, use: `git push heroku master`)

### 2.6 Executar migrações no Heroku
```bash
heroku run python manage.py migrate --app seu-app-name
heroku run python manage.py createsuperuser --app seu-app-name
```

### 2.7 Verificar o status
```bash
heroku logs --tail --app seu-app-name
```

### 2.8 Abrir a aplicação
```bash
heroku open --app seu-app-name
```

---

## 🔧 Troubleshooting

### Erro: "Application error"
Verifique os logs:
```bash
heroku logs --tail --app seu-app-name
```

### Erro: "Collectstatic failed"
Tente:
```bash
heroku run python manage.py collectstatic --noinput --app seu-app-name
```

### Erro de conexão com banco de dados
Verifique se o PostgreSQL foi criado:
```bash
heroku addons --app seu-app-name
```

### Resetar o banco de dados
```bash
heroku pg:reset DATABASE --confirm seu-app-name
heroku run python manage.py migrate --app seu-app-name
```

---

## 📊 Monitorar a Aplicação

```bash
# Ver variáveis de ambiente
heroku config --app seu-app-name

# Ver logs em tempo real
heroku logs --tail --app seu-app-name

# Acessar console Django
heroku run python manage.py shell --app seu-app-name

# Ver status dos dyos
heroku ps --app seu-app-name
```

---

## 🔒 Segurança

✅ Sempre use `DEBUG=False` em produção
✅ Gere uma `SECRET_KEY` segura
✅ Adicione seu domínio em `ALLOWED_HOSTS`
✅ Use SSL (Heroku fornece automaticamente)
✅ Não commit arquivos `.env` (use `.env.example`)

---

## 📝 Arquivos Criados

- **Dockerfile**: Define como construir a imagem Docker
- **docker-compose.yml**: Orquestra containers localmente
- **.dockerignore**: Exclui arquivos desnecessários do Docker
- **Procfile**: Instruções para Heroku
- **runtime.txt**: Especifica versão do Python
- **requirements.txt**: Atualizado com dependências de produção
- **config/settings.py**: Configurado para ambiente de produção

---

## 🎯 Próximas Passos

1. ✅ Testar localmente com Docker Compose
2. ✅ Fazer deploy no Heroku
3. ✅ Configurar domínio personalizado (opcional)
4. ✅ Configurar CI/CD (opcional)
5. ✅ Adicionar backups automáticos do banco de dados

---

## 🆘 Suporte

- [Documentação Heroku Django](https://devcenter.heroku.com/articles/django-app-configuration)
- [Documentação Docker](https://docs.docker.com/)
- [Documentação Django](https://docs.djangoproject.com/)
