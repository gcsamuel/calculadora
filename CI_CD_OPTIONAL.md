# 🔄 CI/CD Opcional - GitHub Actions

Este arquivo descreve como configurar **deploy automático** no Heroku usando GitHub Actions.

## ⚠️ Importante

- Este passo é **opcional**
- Você pode fazer deploy manualmente com `git push heroku main`
- GitHub Actions é útil se você quer deploy **automático** a cada push

---

## 🚀 Configurar CI/CD (5 minutos)

### 1. Gerar Heroku API Token

```bash
# Faça login no Heroku
heroku login

# Gere um token
heroku authorizations:create --description "GitHub Actions"

# Copie o token (será usado no passo 2)
```

### 2. Adicionar Secret ao GitHub

No seu repositório GitHub:

1. Vá para: **Settings → Secrets and variables → Actions**
2. Clique em: **New repository secret**
3. Nome: `HEROKU_API_KEY`
4. Valor: Cole o token gerado acima
5. Clique: **Add secret**

### 3. Criar arquivo de workflow

Na raiz do seu projeto, crie o arquivo `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Heroku

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Deploy to Heroku
        uses: akhileshns/heroku-deploy@v3.12.12
        with:
          heroku_api_key: ${{ secrets.HEROKU_API_KEY }}
          heroku_app_name: "seu-app-name"
          heroku_email: "seu-email@example.com"
          usedocker: true
```

### 4. Customizar valores

Substitua:
- `seu-app-name` pelo nome da sua app no Heroku
- `seu-email@example.com` pelo seu email do Heroku

### 5. Commit e Push

```bash
git add .github/workflows/deploy.yml
git commit -m "Add GitHub Actions CI/CD"
git push origin main
```

---

## ✅ Pronto!

Agora, cada vez que você fizer push para `main`:

1. GitHub Actions começará automaticamente
2. Build da imagem Docker
3. Deploy no Heroku
4. Migrações executadas automaticamente

### Ver status do deploy

No GitHub:
- Vá para: **Actions**
- Veja o status do build/deploy

---

## 🆘 Troubleshooting

### Erro: "Authentication failed"
- Verifique se o token foi copiado corretamente
- Verifique se o secret foi adicionado ao repositório

### Erro: "App not found"
- Verifique o nome da app (deve ser exatamente igual ao Heroku)
- Verifique a spelling

### Logs
- Clique no workflow em **Actions** → detalhes
- Veja os logs de erro completos

---

## 🔄 Alternativas (Sem CI/CD)

Se preferir **não** usar CI/CD, pode fazer deploy manualmente:

```bash
git push heroku main
```

---

## 📚 Referências

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Heroku Deploy Action](https://github.com/akhileshns/heroku-deploy)

---

## ✨ Resumo

- **Sem CI/CD**: `git push heroku main` (manual)
- **Com CI/CD**: `git push origin main` (automático)

Escolha baseado na sua preferência! 🚀
