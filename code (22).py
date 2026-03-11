total = 0
quantidade = 0

while True:
    deposito = float(input("Digite o valor do depósito (ou 0 para encerrar): "))
    if deposito == 0:
        break
    total += deposito
    quantidade += 1

print(f"Total depositado: R$ {total:.2f}")
print(f"Quantidade de transações: {quantidade}")