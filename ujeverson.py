#script para input dos valores e operação, e verificar o zero para a divisão
print("Selecione a operação:")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

escolha = input("Digite a sua escolha (1/2/3/4):")

num1 = int(input("Digite o primeiro número:"))
num2 = int(input("Digite o segundo número:"))

if escolha == '1':
    resultado = num1 + num2
    print(num1, "+", num2, "=", resultado)
    
elif escolha == '2':
    resultado = num1 - num2
    print(num1, "-", num2, "=", resultado)
    
elif escolha == '3':
    resultado = num1 * num2
    print(num1, "*", num2, "=", resultado)
    
elif escolha == '4':
    resultado = num1 / num2
    print(num1, "/", num2, "=", resultado)
    if num2 == 0:
        print("Não é possível dividir por zero")
    else:
        print(num1, "/", num2, "=", resultado)
    
else:
    print("Opção inválida") 
    