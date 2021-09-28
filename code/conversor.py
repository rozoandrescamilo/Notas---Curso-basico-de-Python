def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos " + tipo_pesos + " tienes?: ")
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


menu = """  
Bienvenido al conversor de monedas  👌💰📈

1 - Pesos colombianos 
2 - Pesos argetinos
3 - Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("colombiano", 3875)
elif opcion == 2:
    conversor("argetinos", 91.64)
elif opcion == 3:
    conversor("mexiacanos", 20.59)
else:
    print("Ingresa una opción correcta por favor")



