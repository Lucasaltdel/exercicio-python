soma = 0
num = int(input("Digite um número: "))
for x in range(0,num+1):
    if x % 2 != 0:
        soma = soma + x
        if soma == num:
            print(num, "é um quadrado perfeito")
