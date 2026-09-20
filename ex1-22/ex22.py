### 22\. Sistema de notas

alunos = {
    "João": [8, 7, 9],
    "Maria": [10, 9, 8],
    "Pedro": [5, 6, 4]
}

def media_alunos(alunos):
    for chave, valor in alunos.items():
        soma = sum(valor)
        media = soma / len(valor)
        if media >= 6:
            print(f" A média de {chave} é {media:.2f} e sua situação é Aprovada!")
        else:
            print(f" A média de {chave} é {media:.2f} e sua situação é Reprovada!")


media_alunos(alunos)