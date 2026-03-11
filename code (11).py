salarioBase = float(input("Insira seu salário base: "))
salarioBonus = float(input("Insira algum bônus (se tiver algum): "))
taxas = float(input("Insira suas taxas: "))
salarioLiquido = salarioBonus - taxas
salarioBruto = salarioBase + salarioLiquido
print("Salário total: ", salarioBruto)