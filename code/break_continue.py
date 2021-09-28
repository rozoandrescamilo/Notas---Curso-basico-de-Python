def run():
    # for contador in range(1000): #imprimir numeros pares hasta 1000
    #     if contador % 2  != 0: # termino para decir diferente "!="
    #         continue
    #     print(contador)
    
    # for i in range(10000): #imprimir hasta que llegue al 5678
    #     print(i)
    #     if i == 5678:
    #         break

    texto = input("Escribe un texto:  ") #imprimir hasta que encuentre letra "o"
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == "__main__":
    run()