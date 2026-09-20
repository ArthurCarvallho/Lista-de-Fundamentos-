### 14\. Calculadora

def somar(a,b):
    return a+b

def subtrair(a,b):
    return a-b
def multiplicar(a,b):
    return a*b
def dividir(a,b):
    if b == 0:
        return "Impossivel dividir algo por 0."
    else:
        return a/b
       
num1 = int(input("Digite o primeiro número:"))
while True:
    operacao = int(input("informe a operação com 1 = Somar 2 = subtrair 3 = multiplicar = 4 dividir: "))
    if operacao in [1, 2, 3, 4]:
        break
    else: 
        print("informe uma operação valida!")
        
num2 = int(input("Digite o segundo número:"))

if operacao == 1:
    print(somar(num1,num2))
elif operacao == 2: 
    print(subtrair(num1,num2))
elif operacao == 3:
    print(multiplicar(num1,num2))
else: 
    print(dividir(num1,num2))
    
