cap=float(input("insira o valor desejado:"))
temp=int(input("em quanto tempo deseja? tempos 2, 6 ,12 e 24 meses"))
while cap>0:
    if temp==2:
        i=6.9
        j=(cap*i*temp)
        print(j)
        i=7.14        
        j=(cap*i*temp)
        print(j)
    elif temp==12:
        i=9.23
        j=(cap*i*temp)
        print(j)
    elif temp==24:
        i=12.46
        j=(cap*i*temp)
        print(j)
    else:
        print("opção errada")
    break
