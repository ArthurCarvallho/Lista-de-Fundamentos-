 ### 11\. Senha
 
senha = input("crie uma senha:")
 
 
 
for i in range(3):
    c_senha = input("informe sua senha:")
    if senha == c_senha:
        print("Acesso permitido")
        break
    elif i == 2 and senha != c_senha:
        print("Acesso bloqueado")