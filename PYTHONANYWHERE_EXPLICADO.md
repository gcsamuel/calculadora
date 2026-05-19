# 🐍 PythonAnywhere - Explicação Simples

## O que é PythonAnywhere?

É um serviço online que **hospeda aplicações Django** na nuvem.

### Analogia:
- Seu computador = Hotel (hospedaria a app)
- PythonAnywhere = Airbnb (aluga servidor já pronto)

**Vantagem**: Seu computador pode ficar desligado, app continua online!

---

## O que Você Precisa Fazer?

### 1️⃣ Colocar Código no GitHub (Nuvem)
```bash
git add .
git commit -m "Mensagem"
git push origin main
```

**Por quê?** Para acessar seu código no PythonAnywhere

### 2️⃣ Criar Conta no PythonAnywhere
- Site: https://pythonanywhere.com
- Cria user + senha
- Recebe domínio grátis: `seu-usuario.pythonanywhere.com`

### 3️⃣ Clonar Código no Servidor
```bash
git clone seu-repo
```

Agora seu código está no servidor PythonAnywhere!

### 4️⃣ Instalar Dependências
```bash
pip install -r requirements.txt
```

Django, bibliotecas, tudo instalado no servidor!

### 5️⃣ Configurar Web App
No dashboard → Web → Configurar WSGI (arquivo especial)

**WSGI** = "Como executar Django no servidor"

### 6️⃣ Recarregar
Clique em Reload

**Pronto!** App está ONLINE! 🎉

---

## Arquitetura Simplificada

```
SEU COMPUTADOR                      PYTHONANYWHERE
===============                     ===============
calculadora/                        Servidor Linux
├─ views.py                         ├─ calculadora/
├─ templates/                       ├─ venv/
├─ static/                          ├─ Nginx/Gunicorn
└─ .git/                            └─ PostgreSQL/SQLite
      ↓                                    ↑
   git push                           git pull
```

---

## O Que Muda Para Você?

| Local | Produção |
|-------|----------|
| `python manage.py runserver` | Gunicorn (automático) |
| `localhost:8000` | `seu-usuario.pythonanywhere.com` |
| Seu computador | Servidor Linux |
| Pode desligar PC | App continua online 24/7 |
| SQLite local | SQLite online (free) |

---

## Os 3 Arquivos Importantes

### 1. `settings.py`
```python
ALLOWED_HOSTS = ['seu-usuario.pythonanywhere.com']
```
"Permite conexões deste domínio"

### 2. `WSGI file` (editado no dashboard)
```python
# Diz ao servidor: execute a app Django!
application = get_wsgi_application()
```

### 3. `requirements.txt`
```
Django==5.2.14
gunicorn==23.0.0
...
```
"Instale essas bibliotecas"

---

## O que Você NÃO Precisa Mais Fazer

❌ Manter computador ligado 24/7
❌ Instalar Docker
❌ Gerenciar servidor (PythonAnywhere faz!)
❌ Preocupar com SSL (automático!)

---

## O que PythonAnywhere Faz Por Você

✅ Servidor rodando 24/7
✅ HTTPS automático (seguro)
✅ Backups
✅ Gerenciamento de arquivos
✅ Console para debug
✅ Logs para ver problemas

---

## Exemplo de Acesso

### Antes (Seu PC):
```
http://192.168.0.10:8000/  (só na rede local)
```

### Depois (PythonAnywhere):
```
https://seu-usuario.pythonanywhere.com/  (acesso global!)
```

---

## Preços

### Free Tier (Recomendado para Começar)
- ✅ App online
- ✅ SQLite database
- ✅ 512 MB storage
- ❌ Sem PostgreSQL
- ❌ CPU limitada
- **Custo**: R$0

### Paid (Se Precisar Escalar)
- ✅ PostgreSQL database
- ✅ Mais storage (10GB+)
- ✅ Mais CPU
- ✅ Email support
- **Custo**: ~R$25/mês (USD $5)

---

## Fluxo Tipo

```
1. Desenvolvimento local com Django ✅
   ↓
2. Commitar no GitHub ✅
   ↓
3. Criar conta PythonAnywhere (5 min)
   ↓
4. Clonar repo no servidor (2 min)
   ↓
5. Instalar dependências (2 min)
   ↓
6. Configurar WSGI (2 min)
   ↓
7. Recarregar web app (30 seg)
   ↓
🎉 APP ONLINE! 🎉
```

**Tempo total**: ~10-15 minutos

---

## Dashboard PythonAnywhere

### Menu Principal:
- **Web** - Configurar app
- **Consoles** - Terminal bash
- **Databases** - Banco de dados
- **Files** - Ver/editar arquivos
- **Tasks** - Tarefas agendadas
- **Scheduled tasks** - Automação

### Básico que Você Usa:
- **Web** - Configurar e recarregar
- **Consoles** - Executar comandos
- **Files** - Ver logs

---

## Atualizações Depois

```
LOCAL:
1. git push origin main

NO PYTHONANYWHERE:
1. git pull origin main
2. python manage.py migrate
3. python manage.py collectstatic
4. Reload no dashboard
```

**Tempo**: ~1 minuto

---

## Vantagens PythonAnywhere

### vs Heroku:
- 🟢 Mais simples
- 🟢 Free tier funciona
- 🟢 Sem Docker
- 🟢 Mais barato
- 🔴 Menos escalável

### vs Seu Computador:
- 🟢 24/7 online
- 🟢 HTTPS automático
- 🟢 Domínio profissional
- 🟢 Backups
- 🔴 Menos controle total

---

## TL;DR (Muito Longo; Não Leu)

**PythonAnywhere = Servidor Django na nuvem, super fácil**

**Como funciona:**
1. Você escreve código (local)
2. Commita no GitHub
3. PythonAnywhere puxa o código
4. PythonAnywhere roda a app
5. Acessa online: `seu-usuario.pythonanywhere.com`

**Tempo**: 10 minutos

**Custo**: Grátis (ou $5/mês se quiser melhor)

**Próximo passo**: [PYTHONANYWHERE_PASSO_A_PASSO.md](PYTHONANYWHERE_PASSO_A_PASSO.md)

---

## Dúvidas Comuns

**P: Posso desligar meu computador?**
A: SIM! App fica online mesmo desligado!

**P: Quanto tempo minha app fica online?**
A: 24/7, sempre online (se pagar, garantido; se free, pode cair ocasionalmente)

**P: Como atualizar o código depois?**
A: `git push` → `git pull` no PythonAnywhere → Reload

**P: Como faço backup?**
A: Você tem no GitHub + no PythonAnywhere. Seguro!

**P: Preciso saber Linux?**
A: Não! Você só usa bash para Git e pip. Tudo pronto!

---

**Pronto? Vamos lá!** 👉 [PYTHONANYWHERE_PASSO_A_PASSO.md](PYTHONANYWHERE_PASSO_A_PASSO.md)
