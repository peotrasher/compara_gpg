def ingreso_de_strings() -> list:
    """
    No recibe valores, retorna 2 listas, una con la/las strings con que 
    comparar, otra con la/las strings a comparar con.
    ¡Se omitira aquellas strings que se comparará con y sean identicas!
    """
    strings_con_que_comparar = []
    strings_a_comparar_con = []
    while True:
        try:
            rango_strings_0 = int(input("Número de str. con que comparar\n> "))
            rango_strings_1 = int(input("Número de str. a comparar con\n> "))
            break
        except:
            print("Ocurrio un error! Ingrese datos nuevamente.")
    for i in range(rango_strings_0):
        string = input(f"Compare con ({i + 1}): ")
        if (no_existencia_en_lista(string, 
                                    strings_con_que_comparar, True)):
            strings_con_que_comparar.append(string)
        
    for i in range(rango_strings_1):
        string = input(f"A comparar ({i + 1}): ")
        if (no_existencia_en_lista(string, 
                                    strings_a_comparar_con, False)):
            strings_a_comparar_con.append(string)
    return strings_con_que_comparar, strings_a_comparar_con


def no_existencia_en_lista(string: str, lista: list, 
                            formatear: bool) -> bool:
    """
    Recibe una string, una lista y un valor booleano correspondiente a
    si se quiere o no formatear la string y lista, retorna valor 
    booleano que dice si es que es un elemento que no existia (True) o 
    ya existia (False) en la lista que se ingreso.
    """
    for elemento in lista:
        if formatear:
            if (formatea_string(string)
                    == formatea_string(elemento)):
                print(
                f"""
                | {string} | será omitido, ya existia.
                (input) | {string} | == (existente) | {elemento} |
                """
                )
                return False
        else:
            if (string 
                    == elemento):
                print(
                f"""
                | {string} | será omitido, ya existia.
                (input) | {string} | == (existente) | {elemento} |
                """
                )
                return False
    return True


def formatea_string(string0: str) -> str:
    """Recibe una string, retorna esta con todo whitespace removido."""
    string0_alt = string0.replace(' ','')
    return string0_alt


def formatear_strings(lista0: list, lista1: list) -> list:
    """
    Recibe dos listas de strings, retorna las dos listas sin NINGUN
    whitespace en NINGUNO de sus elementos.
    """
    for i in range(len(lista0)):
        lista0[i] = lista0[i].replace(' ', '')
    for i in range(len(lista1)):
        lista1[i] = lista1[i].replace(' ', '')
    return lista0, lista1


def comparar_string(lista0: list, lista1: list) -> None:
    """
    Recibe dos listas de strings, retorno vacio pero se imprime un 
    diccionario con la/las string con que comparar como llave y la/las 
    strings a comparar como valor siendo estas las coincidencias, osea 
    si son iguales.
    """
    lista0_alt, lista1_alt = formatear_strings(lista0.copy(), lista1.copy())
    diccionario = {}
    for i in range(len(lista0)):
        coincidencias = []
        no_coincidentes = []
        for j in range(len(lista1)):
            if (lista0_alt[i] 
                    == lista1_alt[j]):
                coincidencias.append(lista1[j])
            else:
                no_coincidentes.append(lista1[j])
        diccionario[f"✅ Coincide con | {lista0[i]} |"] = coincidencias
        diccionario[f"❎ | {lista0[i]} | no coincide con"] = no_coincidentes
    for llave in diccionario:
        print(f"{llave}")
        for valor in diccionario[llave]:
            print(f"-> {valor}")       


def main():
    strings_con_que_comparar, strings_a_comparar_con = ingreso_de_strings()
    comparar_string(strings_con_que_comparar, strings_a_comparar_con)


if __name__ == "__main__":
    main()
