def run():
    mi_diccionario = {
        'llave1' : 1,
        'llave2' : 2,
        'llave3' : 3,
    }

    # print(mi_diccionario['llave1']) #Se utiliza para imprimir cada llave con su valor
    # print(mi_diccionario['llave2'])
    # print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina' : 449388712,
        'Brasil' : 210147125,
        'Colombia' : 50372424
    }

    # print(poblacion_paises['Argentina']) # se utiliza para imprimir valro de Argentina

    # for pais in poblacion_paises.keys(): # imprimir nombre de las llaves
    #     print(pais)

    # for pais in poblacion_paises.values(): # imprimir valores de las llaves
    #     print(pais)

    for pais, poblacion in poblacion_paises.items(): # imprimir nombre y valor de las llaves de manera organizada
         print(pais + ' Tiene ' + str(poblacion) + ' habitantes')


if __name__ == "__main__":
    run()