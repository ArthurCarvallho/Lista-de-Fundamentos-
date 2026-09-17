def cadastro(email, nome, telefone, idade, admin=False):
    if email != "" and nome != "" and telefone != "" and idade != None:
        print("Dados recebidos com Sucesso")
    else:
        print("nao recebemos todos os dados necessarios")


cadastro("a","b","c",15,True)
cadastro("a","b","c",15)
cadastro("a","c","","",True)