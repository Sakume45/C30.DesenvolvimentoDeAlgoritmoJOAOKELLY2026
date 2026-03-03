numero = int(input("Digite qualquer número inteiro. "))
if numero <= 0:
    print("Tem que ser um número positivo doido")

quadrado = numero * numero
cubo = numero ** 3
if numero % 2 == 0:
    print(f"O quadrado de {numero} é igual a {quadrado:.f}")
    else:
    print(f"O cubo de {numero} é igual {cubo.f}")