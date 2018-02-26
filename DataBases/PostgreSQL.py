import psycopg2


def create_table():
    con = psycopg2.connect("dbname = 'DB1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER, name TEXT, value REAL)")
    con.commit()
    con.close()


def insert_values(id, name, value):
    con = psycopg2.connect("dbname = 'DB1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("INSERT INTO product VALUES(%s, %s, %s)",(id, name, value))
    con.commit()
    con.close()


def delete_values(id):
    con = psycopg2.connect("dbname = 'DB1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("DELETE FROM product WHERE id = %s",(id,))
    con.commit()
    con.close()


def update_values(name,value,id):
    con = psycopg2.connect("dbname = 'DB1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("UPDATE product SET name = %s, value = %s WHERE id = %s",(name, value, id))
    con.commit()
    con.close()

def view_records():
    con = psycopg2.connect("dbname = 'DB1' user = 'postgres' password = 'postgres123' host = 'localhost' port = '5432'")
    cur = con.cursor()
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    con.close()
    return rows

# create_table()

# insert_values(111,"Ipad",800.00)
# insert_values(222,"Imac",2200.00)
# insert_values(333,"MacAir",850.00)

# delete_values(111)

# update_values("Iphone", 650.00, 333)

print(view_records())







