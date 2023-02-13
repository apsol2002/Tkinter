import sqlite3

def buscarElementoEnLista(lista, valor):
    t = ''
    for tupla in lista:
        for elemento in tupla:
            if elemento == valor:
                t = tupla
    return t

def pedirProducto():
    nombre = input("Ingresa el NOMBRE del producto: -> ")
    precio = input("Ingresa el PRECIO del producto: -> ")
    seccion = input("Ingresa la SECCION del producto: -> ")
    return nombre, precio, seccion


def dbProcesarConsulta(consulta, tipo):
    resultado = ''
    miConexion = sqlite3.connect("GestionProductos.db")
    miCursor = miConexion.cursor()

    if tipo == "select":
        miCursor.execute(consulta)
        resultado = miCursor.fetchall()
    if tipo == "insert" or tipo == "delete" or tipo == "update":
        miCursor.execute(consulta)
        resultado = True

    miConexion.commit()
    miConexion.close()

    return resultado


def listalProductos():
    consulta = "SELECT * FROM PRODUCTOS"
    listaproductos = dbProcesarConsulta(consulta, tipo="select")
    print("----------------")
    for producto in listaproductos:
        print(f"{producto[0]} - {producto[1]} - {producto[2]}")
    print("----------------")
    return listaproductos


def agregarProducto():
    #     miCursor.execute("INSERT INTO productos VALUES ('Balon', 15, 'Deportes')")
    n, p, s = pedirProducto()
    consulta = "INSERT INTO productos VALUES (null,'{}', {}, '{}')".format(n, int(p), s)
    estado = dbProcesarConsulta(consulta, tipo="insert")
    return estado  # True en caso de  que se pudo hacer la consulta.


def eliminarProducto():
    id = int(input("Ingresa el ID del producto a eliminar - > "))
    consulta = f"DELETE FROM PRODUCTOS WHERE ID = {id}"
    estado = dbProcesarConsulta(consulta, tipo="delete")
    return estado  # True en caso de  que se pudo hacer la consulta.

def modificarProducto():

    productos = listalProductos()
    id = int(input("Ingresa el ID del producto a modificar - > "))

    global tupla
    tupla = buscarElementoEnLista(productos, id)
    while tupla[0] != id:
        print("Ese ID no es valido - reintentar.. ")
        id = int(input("Ingresa el ID del producto a modificar - > "))

        tupla = buscarElementoEnLista(productos, id)

    n, p, s = pedirProducto() # UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'

    if n == '':
        n = tupla[1]
    if p == '':
        p = tupla[2]
    else:
        p = int(p)
    if s == '':
        s = tupla[2]

    consulta = "UPDATE PRODUCTOS SET NOMBRE_ARTICULO='{}', PRECIO={}, SECCION='{}' WHERE ID={}".format(n, p, s, id)

    #print(consulta)

    estado = dbProcesarConsulta(consulta, tipo="update")

    return estado # True en caso de  que se pudo hacer la consulta.



menu = '''
    . : MENU : . 
1 - Listar elementos
2 - Agregar elementos
3 - Borrar elementos
4 - Modificar elementos
-----------------------
Trabajo con archivos (XD)
8 - none
9 - none
0 - Salir del programa.  
'''

while True:
    print(menu)
    op = input("Ingresa la opción - > ")

    if op == '0':
        print("Saliendo del programa ... ")
        break
    elif op == '1':
        listalProductos()
    elif op == '2':
        if agregarProducto():
            print("Se agregó el producto en la base de datos.")
    elif op == '3':
        if eliminarProducto():
            print("Se eliminó el producto de la base de datos")
    elif op == '4':
        if modificarProducto():
            print("Se modifico  el producto de la base de datos")
    else:
        print("Opcion no valida.")
