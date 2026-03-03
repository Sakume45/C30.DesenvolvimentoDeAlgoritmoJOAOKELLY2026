login1 = bunda
senha1 = 1234
login2 = bunda2
senha2 = 5678

usuarioLogOn = input("Por favor, digite seu usuário. ")
usuarioLogOn2 = int(input("Agora, sua senha, por favor "))

if usuarioLogOn != login1:
    print("Usuário incorreto")
    elif usuarioLogOn != login2:
        print("Usuário incorreto")
    elif usuarioLogOn2 != senha:
        print("Senha incorreta")
    elif usuarioLogOn2 != senha2:
        print("Senha incorreta")
    else:
        print("Bem-vindo.")