# Calculadora Django

Projeto Django simples com uma calculadora que soma, subtrai, multiplica e divide.

## Como rodar localmente

1. Ative o ambiente virtual:

```bash
cd /home/devmobhis/calculadora
source .venv/bin/activate
```

2. Inicie o servidor Django:

```bash
python manage.py runserver 0.0.0.0:8000
```

3. Acesse a aplicação no navegador:

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

## Versionar no GitHub

1. Se ainda não tiver, crie um repositório no GitHub.
2. No terminal:

```bash
git add .
git commit -m "Adicionar calculadora Django e configuração"
```

3. Configure o `origin` caso ainda não tenha feito:

```bash
git remote add origin https://github.com/gcsamuel/calculadora.git
```

4. Envie para o GitHub:

```bash
git push -u origin master
```

5. Depois, para atualizar:

```bash
git add .
git commit -m "Atualização"
git push
```
# calculadora
