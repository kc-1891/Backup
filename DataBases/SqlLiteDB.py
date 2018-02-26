import sqlite3

def create_table():
    # Create connection
    con = sqlite3.connect('product_details.db')

    # Create cursor
    cur = con.cursor()

    # execute command from the cursor
    cur.execute("CREATE TABLE IF NOT EXISTS product(id INTEGER , name TEXT, value REAL  )")

    # DB commit
    con.commit()

    # Close connection
    con.close()



def insert_values(id,name,value):
    con = sqlite3.connect('product_details.db')
    cur = con.cursor()
    cur.execute("INSERT INTO product VALUES(?,?,?)",(id,name,value))
    con.commit()
    con.close()

def delete_values(id):
    con = sqlite3.connect('product_details.db')
    cur = con.cursor()
    cur.execute("DELETE FROM product WHERE id = ?", (id,))
    con.commit()
    con.close()


def update_record(name,value,id):
    con = sqlite3.connect("product_details.db")
    cur = con.cursor()
    cur.execute("UPDATE product SET name = ?, value = ? WHERE id = ?", (name,value,id))
    con.commit()
    con.close

def view_records():
    con = sqlite3.connect("product_details.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM product")
    rows = cur.fetchall()
    cur.close()
    con.close()
    return rows


# insert_values(111,'Iphone',600.00)
# insert_values(222,'Ipad',800.00)
# insert_values(333,'Imac',2200.00)
insert_values(555,'Iphone',650.00)

# delete_values(444)

update_record("MacPro",1500, 111)

print(view_records())

