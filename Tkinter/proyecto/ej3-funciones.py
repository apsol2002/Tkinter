import sqlite3

def dbListalProductos():
    miConexion = sqlite3.connect("GestionProductos.db")
    miCursor = miConexion.cursor()



    miConexion.commit()
    miConexion.close()