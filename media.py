notaA = float(input("Informe a primeira nota: "))
notaB = float(input("Informe a segunda nota: "))

mediaFinal = (notaA + notaB) / 2

if (mediaFinal >= 7.0):
    print("Aprovado!!!")
elif(mediaFinal >=5):
    print("Recuperação...")
else: 
    print("Reprovado!!!")