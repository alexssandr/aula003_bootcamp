### Exercício 1: Verificação de Qualidade de Dados

# try:
#     quantidade = int(input('Digite a quantidade:\n'))
#     preco = float(input('Digite o preco:\n'))
#     if quantidade > 0 and preco > 0:
#         print('Dados validos')
#     else:
#         print('Dados invalidos')
# except:
#     print('erro de input')

### Exercício 2: Classificação de Dados de Sensor
# try:
#     temperatura = float(input('Digite a temperatura:\n'))
#     if temperatura < 18:
#         print('Baixa')
#     elif temperatura < 27:
#         print('Normal')
#     else:
#         print('Alta')
# except:
#     print('erro de input')

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}

# if log['level'] == 'ERROR':
#     print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# import re


# def is_valid_email(email):

#     """Check if the email is a valid format."""

#     # Regular expression for validating an Email

#     regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$'

#     # If the string matches the regex, it is a valid email

#     if re.match(regex, email):

#         return True

#     else:

#         return False

# try:
#     idade = int(input('Digite a idade:\n'))
#     email = input('Digite o e-mail:\n')
    
#     if not idade >= 18 and idade <= 65:
#         print('Idade não permitida')
#     elif not is_valid_email(email):
#         print('Email invalido')
#     else:
#         print('Dados Valido')
# except:
#     print('erro de input')

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# transacao = {'valor': 5000, 'hora': 20}

# if transacao['valor'] > 10000 or (transacao['hora'] < 9 or transacao['hora'] > 18):
#     print('Fraude')
# else:
#     print("ok")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# texto = 'Se você pode sonhar, pode realizar'

# texto_formatado = texto.replace(',', '').lower()
# texto_lista = texto_formatado.split()

# palavras = {}

# for palavra in texto_lista:
#     if palavra in palavras:
#         palavras[palavra] += 1
#     else:
#         palavras[palavra] = 1

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# for user in usuarios:
#     if user['email'] == '':
#         print(user)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

palavra_chave = 'ok'

while palavra_chave != 'sair':
    palavra_chave = input('Digite a palavra-chave:\n')