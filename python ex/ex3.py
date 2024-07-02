soma=0
print("Radar")

velocidade=int(input("digite sua velocidade "))
while True:
    if velocidade>80:
        soma=soma+velocidade
        calc=soma+10
        print("multado, valor da multa",calc)
        break
    if velocidade<=80:
        print("não está multado")    
        break
