### 23\. Escrever em arquivo
from pathlib import Path
"""Foi utilizado essa biblioteca apenas para garantir
    que ambos os arquivos ficassem na mesma pasta."""

mensagem = input("Digite uma mensagem: ")

caminho = Path(__file__).parent / "mensagem.txt"

with open(caminho, "w") as arquivo:
    arquivo.write(mensagem)
    print(f"Mensagem salva em {caminho}")

#Solução sem utilizar a biblioteca pathlib
"""
mensagem = input("Digite uma mensagem: ")
with open("mensagem.txt", "w") as arquivo:
    arquivo.write(mensagem) 
    print("Mensagem salva em mensagem.txt")
"""