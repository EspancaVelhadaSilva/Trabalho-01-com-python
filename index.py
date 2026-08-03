# print("Olá, mundo!")

# nome = "Arthur"
 
 #idade = 15
 
# altura = 1,70
 
#print("Nome", nome)
#print("Idade", idade)
#print("Altura", altura)
 
#num1 = int(input("Digite o primeiro numero"))
#num2 = int(input("Digite o segundo numero"))
#soma = num1 + num2
#sub = num1 - num2
#multi = num1 * num2
#div = num1 / num2
 
#print("soma", Soma)
#print("sub", Sub)
#print("multi", Multi)
#print("div", Div)

#criar variavel salario e dividir esse salario por 30. Em seguida fazer uma condicional para saber se o salario é baixo ou alto
salario = int(input("Coloque quanto você ganha por mês: "))
dia = salario / 30

if salario >= 3000:
    print(f"Salário muito alto, recebendo {dia:.2f} por dia!")
elif salario >= 1000 and salario <= 2999:
    print(f"Salário na média, recebendo {dia:.2f} por dia.")
else:
    print(f"Salário muito baixo, recebendo {dia:.2f} por dia, o que dá menos que um salário mínimo!")
