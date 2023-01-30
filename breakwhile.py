# break em while
total = 0
while(True):
    v=float(input("Digite um valor(ou zero para encerrar): "))
    if v==0:
        break
    total += v
print ("Total Digitado:",total)