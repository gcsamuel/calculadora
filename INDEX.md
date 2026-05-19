# 📚 Documentação - Django + PythonAnywhere/Heroku

## 🎯 Comece Aqui

### ⭐ OPÇÃO 1: PythonAnywhere (Recomendado para Começar)
Se você quer **5 minutos** e **sem Docker**:
👉 [PYTHONANYWHERE_QUICK.md](PYTHONANYWHERE_QUICK.md)

### OPÇÃO 2: Heroku
Se você prefere e já tem Docker instalado:
👉 [QUICK_START.md](QUICK_START.md)

### OPÇÃO 3: Entender Tudo
👉 [ARCHITECTURE.md](ARCHITECTURE.md)

---

## 📖 Documentação Disponível

| Arquivo | Tempo | Propósito |
|---------|-------|----------|
| **PYTHONANYWHERE_QUICK.md** ⭐ | ⚡ 5 min | **Quick start PythonAnywhere** |
| **PYTHONANYWHERE_GUIDE.md** ⭐ | 📚 15 min | **Guia completo PythonAnywhere** |
| **QUICK_START.md** | ⚡ 5 min | Quick start Heroku |
| **SETUP_CHECKLIST.md** | ⏱️ 10 min | Checklist pré-requisitos |
| **DEPLOYMENT_GUIDE.md** | 📚 20 min | Guia completo Heroku |
| **DOCKER_GUIDE.md** | 🐳 10 min | Docker específico |
| **COMMANDS_REFERENCE.md** | 🔧 consulta | Referência rápida |
| **ARCHITECTURE.md** | 🏗️ 15 min | Visão geral arquitetura |

---

## 🌐 Plataformas Suportadas

### 🐍 PythonAnywhere ⭐ RECOMENDADO

**Vantagens:**
- ✨ Super simples (sem Docker necessário)
- 💰 Free tier funcional (512 MB storage)
- ⚡ Setup em 5 minutos
- 🎯 Feito exclusivamente para Python/Django
- 📊 Dashboard intuitivo
- 🔐 HTTPS automático
- 🎛️ Controle total (editar arquivos, ver logs)

**Limitações Free:**
- SQLite (sem PostgreSQL nativo)
- Sem acesso a APIs externas
- CPU limitada

**Melhor para:**
- Aprender Django
- Prototipagem rápida
- Pequenos projetos

👉 **Comece**: [PYTHONANYWHERE_QUICK.md](PYTHONANYWHERE_QUICK.md)

---

### ☁️ Heroku

**Vantagens:**
- 🏗️ Mais escalável
- 📊 PostgreSQL pago
- 🔗 APIs externas ilimitadas
- 🌍 Deploy para qualquer linguagem
- 🤖 CI/CD integrado

**Desvantagens:**
- 🐳 Requer Docker
- ⏱️ Setup 15+ minutos
- 💰 Planos começam em $7/mês

**Melhor para:**
- Produção profissional
- Escalabilidade
- Equipes

👉 **Comece**: [QUICK_START.md](QUICK_START.md)

---

## 📊 Comparação Rápida

| Aspecto | PythonAnywhere | Heroku |
|--------|---|---|
| **Free Tier** | ✅ Funcional | ❌ Descontinuado |
| **Setup** | ⚡ 5 min | ⚡⚡ 15 min |
| **Dificuldade** | 🟢 Fácil | 🟡 Médio |
| **Docker** | ❌ Não precisa | ✅ Necessário |
| **Database Free** | SQLite | - |
| **Controle** | 🟢 Total | 🟡 Limitado |
| **Escala** | 🟡 Média | 🟢 Alta |
| **Custo Pago** | $5/mês | $7+/mês |

---

## ✨ O que Você Tem

### 🐍 PythonAnywhere Ready
```
✅ Guias completos
✅ Setup super simples
✅ Sem Docker necessário
```

### 🐳 Docker (Opcional)
```
✅ Dockerfile - Python 3.11
✅ docker-compose.yml - Django + PostgreSQL
✅ Desenvolvimento local completo
```

### 🌐 Heroku Ready
```
✅ Procfile - Instruções
✅ runtime.txt - Python 3.11.9
✅ Guias completos
```

### ⚙️ Configuração Django
```
✅ requirements.txt - Atualizado
✅ config/settings.py - Production-ready
✅ .env + .env.example
✅ WhiteNoise - Statics
```

---

## 🚀 3 Opções de Deploy

### Opção 1: PythonAnywhere (Mais Fácil) ⭐
```bash
# 1. Criar conta
https://pythonanywhere.com

# 2. Clonar seu código
git clone seu-repo
cd calculadora

# 3. Setup (5 min)
mkvirtualenv --python=/usr/bin/python3.11 calculadora
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic

# 4. Configurar web app
# (Dashboard → Web → Add web app)

# 5. Pronto! 🎉
# https://seu-username.pythonanywhere.com
```

### Opção 2: Heroku
```bash
heroku create seu-app
git push heroku main
heroku run python manage.py migrate
# https://seu-app.herokuapp.com
```

### Opção 3: Docker (Desenvolvimento Local)
```bash
docker-compose up --build
# http://localhost:8000
```

---

## 🎯 Recomendação Final

| Situação | Escolha |
|----------|--------|
| **Primeira vez aprendendo Django** | 🐍 **PythonAnywhere** |
| **Quer ver rápido online** | 🐍 **PythonAnywhere** |
| **Projeto pequeno/médio** | 🐍 **PythonAnywhere** |
| **Produção empresarial** | ☁️ **Heroku** |
| **Quer escalabilidade profissional** | ☁️ **Heroku** |
| **Quer muita customização** | 🐳 **Docker** |

---

## 📚 Links Úteis

- 🐍 [PythonAnywhere Official](https://www.pythonanywhere.com)
- ☁️ [Heroku Official](https://www.heroku.com)
- 📖 [Django Docs](https://docs.djangoproject.com/)
- 🐳 [Docker Docs](https://docs.docker.com/)

---

## 🔗 Navegação Rápida

**Escolheu PythonAnywhere?**
- [PYTHONANYWHERE_QUICK.md](PYTHONANYWHERE_QUICK.md) ⚡ (5 min)
- [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) 📚 (Completo)

**Escolheu Heroku?**
- [QUICK_START.md](QUICK_START.md) ⚡ (5 min)
- [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md) 📚 (Completo)

**Tem problemas?**
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

**Procura comandos?**
- [COMMANDS_REFERENCE.md](COMMANDS_REFERENCE.md)

---

## 🎉 Parabéns!

Você tem tudo que precisa para:
- ✅ Desenvolvimento local
- ✅ Deploy online (2 opções!)
- ✅ Produção profissional

**Próximo passo?** Escolha uma plataforma acima e comece! 🚀
