import time
azul=1
vermelho=2
amarelo=3
preto=4
cinza=5
roxo=6
print("corte o fio correto")
time.sleep(4)
print("azul, vermelho, amarelo,preto,cinza,roxo")
fio_correto = 'vermelho'
fio = str(input("Digite a cor do fio para cortar: "))

print("cortando o fio")
time.sleep(2)
print("quase lá...")
time.sleep(2)
if fio==fio_correto:
    print("----------------------------------------")
    print("missão completa fio cortado com sucesso")
    print("----------------------------------------")
else:
    print("KABOOM")