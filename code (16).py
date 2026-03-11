idade = int(input("Digite a idade do atleta: "))

if idade < 12:
    categoria = "Infantil"
elif idade < 18:
    categoria = "Juvenil"
elif idade < 60:
    categoria = "Adulto"
else:
    categoria = "Sênior"

print(f"Categoria: {categoria}")
print(f"Bem-vindo à competição de natação!")