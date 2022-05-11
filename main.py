nome = input('Qual é o seu nome? ')
idade = input('Olá, ' + nome + '! Qual a sua idade? ')
peso = float(input('Digite o seu peso: '))
h = float(input('Me informe a sua altura em metros: '))
imc = (peso / (h * h))

print(nome, 'tem', idade, 'anos', 'e pesa', peso, 'kg. Seu IMC é {}'.format(imc))
