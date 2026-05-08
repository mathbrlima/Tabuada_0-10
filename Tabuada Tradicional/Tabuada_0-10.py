tabuada = int(input("Digite um número para exibir na tabuada: "))
print(f"Tabuada do número {tabuada}")
for valor in range(1, 11, 1):
    print(f"{tabuada} x {valor} = {tabuada * valor}")

#while True:
    #tabuada = int(input("Digite um número para ver a tabuada: "))
    #print(f"\nTabuada do número {tabuada}")

    #for valor in range(1, 11):
        #print(f"{tabuada} x {valor} = {tabuada * valor}")

    #continuar = input("\nQuer ver outra tabuada? (s/n): ")
    #if continuar.lower() != 's':
        #break