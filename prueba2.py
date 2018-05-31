import sqlite3, csv

connection = sqlite3.connect('musica.db')

cursor = connection.cursor()

cursor.execute("DROP TABLE genres")
cursor.execute("CREATE TABLE genres(id INTEGER, Artist TEXT, Genre TEXT)")

with open('genres.csv', newline='', encoding='utf-8') as csvfile:
    datareader = csv.reader(csvfile, delimiter='\t', quotechar='|')
    
    i=0
    for row in datareader:
        row = row[0].split(",")
        aux = (i, row[0], row[1])
        
        cursor.execute("INSERT INTO genres VALUES(?,?,?)", aux)
        i += 1

            
#Eliminaremos la primera fila (encabezados)
primera_fila=(0,)            
cursor.execute('DELETE FROM genres WHERE id=?', primera_fila)

#cursor.execute('SELECT * FROM genres')  #Lo comenté porque no quiero ver el output, de momento
#cursor.fetchall()

connection.commit()
connection.close()
