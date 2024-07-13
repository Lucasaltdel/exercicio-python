indiceP=float(input("qual o indice de poluição: "))
if indiceP==0.5:
    print("todos os grupos 1º, 2º e 3º devem ser notificados a paralisarem suas atividades.")
if indiceP==0.4:
    print("1º e 2º grupo são intimadas a suspenderem suas atividades")
if indiceP>=0.3:
    print("1º grupo são intimadas a suspenderem suas atividades")
else:
    print("Ok está aceitavel o indice")
