import sqlite3 as sq
with sq.connect("database.db") as con:
    cur = con.cursor()
    
    cur.execute("""CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER        
        )""")
    
    cur.execute("""CREATE TABLE IF NOT EXISTS xaridlar (
        id INTEGER PRIMARY KEY,
        user_id INTEGER,
        product_name TEXT,
        price INTEGER        
        ) """)
    
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name , age)
                VALUES (1 , 'Xusniddin' , 'Urinbayev', 18)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name  , age)
                VALUES (2 , 'Anvar' , 'Davronov',  15)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name ,  age)
                VALUES (3 , 'Rasulbek' , 'Hakimboyev',  25)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name ,  age)
                VALUES (4 , 'Durbek' , 'Hayotbekov' , 17)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name ,  age)
                VALUES (5 , 'Farhotjon' , 'Abdullayev' , 35)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name , age)
                VALUES (6 , 'Navrozbek' , 'Rajabov',  45)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name  , age)
                VALUES (7 , 'Lobarhon' , 'Qodirova', 23)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name , age)
                VALUES (8 , 'Shohjahon' , 'Baxtiyorov' , 22)""")
    cur.execute("""INSERT OR IGNORE INTO users (id , first_name , last_name , age)
                VALUES (9 , 'Bekzod' , 'Lozayev',  21)""")
    
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id ,user_id , product_name , price)
                VALUES (1 ,1 , 'Olma' , 25000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar (id ,user_id , product_name , price)
                VALUES (2 , 2 , 'Uzum', 15000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (3 ,3 ,'Olcha' , 15000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (4,4,'Gilos',35000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (5 ,5 ,'Banan' , 18000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (6,6,'Kitob',125000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (7 ,7 ,'Telefon' , 15_000_000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (8,8,'Kompyuter',25_000_000)""")
    cur.execute("""INSERT OR IGNORE INTO xaridlar(id , user_id , product_name , price)
                VALUES (9,9,'Kozoynak',300_000)""")
    con.commit()
    
    cur.execute("UPDATE users SET age = 25 WHERE id = 1")
    con.commit() 

    print("\n=== id=1 foydalanuvchining yoshi yangilandi ===")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)

    cur.execute("""UPDATE users
                SET first_name = 'BOBUR' , last_name = 'Mirzayev
                WHERE id = 2'""")
    
    print("\n=== id=2 foydalanuvchining ism-familyasi yangilandi ===")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)

    yangi_yosh = 25
    user_id = 1
    cur.execute("UPDATE users SET age = ? WHERE id = ?", (yangi_yosh , user_id))
    con.commit()
    print("\n=== Parametr orqali yangilandi ===")
    cur.execute("SELECT * FROM users")
    for row in cur.fetchall():
        print(row)







