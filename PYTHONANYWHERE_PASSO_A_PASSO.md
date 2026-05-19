# 🎯 PythonAnywhere: Do Zero ao Deploy (Passo a Passo Completo)

## ℹ️ Antes de Começar

Seu código Django já está pronto. Você só precisa:
- Conta no GitHub (para versionar código)
- Conta no PythonAnywhere (para hospedar)
- 10 minutos de tempo

---

## PASSO 1: Preparar Código no GitHub (3 minutos)

Seu código precisa estar no GitHub para você acessar no PythonAnywhere.

### Se JÁ TEM repositório no GitHub:

```bash
cd /home/devmobhis/calculadora

# Atualizar código
git add .
git commit -m "Calculadora Django - Pronto para PythonAnywhere"

# Enviar
git push origin main
```

### Se NÃO TEM repositório:

1. Vá para https://github.com/new
2. Crie repositório com nome "calculadora"
3. No seu computador:

```bash
cd /home/devmobhis/calculadora

# Inicializar git
git init

# Adicionar tudo
git add .

# Commit inicial
git commit -m "Calculadora Django - Inicial"

# Adicionar origem (SUBSTITUA seu-usuario)
git remote add origin https://github.com/seu-usuario/calculadora.git

# Renomear branch se necessário
git branch -M main

# Enviar
git push -u origin main
```

✅ **Verificação**: Seu código deve estar em `https://github.com/seu-usuario/calculadora`

---

## PASSO 2: Criar Conta PythonAnywhere (2 minutos)

1. Acesse: https://www.pythonanywhere.com
2. Clique em **"Start running Python online"**
3. Clique em **"Free account"**
4. Preencha:
   - Email
   - Username (lembre deste! será usado depois)
   - Senha
5. Clique **"Create a free account"**
6. Confirme seu email
7. Faça login

✅ **Você agora tem**: Username PythonAnywhere (ex: seu-username)

---

## PASSO 3: Abrir Bash Console no PythonAnywhere (1 minuto)

1. No Dashboard do PythonAnywhere
2. Procure por **"Consoles"** ou **"Bash"**
3. Clique em **"Open Bash console"** (ou "New console")

Agora você tem um terminal Linux na nuvem! 🎉

---

## PASSO 4: Clonar Seu Repositório (2 minutos)

No bash console:

```bash
# Copiar seu repositório
git clone https://github.com/seu-usuario/calculadora.git
cd calculadora
```

✅ **Verificação**: `ls` deve mostrar os arquivos do seu projeto

---

## PASSO 5: Criar Ambiente Virtual (1 minuto)

```bash
# ⚠️ NOTA: Se encontrar erro com Python 3.11, use Python 3.10 (mais estável no PythonAnywhere)
# Criar venv (isso também ativa)
mkvirtualenv --python=/usr/bin/python3.10 calculadora

# Pronto! Você verá: (calculadora) ...
```

✅ **Verificação**: Prompt deve mostrar `(calculadora)` no início

⚠️ **Se falhar**, tente descobrir versões disponíveis:
```bash
ls /usr/bin/python*
```
E use a versão que aparecer (3.9, 3.10 ou 3.12)

---

## PASSO 6: Instalar Dependências (2 minutos)

```bash
# Já deve estar ativado, mas certifique-se
workon calculadora

# Instalar
pip install -r requirements.txt
```

✅ **Verificação**: Espere terminar (pode demorar 1-2 minutos)

---

## PASSO 7: Fazer Migrações (1 minuto)

```bash
# Migrar banco de dados
python manage.py migrate

# Você verá: "... Running migrations: ... OK"
```

✅ **Verificação**: Sem erros?

---

## PASSO 8: Coletar Arquivos Estáticos (1 minuto)

```bash
# Coletar CSS, JavaScript, etc.
python manage.py collectstatic --noinput

# Você verá: "... static files collected ... OK"
```

✅ **Verificação**: Sem erros?

---

## PASSO 9: Criar Superuser (Admin) (1 minuto)

```bash
# Criar usuário admin
python manage.py createsuperuser

# Responda as perguntas:
# Username: admin (ou seu nome)
# Email: seu-email@exemplo.com
# Password: (digitar e confirmar)
```

✅ **Verificação**: Criado com sucesso?

---

## PASSO 10: Configurar settings.py (2 minutos)

Editar arquivo de configuração para adicionar seu domínio:

```bash
# Editar arquivo
nano config/settings.py
```

Procure por `ALLOWED_HOSTS` e altere para:

```python
ALLOWED_HOSTS = ['seu-username.pythonanywhere.com', 'localhost']
```

⚠️ **IMPORTANTE**: Substitua `seu-username` pelo seu username do PythonAnywhere!

Salve: `Ctrl+X` → `Y` → `Enter`

