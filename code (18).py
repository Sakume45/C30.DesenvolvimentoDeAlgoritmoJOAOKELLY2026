valor = float(input("Valor da compra: R$ "))

if valor < 100:
    perc = 0
elif valor < 500:
    perc = 0.05
elif valor < 1000:
    perc = 0.10
else:
    perc = 0.15

desconto = valor * perc
valor_final = valor - desconto

print(f"Valor Original: R$ {valor:.2f}")
print(f"Desconto: R$ {desconto:.2f} ({perc*100:.0f}%)")
print(f"Valor Final: R$ {valor_final:.2f}")
