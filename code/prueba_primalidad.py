def es_primo(numero):
    contador = 0

    if numero <= 1:
        return False

    for i in range(1, numero + 1):
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            contador += 1
            break
    if contador == 0:
        return True
    else:
        return False
        

def run():
    numero = int(input("Escribe un número:  "))
    if es_primo(numero):
        print(str(numero) + " Es primo")
    else:
        print(str(numero) + " No es primo")
      

if  __name__  == "__main__":
    run()