✅ **Verificação**: Arquivo salvo?

---

## PASSO 11: Retornar ao Dashboard (1 minuto)

1. Saia do bash (ou abra nova aba)
2. Vá para Dashboard PythonAnywhere
3. Clique em **"Web"** (ou "Web apps")

---

## PASSO 12: Criar Web App (2 minutos)

1. Clique **"Add a new web app"**
2. Escolha seu domínio: `seu-username.pythonanywhere.com`
3. Clique **"Next"**
4. Escolha **"Manual configuration"**
5. Escolha **"Python 3.11"**
6. Clique **"Next"**

✅ **Verificação**: Você deve ver a configuração da web app

---

## PASSO 13: Editar Arquivo WSGI (2 minutos)

1. Você deve estar na página de configuração da web app
2. Na seção **"Code"**, procure pelo **arquivo WSGI**
3. Clique no link (algo como `/var/www/seu_username_pythonanywhere_com_wsgi.py`)
4. **APAGUE TUDO** o conteúdo
5. **COLE ISTO**:

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

⚠️ **IMPORTANTE**: Substitua `seu-username` pelo seu username!

6. Salve: `Ctrl+S`

✅ **Verificação**: Arquivo salvo?

---

## PASSO 14: Configurar Arquivos Estáticos (1 minuto)

1. Volte para a página de configuração da web app
2. Procure por seção **"Static files:"**
3. Clique **"Add a new static files mapping"**
4. Preencha:
   - **URL**: `/static/`
   - **Directory**: `/home/seu-username/calculadora/staticfiles/`

⚠️ **IMPORTANTE**: Substitua `seu-username`!

5. Clique salvar

✅ **Verificação**: Mapeamento adicionado?

---

## PASSO 15: Recarregar Web App (1 minuto)

1. Volte para **Web** (se não estiver)
2. Procure pelo botão verde **"Reload seu-username.pythonanywhere.com"**
3. Clique **"Reload"**
4. Aguarde ~10 segundos

✅ **Verificação**: Botão ficou cinza? Se sim, está recarregando.

---

## PASSO 16: Acessar Sua App! 🎉 (1 minuto)

Abra seu navegador e vá para:

### App Principal:
```
https://seu-username.pythonanywhere.com/
```

### Admin:
```
https://seu-username.pythonanywhere.com/admin/
```

Faça login com o superuser que criou no PASSO 9!

✅ **Verificação**: Funcionando? 🎉

---

## 🎊 Parabéns!

Sua aplicação Django agora está **ONLINE** e acessível externamente!

---

## 📝 Resumo do que você fez:

1. ✅ Colocou código no GitHub
2. ✅ Criou conta PythonAnywhere
3. ✅ Clonou repositório
4. ✅ Instalou dependências
5. ✅ Fez migrações
6. ✅ Configurou web app
7. ✅ Editou arquivo WSGI
8. ✅ Mapeou arquivos estáticos
9. ✅ Recarregou
10. ✅ Acessou app online!

---

## 🔄 Próximas Vezes que Quiser Atualizar

```bash
# No bash PythonAnywhere
cd calculadora
git pull origin main
workon calculadora
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Depois, no Dashboard: Clique em Reload
```

---

## 🆘 Algo Deu Errado?

### "502 Bad Gateway"
- Vá para Dashboard → **Web** → **Log files**
- Leia **Error log** e procure pela mensagem de erro
- Causas comuns:
  - WSGI file mal editado
  - settings.py com erro
  - Virtualenv incorreto

### "CSS/JS não carregam"
```bash
# No bash:
python manage.py collectstatic --noinput

# Depois reload no Dashboard
```

### "Admin não funciona"
- Verifique ALLOWED_HOSTS em settings.py
- Deve incluir seu domínio PythonAnywhere

### Precisa de ajuda?
- Leia: [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) (guia completo)
- Leia: [TROUBLESHOOTING.md](TROUBLESHOOTING.md) (problemas comuns)

---

## 🎯 Próximos Passos

- ✅ Teste sua app funcionando
- ✅ Compartilhe URL com amigos: `https://seu-username.pythonanywhere.com`
- ✅ (Opcional) Compre domínio personalizado
- ✅ (Opcional) Upgrade para plano pago (se quiser PostgreSQL)

---

## 🌟 Você agora tem:

- ✅ App Django online
- ✅ Acessível externamente
- ✅ Com HTTPS automático
- ✅ Database persistente (SQLite)
- ✅ Admin funcional

**Bem-vindo ao mundo da hospedagem em produção!** 🚀

---

**Dúvidas?** Consulte a documentação:
- [PYTHONANYWHERE_GUIDE.md](PYTHONANYWHERE_GUIDE.md) - Guia completo
- [INDEX.md](INDEX.md) - Central de docs
- [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Problemas comuns
