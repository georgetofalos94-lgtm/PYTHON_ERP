import sqlite3
from def_erp import quantity,inpt,sale,change_quantity,paralavh,timh,admin
conn = sqlite3.connect('ERP.db')
c = conn.cursor()
conn.commit()
c.execute("""create table if not exists login(username varchar(50),password varchar(50),type int)""")
c.execute("""create table if not exists products(barcode int primary key,name varchar (100),description varchar(1000),price int,quantity int)""")
conn.commit
c.execute("insert into login(username,password,type)values(?,?,?)",("useradmin01","usradmn0100",1))
print("PY ERP\n\n\n")
check="false"
while (check=="false"):
    print("username:")
    usrnm=input()
    print("password:")
    psswrd=input()
    c.execute("select * from login where username==?",(usrnm,))
    x=c.fetchone()
    #print(x)
    if (x is None):
        print("wrong username")
    elif(x[0]==usrnm and x[1]==psswrd):
        print("welcome")
        check="true"
    else:
        print("wrong password")

if(x[2]==1):    
    print("gia eisagwgh proiontos pathste 1\ngia na deite apothema proiontos pathste 2\ngia pwlhsh proiontos pathste 3\ngia allagh apothematos proiontos pathste 4\ngia eisagwgh paralavhs pathste 5\ngia na deite thn timh tou proiontos pathste 6\ngia dhmiourgia xrhsth pathste 7\ngia eksodo pathste 0")
    choice=int(input())
    conn.commit()
    while (choice!=0):
    
        if (choice==1):
            inpt()
    
        elif (choice==2):
           quantity()

        elif (choice==3):
           sale()

        elif (choice==4):
           change_quantity()
        
        elif (choice==5):
            paralavh()
    
        elif (choice==6):
            timh()

        elif (choice==7):
            admin()
        
        print("\ngia eisagwgh proiontos pathste 1\ngia na deite apothema proiontos pathste 2\ngia pwlhsh proiontos pathste 3\ngia allagh apothematos proiontos pathste 4\ngia eisagwgh paralavhs pathste 5\ngia na deite thn timh tou proiontos pathste 6\ngia dhmiourgia xrhsth pathste 7\ngia eksodo pathste 0")
        choice=int(input())

if(x[2]==2):    
    print("gia na deite apothema proiontos pathste 1\ngia pwlhsh proiontos pathste 2\ngia na deite thn timh tou proiontos pathste 3\ngia eksodo pathste 0")
    choice=int(input())
    conn.commit()
    while (choice!=0):
    
        if (choice==1):
            quantity()
    
        elif (choice==2):
           sale()

        elif (choice==3):
           timh()

        print("\ngia na deite apothema proiontos pathste 1\ngia pwlhsh proiontos pathste 2\ngia na deite thn timh tou proiontos pathste 3\ngia eksodo pathste 0")
        choice=int(input())
