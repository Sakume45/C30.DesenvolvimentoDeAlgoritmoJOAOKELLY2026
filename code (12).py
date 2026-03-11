distancia = 450
consumo_km_l = 8
preco_litro = 5.50
litros_consumidos = distancia / consumo_km_l
custo_total = litros_consumidos * preco_litro

start = input("Iniciar programa? Y/N: ").upper().strip()

if start == "Y":
    print(f"Distância percorrida: {distancia} km")
    print(f"Consumo do carro: {consumo_km_l} km/l")
    print(f"Preço da gasolina: R$ {preco_litro:.2f}")
    print("-" * 30)
    print(f"Litros consumidos: {litros_consumidos:.2f} L")
    print(f"Custo total: R$ {custo_total:.2f}")
elif start == "N":
    print("Programa encerrado.")
else:
    print("Opção inválida.")