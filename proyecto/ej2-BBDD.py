import sqlite3

miConexion = sqlite3.connect("GestionProductos.db")

miCursor = miConexion.cursor()

'''
SELECT * 
UPDATE PRODUCTOS SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'

DELETE FROM PRODUCTOS WHERE ID = 5
'''

miCursor.execute('''
CREATE TABLE PRODUCTOS(
ID INTEGER PRIMARY KEY AUTOINCREMENT,
NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
PRECIO INTEGER,
SECCION VARCHAR(50))
''')

variosProductos = [
    ("Camisa", 10, "Ropa"),
    ("Vaso de Vidrio", 3, "Cerámica"),
    ("Camión", 89, "Juguetería")
]

miCursor.executemany("INSERT INTO productos VALUES (NULL,?,?,?)", variosProductos)

miConexion.commit()

miConexion.close()