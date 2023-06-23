import sqlite3

conn = sqlite3.connect("DBEjemplo.db")
c = conn.cursor()

c.execute(
    """
    CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL )
    """
)

# como insertar datos en la base de datos.
c.execute('INSERT INTO usuarios VALUES (NULL, "Hernan", "Acosta")')
c.execute('INSERT INTO usuarios VALUES (NULL, "Fernando", "Alvarez")')
conn.commit()

# como actualizar datos en la base de datos.
c.execute("UPDATE usuarios SET nombre = 'Juan' WHERE id = 1")
conn.commit()

# como eliminar datos en la base de datos.
c.execute("DELETE FROM usuarios WHERE id = 6")
conn.commit()

# como buscar datos en la base de datos.
c.execute("SELECT * FROM usuarios")
print(c.fetchall())

conn.close()
