#Um termômetro em uma cidade registrou a temperatura de 32°F (Fahrenheit).
# Crie um programa que converta essa temperatura para Celsius usando a fórmula: C = (F - 32) × 5/9. Imprima o resultado com uma mensagem clara.
start = int(input("Começar? Y/N ")).upper().strip()
if start == "Y":
    Celsius = (F - 32) * 5 / 9
    print(f"Temperatura em Celsius: ", {Celsius})
elif start == "N":
    print("Program terminated.")
else:
    print("Invalid input")