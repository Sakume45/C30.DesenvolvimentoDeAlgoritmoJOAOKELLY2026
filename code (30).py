# Criar uma função de Calculadora, na qual o usuário digite dois valores e escolha qual opção ele quer realizar o cálculo (soma, subtração, multiplicação, divisão) e não esqueça de adicionar uma opção de sair.
print("\n --- Calculadora ---")
print("1. Soma (+)")
print("2. Subtrair (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

opcao = input("O que deseja fazer?")

if opcao in ('1', '2', '3', '4'):
    try:
        num1 = float(input("Digite um valor: "))
        num2 = float(input("Digite um valor: "))
    
    if opcao == '1':
        print(f"Resultado: {num1} + {num2}")
    elif opcao == '2':
        print(f"Resultado: {num1} - {num2}")
    elif opcao == '3':
        print(f"Resultado: {num1} * {num2}")
    elif opcao == '4':
        print(f"Resultado: {num1} / {num2}")
    else:
        print("Opção inválida.")

if opcao == '5':
    print("Encerrando programa...")
    break

calculadora()