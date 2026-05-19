# 🔧 Troubleshooting - Problemas Comuns

## 🐳 Docker

### Erro: "Docker daemon is not running"
```bash
# Linux
sudo systemctl start docker

# Mac
open /Applications/Docker.app
```

### Erro: "Permission denied while trying to connect to Docker daemon"
```bash
# Linux
sudo usermod -aG docker $USER
# Logout e login novamente
```

### Erro: "Port 8000 already in use"
```bash
# Linux/Mac
lsof -i :8000
kill -9 <PID>

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

### Erro: "Database connection refused"
```bash
# Reiniciar compose com volumes limpos
docker-compose down -v
docker-compose up --build
```

### Build falha com "permission denied"
```bash
# Dar permissão ao arquivo
chmod +x Dockerfile

# Ou rebuildcomm --no-cache
docker-compose up --build --no-cache
```

---

## 🌐 Heroku

### Erro: "Application error"

**Verificar logs:**
```bash
heroku logs --tail --app seu-app-name
```

**Causas comuns:**
1. Migrações não executadas
2. DATABASE_URL mal configurado
3. SECRET_KEY faltando
4. Porta não configurada corretamente

**Solução:**
```bash
heroku run python manage.py migrate --app seu-app-name
heroku restart --app seu-app-name
```

### Erro: "Build failed"

```bash
# Ver logs de build
heroku logs --source heroku --tail --app seu-app-name

# Reconstruir
git commit --allow-empty -m "Rebuild"
git push heroku main
```

### Erro: "Collectstatic failed"

```bash
heroku run python manage.py collectstatic --noinput --app seu-app-name
```

### Erro: "Database URL environment variable not set"

```bash
# Verificar
heroku config --app seu-app-name

# Se DATABASE_URL falta, adicionar addon
heroku addons:create heroku-postgresql:essential-0 --app seu-app-name
```

### Erro: "Permission denied" no Heroku CLI

```bash
# Relogin
heroku logout
heroku login
```

### Não consigo acessar a app

1. Verificar se está running:
```bash
heroku ps --app seu-app-name
```

2. Se dyno está "crashed", restart:
```bash
heroku restart --app seu-app-name
```

3. Se tiver mais de 1 dyno, scale para 1:
```bash
heroku ps:scale web=1 --app seu-app-name
```

### App fica offline depois de 30 minutos

Heroku para dyos free que não recebem tráfego.

**Solução**: Fazer upgrade para plano pago ou usar serviço como [UptimeRobot](https://uptimerobot.com) para manter vivo.

---

## 🐍 Django

### Erro: "No such table: auth_user"

Migrações não foram executadas:

```bash
# Local
python manage.py migrate

# Docker
docker-compose exec web python manage.py migrate

# Heroku
heroku run python manage.py migrate --app seu-app-name
```

### Erro: "Static files not found"

```bash
# Local
python manage.py collectstatic

# Docker
docker-compose exec web python manage.py collectstatic

# Heroku (automático no deploy)
heroku run python manage.py collectstatic --app seu-app-name
```

### 500 Internal Server Error

```bash
# Verificar logs
# Local: console do terminal
# Docker: docker-compose logs web
# Heroku: heroku logs --tail --app seu-app-name

# Comum: arquivo .env faltando ou mal configurado
```

### "SECRET_KEY" errors

Verificar arquivo `.env`:
```bash
cat .env | grep SECRET_KEY
```

Se vazio, copiar de `.env.example`:
```bash
cp .env.example .env
```

### "ALLOWED_HOSTS" error

Adicionar seu domínio:
```bash
# Local
echo "ALLOWED_HOSTS=localhost,127.0.0.1,seu-dominio.com" >> .env

# Heroku
heroku config:set ALLOWED_HOSTS=seu-app.herokuapp.com --app seu-app-name
```

---

## 🔐 Variáveis de Ambiente

### Como verificar variáveis

```bash
# Local
cat .env

# Docker (interno)
docker-compose exec web env

# Heroku
heroku config --app seu-app-name
```

### Variável não está sendo lida

1. Verificar se `.env` existe
2. Se está usando Docker Compose, verificar `docker-compose.yml`
3. Reiniciar serviços após alterar `.env`

```bash
docker-compose down
docker-compose up
```

### Alterar variável em produção

```bash
heroku config:set VARIAVEL=novo-valor --app seu-app-name

# Heroku reinicia app automaticamente
```

---

## 🚀 Deploy

### "Git remote not found"

```bash
git remote add heroku https://git.heroku.com/seu-app-name.git
```

### Deploy para branch errado

```bash
# Se seu branch é 'main' e não 'master'
git push heroku main

# Se em branch local 'develop'
git push heroku develop:main
```

### Commits pendentes

```bash
git status  # Ver mudanças
git add .
git commit -m "mensagem"
git push heroku main
```

### Rollback de deploy

```bash
# Ver releases
heroku releases --app seu-app-name

# Voltar para release anterior
heroku releases:rollback v123 --app seu-app-name
```

---

## 📊 Performance

### App muito lento

1. **Ver dyno**:
```bash
heroku ps --app seu-app-name
```

2. **Upgrade dyno** (pago):
```bash
heroku ps:type web=standard-1x --app seu-app-name
```

3. **Ver logs de erro**:
```bash
heroku logs --source app --tail --app seu-app-name
```

### Banco de dados lento

```bash
# Ver stats
heroku pg:info --app seu-app-name

# Upgrade database (pago)
heroku addons:upgrade heroku-postgresql:standard-0 --app seu-app-name
```

---

## 📞 Recursos de Ajuda

### Verificar status do Heroku

```bash
curl https://status.heroku.com/api/v4/status.json
```

### Ver limite de requisições

```bash
heroku apps:info seu-app-name
```

### Contatar suporte Heroku

- [Heroku Support](https://support.heroku.com)
- Status: https://status.heroku.com

---

## ✅ Checklist de Diagnóstico

```
☐ Docker está rodando?
☐ docker --version mostra versão?
☐ Heroku CLI instalado?
☐ Git configurado?
☐ .env existe com variáveis corretas?
☐ DATABASE_URL está configurado?
☐ SECRET_KEY foi gerada?
☐ ALLOWED_HOSTS inclui seu domínio?
☐ Migrações foram executadas?
☐ Superuser foi criado?
☐ debug=False em produção?
```

Se tudo ✅, sua app deve estar funcionando!

---

## 🆘 Nada funcionou?

1. 📖 Leia [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. 🔧 Consulte [COMMANDS_REFERENCE.md](COMMANDS_REFERENCE.md)
3. 📊 Verifique logs:
   - Local: Terminal
   - Docker: `docker-compose logs web`
   - Heroku: `heroku logs --tail`

---

**Ainda com problemas?** Consulte a documentação oficial:
- [Django Docs](https://docs.djangoproject.com/)
- [Docker Docs](https://docs.docker.com/)
- [Heroku Docs](https://devcenter.heroku.com/)
