# Atv 1 (19/03/26)
def ranqueFinal(pontos, derrotas):
    pontosFinal = pontos - (derrotas * 10)
    
if pontosFinal < 0:
    return "Account terminated."
    
if pontosFinal < 100:
    return "Bronze rank"
elif pontosFinal < 300:
    return "Silver rank"
elif pontosFinal < 600:
    return "Gold rank"
else:
    return "Diamond rank"