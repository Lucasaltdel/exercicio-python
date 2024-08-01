
for x in range(0,1000):
    cont=0
    for i in range(1,x+1):
      if x%i==0:
        cont=cont+1
    if cont==2:
      print(x, "Primo")
