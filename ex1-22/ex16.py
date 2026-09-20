### 16\. Calculadora de média

def calc_media(notas):
    soma = 0
    i = 0
    for nota in notas:
        soma+= nota
        i+=1
    return  soma/i
        
entrada = input("Digite as notas separas por virgula: ")
notas = [int(item.strip()) for item in entrada.split(",")]

print(calc_media(notas))

