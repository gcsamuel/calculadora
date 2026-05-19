# 🐳 Docker - Guia Rápido

## Construir a Imagem

```bash
docker build -t calculadora:latest .
```

## Executar com Docker Compose

```bash
# Subir todos os serviços (Django + PostgreSQL)
docker-compose up --build

# Ou em background
docker-compose up -d

# Ver logs
docker-compose logs -f web
```

## Executar Comandos Django

```bash
# Migrações
docker-compose exec web python manage.py migrate

# Criar superusuário
docker-compose exec web python manage.py createsuperuser

# Coletar arquivos estáticos
docker-compose exec web python manage.py collectstatic

# Shell do Django
docker-compose exec web python manage.py shell
```

## Parar os Serviços

```bash
docker-compose down

# Com limpeza de volumes
docker-compose down -v
```

## Testar Localmente

1. Acesse: http://localhost:8000
2. Admin: http://localhost:8000/admin

## Rebuild da Imagem

```bash
# Se mudar requirements.txt
docker-compose up --build
```

## Troubleshooting

```bash
# Ver status dos containers
docker-compose ps

# Ver logs
docker-compose logs web

# Acessar container
docker-compose exec web bash

# Verificar porta 8000
lsof -i :8000
```
