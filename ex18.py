### 18\. Maior e menor número


numeros = [10, 5, 23, 8, 42, 17, 3]


def maior(numeros):
    maior = numeros[0]
    for numero in numeros:
        if numero > maior:
            maior = numero
    return maior

def menor(numeros):
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor
    
def soma(numeros):
    soma = 0
    for numero in numeros:
        soma+= numero
    return soma
    
def media(numeros):
    quantidade = len(numeros)
    return soma(numeros)/quantidade
        
print(f"maior = {maior(numeros)}\n")
print(f"menor = {menor(numeros)}\n")
print(f"soma = {soma(numeros)}\n")
print(f"media = {media(numeros):.2f}\n")
