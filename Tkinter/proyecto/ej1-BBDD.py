import sqlite3

miConexion = sqlite3.connect("PrimeraBase.db")

miCursor = miConexion.cursor()

# -- CREAR LA TABLA
# ---- se comenta porque ya fue ejecutada y creada..

# -- INSERTAR SOLO UN ELEMENTO POR VEZ
# miCursor.execute("CREATE TABLE productos ( nombre_articulo varchar(50), precio integer, seccion varchar(20) )")
# miConexion.commit()
'''
    miCursor.execute("INSERT INTO productos VALUES ('Balon', 15, 'Deportes')")
    miConexion.commit()
'''

# -- INSERTAR VARIOS ELEMENTOS A LA VEZ ..
'''
variosProductos = [
    ("Camisa", 10, "Ropa"),
    ("Vaso de Vidrio", 3, "Cerámica"),
    ("Camión", 89, "Juguetería")
]

miCursor.executemany("INSERT INTO productos VALUES (?,?,?)", variosProductos)

miConexion.commit()
'''

##### -- CARGAR ELEMENTOS DE LA BASE DE DATOS ..

miCursor.execute("SELECT * FROM PRODUCTOS")

variosProductos = miCursor.fetchall()

for tupla in variosProductos:
    #print(tupla)
    print(f"El bojeto {tupla[0]}  de la seccion {tupla[2]} cuesta {tupla[1]}")


miConexion.close()