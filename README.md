# 🧮 Calculadora Django

Projeto Django simples com uma calculadora que soma, subtrai, multiplica e divide.

**Agora com suporte a Docker, PythonAnywhere e Heroku!** 🐳 + 🐍 + ☁️

---

## 🚀 Começar Rápido

### 🐍 PythonAnywhere (Recomendado - Mais Simples!)
```bash
# 1. Criar conta em pythonanywhere.com
# 2. Clonar repositório
# 3. Seguir guia em 5 minutos

# 👉 Leia: PYTHONANYWHERE_QUICK.md
```

### ☁️ Heroku
```bash
heroku create seu-app-name
git push heroku main
```

### 🐳 Docker (Local)
```bash
docker-compose up --build
# http://localhost:8000
```

👉 **Central de Documentação**: [INDEX.md](INDEX.md) ⭐

---

## 📖 Documentação

| Plataforma | Tempo | Arquivo |
|-----------|-------|--------|
| 🐍 **PythonAnywhere** (Recomendado) | 5 min | [PYTHONANYWHERE_QUICK.md](PYTHONANYWHERE_QUICK.md) |
| 🐍 PythonAnywhere (Completo) | 15 min | [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) |
| ☁️ Heroku | 5 min | [QUICK_START.md](QUICK_START.md) |
| 🐳 Docker | 10 min | [DOCKER_GUIDE.md](DOCKER_GUIDE.md) |
| 📚 Tudo | - | [INDEX.md](INDEX.md) |

---

## 🐍 Como rodar com venv (Tradicional)

1. Ative o ambiente virtual:

```bash
cd /home/devmobhis/calculadora
source .venv/bin/activate
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Inicie o servidor Django:

```bash
python manage.py runserver 0.0.0.0:8000
```

4. Acesse a aplicação no navegador:

```text
http://127.0.0.1:8000/
```

## Acessar de outro computador na mesma rede

1. Descubra o IP do seu computador (por exemplo `192.168.0.10`).
2. No outro computador, abra:

```text
http://192.168.0.10:8000/
```

> Atenção: ambos os computadores devem estar na mesma rede local e o firewall deve permitir conexões na porta `8000`.

---

## 🐳 Com Docker (Local)

```bash
# Build e start com database PostgreSQL
docker-compose up --build

# Fazer migrações
docker-compose exec web python manage.py migrate

# Criar superuser
docker-compose exec web python manage.py createsuperuser

# Parar
docker-compose down
```

---

## 🌐 Deploy no Heroku (Production)

```bash
# Login
heroku login

# Criar app
heroku create seu-app-name

# Adicionar database PostgreSQL
heroku addons:create heroku-postgresql:essential-0 --app seu-app-name

# Deploy
git push heroku main

# Migrar
heroku run python manage.py migrate --app seu-app-name
heroku run python manage.py createsuperuser --app seu-app-name

# Abrir
heroku open --app seu-app-name
```

👉 **Guia Completo**: [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

---

## 📦 Stack Tecnológico

- **Backend**: Django 5.2.14
- **Servidor**: Gunicorn 23.0.0 (produção)
- **Database**: 
  - SQLite (desenvolvimento local)
  - PostgreSQL (Docker local & Heroku)
- **Container**: Docker + Docker Compose
- **Deploy**: Heroku
- **Statics**: WhiteNoise 6.6.0

---

## 📁 Estrutura do Projeto

```
calculadora/
├── Dockerfile ........................ Imagem Docker
├── docker-compose.yml .............. Django + PostgreSQL local
├── Procfile ......................... Instruções Heroku
├── runtime.txt ...................... Versão Python
├── requirements.txt ................. Dependências Python
├── manage.py ........................ Script Django
├── .env ............................ Variáveis (não commitar)
├── .env.example .................... Template de variáveis
├── README.md ....................... Este arquivo
├── INDEX.md ........................ Central de documentação
├── QUICK_START.md .................. Começo rápido
├── DEPLOYMENT_GUIDE.md ............ Guia completo
├── DOCKER_GUIDE.md ................ Docker específico
├── COMMANDS_REFERENCE.md ......... Comandos úteis
├── ARCHITECTURE.md ............... Visão geral
├── SETUP_CHECKLIST.md ........... Pré-requisitos
│
├── config/ ......................... Configurações Django
│   ├── settings.py ............... Configuração (production-ready)
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
│
├── calculadora/ ................... Aplicação principal
│   ├── views.py
│   ├── urls.py
│   ├── models.py
│   ├── admin.py
│   ├── templates/
│   │   └── calculadora/
│   │       └── home.html
│   └── static/
│       └── calculadora/
│           └── style.css
│
├── db.sqlite3 ..................... Database (desenvolvimento)
└── staticfiles/ ................... Arquivos estáticos (gerado)
```

---

## Versionar no GitHub

1. Se ainda não tiver, crie um repositório no GitHub.
2. No terminal:

```bash
git add .
git commit -m "Adicionar calculadora Django com Docker e Heroku"
```

3. Configure o `origin` caso ainda não tenha feito:

```bash
git remote add origin https://github.com/seu-usuario/calculadora.git
```

4. Envie para o GitHub:

```bash
git push -u origin main
```

---

## 🔐 Segurança em Produção

✅ DEBUG=False no Heroku  
✅ SECRET_KEY via variável de ambiente  
✅ ALLOWED_HOSTS configurado  
✅ SSL automático no Heroku  
✅ WhiteNoise para arquivos estáticos  
✅ Cookies seguros  
✅ CSRF proteção ativada  

---

## 📚 Recursos Úteis

- [Django Documentation](https://docs.djangoproject.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Heroku Devcenter](https://devcenter.heroku.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- [WhiteNoise](http://whitenoise.evans.io/)

---

## ✨ Mudanças Recentes

- ✅ Adicionado Dockerfile para containerização
- ✅ docker-compose.yml para desenvolvimento local com PostgreSQL
- ✅ Procfile e runtime.txt para Heroku
- ✅ Configuração Django production-ready
- ✅ WhiteNoise para servir statics em produção
- ✅ Documentação completa incluída

---

## 🆘 Precisa de Ajuda?

- 📖 Leia [INDEX.md](INDEX.md) para navegar pela documentação
- 🐳 Dúvidas Docker? Veja [DOCKER_GUIDE.md](DOCKER_GUIDE.md)
- 🌐 Deploy com dúvidas? Veja [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- 🔧 Procura um comando? Veja [COMMANDS_REFERENCE.md](COMMANDS_REFERENCE.md)

---

## 📝 Licença

Este projeto é de código aberto.

---

**🎉 Sua app está pronta para o mundo!**

5. Depois, para atualizar:

```bash
git add .
git commit -m "Atualização"
git push
```
# calculadora
