saldo = float(input("Informe seu saldo: "))
saque = float(input("Quanto deseja sacar: "))

if saque <= 0:
    print("Valor digitado é inválido")
elif saque > saldo:
    print("Saldo insuficiente")
else:
    saldo = saldo - saque
    print(
        f"Saque realizado com sucesso! "
        f"Foi retirado o valor de R${saque:.2f}. "
        f"O saldo atual é R${saldo:.2f}"
    )