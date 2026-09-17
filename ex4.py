### 6\. Sistema de notas

media = 0
for i in range(3): 
    n = float(input(f"informe a {i+1}° nota:"))
    media+= n
media = media/3
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperção")
else:
    print("Reprovado")
