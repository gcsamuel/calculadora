# ✅ Checklist: Antes de Começar

## 🔍 Pré-requisitos (Verificar Primeiro)

- [ ] **Git** instalado
  ```bash
  git --version
  ```

- [ ] **Docker & Docker Compose** instalado
  ```bash
  docker --version
  docker-compose --version
  ```

- [ ] **Python 3.11+** instalado (opcional, Docker fornece)
  ```bash
  python --version
  ```

- [ ] **Heroku CLI** instalado
  ```bash
  heroku --version
  ```

- [ ] **Conta Heroku** criada
  - Acesse: https://www.heroku.com

---

## 📋 Arquivos Já Criados ✨

Na raiz do projeto, você agora tem:

### Docker
- ✅ `Dockerfile` - Imagem Docker
- ✅ `.dockerignore` - Arquivos ignorados no build
- ✅ `docker-compose.yml` - Django + PostgreSQL local

### Heroku
- ✅ `Procfile` - Como executar no Heroku
- ✅ `runtime.txt` - Versão do Python

### Configuração Django
- ✅ `requirements.txt` - Dependências atualizadas
- ✅ `config/settings.py` - Configurado para produção

### Variáveis de Ambiente
- ✅ `.env` - Local (não commitar)
- ✅ `.env.example` - Template

### Documentação
- ✅ `QUICK_START.md` - Rápido (leia isto primeiro!)
- ✅ `DEPLOYMENT_GUIDE.md` - Guia completo
- ✅ `DOCKER_GUIDE.md` - Docker específico
- ✅ `ARCHITECTURE.md` - Visão geral
- ✅ `COMMANDS_REFERENCE.md` - Comandos úteis
- ✅ `SETUP_CHECKLIST.md` - Este arquivo

---

## 🚀 Próximos Passos (Em Ordem)

### 1️⃣ Testar Localmente (5 minutos)
```bash
cd /home/devmobhis/calculadora

# Build e start
docker-compose up --build

# Em outro terminal
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser

# Testar
# Abra: http://localhost:8000
# Admin: http://localhost:8000/admin
```

**✅ Sucesso?** Prossiga para o passo 2.

### 2️⃣ Preparar para Heroku (2 minutos)
```bash
# Login
heroku login

# Criar app
heroku create seu-app-name-unico

# Ex: heroku create calculadora-app-12345
```

**✅ App criado?** Prossiga para o passo 3.

### 3️⃣ Configurar Banco de Dados (1 minuto)
```bash
heroku addons:create heroku-postgresql:essential-0 --app seu-app-name-unico
```

**✅ PostgreSQL adicionado?** Prossiga para o passo 4.

### 4️⃣ Gerar SECRET_KEY (30 segundos)
```bash
# Copie a output deste comando
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Você vai usar na próxima etapa
```

### 5️⃣ Configurar Variáveis (1 minuto)
```bash
heroku config:set \
  DEBUG=False \
  SECRET_KEY=COLE_A_CHAVE_GERADA_ACIMA \
  ALLOWED_HOSTS=seu-app-name-unico.herokuapp.com \
  --app seu-app-name-unico
```

**✅ Variáveis configuradas?** Prossiga para o passo 6.

### 6️⃣ Deploy (2 minutos)
```bash
git add .
git commit -m "Add Docker and Heroku config"
git push heroku main
```

**Aguarde o deploy terminar...**

### 7️⃣ Migrações e Admin (1 minuto)
```bash
heroku run python manage.py migrate --app seu-app-name-unico
heroku run python manage.py createsuperuser --app seu-app-name-unico
```

### 8️⃣ Acessar! 🎉
```bash
heroku open --app seu-app-name-unico

# Ou acesse manualmente:
# https://seu-app-name-unico.herokuapp.com
# https://seu-app-name-unico.herokuapp.com/admin
```

---

## ⚠️ Cuidados Importantes

1. **Nunca commite `.env`** (já está no .gitignore)
2. **Mantenha `requirements.txt` atualizado** se instalar novos pacotes
3. **Use `DEBUG=False` em produção** (está configurado)
4. **Salve a SECRET_KEY gerada** em lugar seguro
5. **Não altere `Dockerfile` ou `Procfile`** sem saber o que está fazendo
6. **Backups do Heroku** são pagos (free tier não tem)

---

## 🔧 Se Algo Der Errado

### Erro: "Application error"
```bash
heroku logs --tail --app seu-app-name-unico
# Procure pela mensagem de erro
```

### Erro: "Permission denied" no Docker
```bash
# Linux: Adicione seu usuário ao grupo docker
sudo usermod -aG docker $USER
# Reinicie o terminal
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
docker-compose down -v
docker-compose up --build
```

---

## 📚 Documentação Completa

Leia nesta ordem:
1. ✅ **QUICK_START.md** - Começo rápido
2. ✅ **DEPLOYMENT_GUIDE.md** - Passo a passo completo
3. ✅ **DOCKER_GUIDE.md** - Se tiver dúvidas sobre Docker
4. ✅ **COMMANDS_REFERENCE.md** - Comandos úteis
5. ✅ **ARCHITECTURE.md** - Entender a estrutura

---

## 🎯 O que mudou no seu projeto

```
calculadora/
├── Dockerfile ..................... 🆕 Image Docker
├── .dockerignore .................. 🆕 Arquivos ignorados
├── docker-compose.yml ............ 🆕 Django + DB local
├── Procfile ....................... 🆕 Para Heroku
├── runtime.txt .................... 🆕 Versão Python
├── requirements.txt ............... 🔄 Atualizado (gunicorn, psycopg2, etc)
├── .env ............................ 🆕 Variáveis locais
├── .env.example ................... 🆕 Template
├── .gitignore ..................... 🔄 Melhorado
├── config/
│   └── settings.py ............... 🔄 Configurado para produção
├── QUICK_START.md ................. 🆕 Começar rápido
├── DEPLOYMENT_GUIDE.md ........... 🆕 Guia completo
├── DOCKER_GUIDE.md ............... 🆕 Docker específico
├── ARCHITECTURE.md ............... 🆕 Visão geral
├── COMMANDS_REFERENCE.md ......... 🆕 Comandos úteis
└── SETUP_CHECKLIST.md ............ 🆕 Este arquivo
```

---

## ✨ Resumo

- 🐳 **Docker** para containerização
- 🌐 **Heroku** para deploy em produção
- 📦 **PostgreSQL** em produção (SQLite em desenvolvimento)
- 🚀 **Gunicorn** como servidor web
- 🔐 **WhiteNoise** para arquivos estáticos
- 📝 **Documentação completa** incluída

---

## 🎊 Você está pronto!

Siga o checklist acima e sua aplicação estará online em **menos de 15 minutos**.

**Próximo passo**: Abra o `QUICK_START.md` e comece! 🚀
