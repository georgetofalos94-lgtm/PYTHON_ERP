def quantity():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("barcode")
    bar=int(input())
    c.execute("select name from products where barcode=?",(bar,))
    z=c.fetchone()
    print (z[0])
    c.execute("select quantity from products where barcode=?",(bar,))
    x=c.fetchone()
    print (x[0])
    
def inpt():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("barcode")
    bar=int(input())
    print("name")
    n=input()
    print("description")
    desc=input()
    print("price per piece")
    p=float(input())
    print("quantity")
    quan=int(input())
    c.execute("insert into products(barcode,name,description,price,quantity)values(?,?,?,?,?)",(bar,n,desc,p,quan))
    conn.commit()
    
def sale():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("barc")
    bar=int(input())
    c.execute("select quantity from products where barcode=?",(bar,))
    x=c.fetchone()
    print("h diathesimh posothta tou proiontos einai:")
    print (x[0])
    print("dwste posothta pwlhshs")
    q=int(input())
    quan=x[0]-q
    c.execute("update products set quantity=? where barcode=?",(quan,bar))
    conn.commit()
    c.execute("select price from products where barcode=?",(bar,))
    y=c.fetchone()
    p=y[0]*q
    print("telikh timh:",p)

def change_quantity():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("barcode")
    bar=int(input())
    print("quantity")
    quan=int(input())
    c.execute("update products set quantity=? where barcode=?",(quan,bar))
    conn.commit()
    
def paralavh():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("barcode")
    bar=int(input())
    print("quantity")
    q=int(input())
    c.execute("select quantity from products where barcode=?",(bar,))
    x=c.fetchone()
    quan=x[0]+q
    c.execute("update products set quantity=? where barcode=?",(quan,bar))
    conn.commit()
    
def timh():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("barcode")
    bar=int(input())
    c.execute("select price from products where barcode=?",(bar,))
    x=c.fetchone()
    print("price per piece:\n",x[0])
    
def admin():
    import sqlite3
    conn = sqlite3.connect('ERP.db')
    c = conn.cursor()
    conn.commit()
    print("username:")
    usrnm=input()
    x=c.execute("select username from login where username=?",(usrnm,))
    x=c.fetchone()
    conn.commit()
    while x is not None:
        print("to username xrhsimopoieitai hdh, parakalw dialekse allo:")
        usrnm=input()
        x=c.execute("select username from login where username=?",(usrnm,))
        x=c.fetchone()
        conn.commit()
    print("password:")
    psswrd=input()
    print("gia diaxeiristh pathste 1\ngia aplo xrhsth pathste 2")
    ad_us=int(input())
    c.execute("insert into login(username,password,type)values(?,?,?)",(usrnm,psswrd,ad_us))
    conn.commit()
