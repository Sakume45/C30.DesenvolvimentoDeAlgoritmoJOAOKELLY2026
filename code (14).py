# Um vendedor começa o mês com 100 unidades em estoque. Durante o mês, ele:
# Recebe 50 unidades
# Vende 30 unidades
# Devolve 5 unidades
# Crie um programa que utilize operadores de atribuição (+=, -=) para atualizar o estoque e imprima o resultado após cada operação.
unidades = {
    "começo": 100
}

unidades["extra"] = int(input("Adicione o extra: "))
unidades["vendidas"] = int(input("Unidades vendidas: "))
unidades["devolvidas"] = int(input("Unidades devolvidas: "))
totalDim = unidades["vendidas"] - unidades["devolvidas"]
total = começo + unidades["extra"] - totalDim