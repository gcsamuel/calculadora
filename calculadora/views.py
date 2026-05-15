from django.shortcuts import render


def home(request):
    resultado = None
    erro = None
    numero1 = ''
    numero2 = ''
    operacao = 'soma'

    if request.method == 'POST':
        numero1 = request.POST.get('numero1', '').strip()
        numero2 = request.POST.get('numero2', '').strip()
        operacao = request.POST.get('operacao', 'soma')

        try:
            value1 = float(numero1)
            value2 = float(numero2)

            if operacao == 'soma':
                resultado = value1 + value2
            elif operacao == 'subtracao':
                resultado = value1 - value2
            elif operacao == 'multiplicacao':
                resultado = value1 * value2
            elif operacao == 'divisao':
                if value2 == 0:
                    erro = 'Não é possível dividir por zero.'
                else:
                    resultado = value1 / value2
            else:
                erro = 'Operação inválida.'
        except ValueError:
            erro = 'Por favor, digite dois números válidos.'

    context = {
        'resultado': resultado,
        'erro': erro,
        'numero1': numero1,
        'numero2': numero2,
        'operacao': operacao,
    }
    return render(request, 'calculadora/home.html', context)
