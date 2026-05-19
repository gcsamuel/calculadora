# 📖 Referência de Comandos

## 🐳 Docker & Docker Compose

### Build
```bash
# Build da imagem
docker build -t calculadora:latest .

# Build via compose
docker-compose up --build
```

### Execução
```bash
# Subir stack completo
docker-compose up

# Em background
docker-compose up -d

# Build e start
docker-compose up --build

# Parar
docker-compose down

# Parar e remover volumes
docker-compose down -v
```

### Logs e Debug
```bash
# Ver logs
docker-compose logs

# Seguir logs em tempo real
docker-compose logs -f web

# Ver status
docker-compose ps

# Acessar container
docker-compose exec web bash

# Executar comando
docker-compose exec web python manage.py shell
```

---

## 🌐 Heroku

### Setup Inicial
```bash
# Login
heroku login

# Criar app
heroku create seu-app-name

# Deletar app (cuidado!)
heroku apps:destroy seu-app-name --confirm seu-app-name
```

### Banco de Dados
```bash
# Criar PostgreSQL
heroku addons:create heroku-postgresql:essential-0 --app seu-app-name

# Ver addons
heroku addons --app seu-app-name

# Deletar add-on
heroku addons:destroy heroku-postgresql:essential-0 --app seu-app-name

# Resetar banco
heroku pg:reset DATABASE --confirm seu-app-name

# Ver status do banco
heroku pg:info --app seu-app-name
```

### Configuração
```bash
# Definir variável
heroku config:set KEY=VALUE --app seu-app-name

# Ver todas as variáveis
heroku config --app seu-app-name

# Remover variável
heroku config:unset KEY --app seu-app-name

# Exemplo: Gerar SECRET_KEY segura
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Configurar DEBUG
heroku config:set DEBUG=False --app seu-app-name
```

### Deploy
```bash
# Deploy
git push heroku main

# Deploy de branch específico
git push heroku seu-branch:main

# Deploy com commit específico
git push heroku seu-commit:main --force
```

### Migrações & Admin
```bash
# Fazer migrações
heroku run python manage.py migrate --app seu-app-name

# Criar superuser interativo
heroku run python manage.py createsuperuser --app seu-app-name

# Coletar estáticos
heroku run python manage.py collectstatic --noinput --app seu-app-name

# Shell Django
heroku run python manage.py shell --app seu-app-name
```

### Monitoramento
```bash
# Logs em tempo real
heroku logs --tail --app seu-app-name

# Últimos 50 logs
heroku logs -n 50 --app seu-app-name

# Ver status dos dyos
heroku ps --app seu-app-name

# Restartar app
heroku restart --app seu-app-name

# Escalar dyos (caro!)
heroku ps:scale web=2 --app seu-app-name
```

### Acesso
```bash
# Abrir app no navegador
heroku open --app seu-app-name

# Admin
heroku open /admin --app seu-app-name
```

---

## 🐍 Django

### Migrações (Local)
```bash
# Ver migrations pendentes
python manage.py showmigrations

# Fazer migrações
python manage.py migrate

# Criar migration para app
python manage.py makemigrations calculadora

# Ver detalhes de migration
python manage.py sqlmigrate calculadora 0001
```

### Superuser
```bash
# Criar
python manage.py createsuperuser

# Alterar senha
python manage.py changepassword username
```

### Admin & Shell
```bash
# Django shell
python manage.py shell

# Python shell (com settings)
python manage.py shell_plus  # (requer django-extensions)

# Admin site
python manage.py runserver
# Acesse: http://localhost:8000/admin
```

### Estáticos
```bash
# Coletar
python manage.py collectstatic

# Sem confirmação
python manage.py collectstatic --noinput

# Listar
python manage.py findstatic --list
```

---

## 📝 Git

### Commit e Push
```bash
# Status
git status

# Adicionar tudo
git add .

# Commit
git commit -m "mensagem"

# Push para main
git push origin main

# Push para Heroku
git push heroku main
```

### Branches
```bash
# Ver branches
git branch

# Criar branch
git checkout -b nome-branch

# Trocar branch
git checkout nome-branch

# Deletar branch
git branch -d nome-branch
```

---

## 🔧 Variáveis de Ambiente

### Local (.env)
```
DEBUG=True
SECRET_KEY=sua-chave
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/calculadora
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Heroku
```bash
# Configurar tudo de uma vez
heroku config:set \
  DEBUG=False \
  SECRET_KEY=sua-chave-segura \
  ALLOWED_HOSTS=seu-app.herokuapp.com \
  --app seu-app-name
```

---

## 📊 Docker Compose Útil

### Atualizar dependências
```bash
docker-compose exec web pip install --upgrade -r requirements.txt
```

### Criar estrutura inicial
```bash
docker-compose exec web python manage.py startapp nova_app
```

### Limpar tudo (⚠️ Cuidado!)
```bash
docker-compose down -v
# Isso remove volumes (banco de dados)
```

---

## 🆘 Troubleshooting

### Port já em uso
```bash
# Linux/Mac
lsof -i :8000

# Matar processo
kill -9 PID

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Reset PostgreSQL Local
```bash
docker-compose down -v
docker-compose up -d db
docker-compose up web
```

### Limpar cache Docker
```bash
docker system prune
docker system prune -a  # Mais agressivo
```

### Rebuild completo
```bash
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```

---

## 🚀 Commands Mais Usados

```bash
# Local - Start
docker-compose up --build

# Local - Migrate
docker-compose exec web python manage.py migrate

# Local - Shell
docker-compose exec web python manage.py shell

# Local - Stop
docker-compose down

# Heroku - Deploy
git push heroku main

# Heroku - Logs
heroku logs --tail --app seu-app-name

# Heroku - Migrate
heroku run python manage.py migrate --app seu-app-name

# Heroku - Open
heroku open --app seu-app-name
```

---

💡 **Dica**: Copie e cole estes comandos conforme necessário. Customize `seu-app-name` e `seu-app.herokuapp.com`.
