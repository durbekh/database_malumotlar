"""  
    DATABASE COURSE
    MAVZU: MAKTAB AXBOROT TIZIMI (Shool Infomatsion System)
    SELECT bo'yicha chuqurlashtirilgan dars:
        -- ORDER BY (saralash)
        -- LIMIT (chegara)
        -- LIKE (matn qidirish)
        -- BEETWEEN (oraliq)
        -- IN (ro'yxatdan)
        -- DISTINCT (takrorlanmaydigan)
        -- COUNT ,SUM, AVG,MIN , MAX (aggregate funksiyalar)
        -- GROUP BY (guruhlash)
        -- HAVING (guruh filtri)
    MAQSAD : O'quvchilar , fanlar va baholar jadvallaridan
    professional darajada ma'lumot olishni o'rganish.
"""
import sqlite3 as sq

with sq.connect("maktab") as con:
    cur = con.cursor()
    # ========================================================
    # 1-BO'LIM , JADVALLARNI YARATISH
    # ========================================================
    # Maktab axborot tizimida 3 ta asosiy jadval bo'ladi:
    #     1) o'quvchilar - o'quvchilar haqida ma'lumot
    #     2) fanlar - o'qitiladigan fanlar va ularning ustozlari
    #     3) baholar - o'quvchilarning fanlardan olgan baholari
    # Jadvallar bir-biri bilan id orqali bog'langan (foreign key).
    # ========================================================
    cur.execute("""CREATE TABLE IF NOT EXISTS oquvchilar (
        id INTEGER PRIMARY KEY,
        ism TEXT NOT NULL,
        familya TEXT NOT NULL,
        sinf TEXT NOT NULL,          --masalan : '10-A' , '11-B'
        tugulgan_yil INTEGER,
        telefon TEXT 
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS fanlar (
        id INTEGER PRIMARY KEY ,
        nomi TEXT NOT NULL UNIQUE,
        oqituvchi TEXT NOT NULL,
        haftalik_soat INTEGER   --haftada necha soat o'qitiladi
    )""")

    cur.execute("""CREATE TABLE IF NOT EXISTS baholar (
        id INTEGER PRIMARY KEY,
        oquvchi_id INTEGER NUT NULL,
        fan_id INTEGER NOT NULL,
        ball INTEGER NOT NULL,
        sana TEXT NOT NULL,
        FOREIGN KEY (oquvchi_id) REFERENCES oquvchilar(id),
        FOREIGN KEY (fan_id) REFERENCES fanlar(id)
    )""")
    
    # ===========================================================
    # 2- BO'LIM . MA'LUMOTLARNI KIRITISH
    # ===========================================================
    # executemany() yordamida bir nechata qatorni bir buyruqda
    # qo'shamiz . INSERT OR IGNORE - id takrorlanmasligi uchun.
    # ===========================================================
    
    oquvchilar_royxati = [
        (1 , 'Diyorbek' , 'Baxtiyorov' , '9-A' , 2010,'+998901234567'),
        (2 , 'Shehnazar' , 'Baxtiyorov' , '9-A' , 2010,'+998901234577'),
        (3 , 'Behruz' , 'Baxtiyorov' , '9-A' , 2010,'+998901234767'),
        (4 , 'Surojbek' , 'Boltabayev' , '9-A' , 2010,'+99890123767'),
        (5 , 'Jahongir' , 'Farhadov' , '9-A' , 2010,'+998901274567'),
        (6 , 'Durbek' , 'Hayotbekov' , '9-A' , 2010,'+998901734567'),
        (7 , 'Foziljon' , 'Ozodbayev' , '9-A' , 2010,'+998907234567'),
        (8 , 'Jahongir' , 'Ozodov' , '9-A' , 2010,'+998901234777'),
        (9 , 'Farruh' , 'Olimov' , '9-A' , 2010,'+998901237777'),
        (10 , 'Muhammadrahimhon' , 'Muhammedjanov' , '9-A' , 2010,'+998901277777'),
        (11 , 'Salohiddin' , 'Rajabboyev' , '9-A' , 2010,'+998901277567'),
        (12 , 'Mehroj' , 'Otaboyev' , '9-A' , 2010,'+9989087734567') ,
        (13 , 'Akbarshoh' , 'Ramanov' , '9-A' , 2010,'+998901254567'),
        (14 , 'Nurali' , 'Xosinov' , '9-A' , 2010,'+998901444567'),
        (15 , 'Hamrozbek' , 'Subhonberdiyev' , '9-A' , 2010,'+998901334567'),
        (16 , 'Azim' , 'Shuhratov' , '9-A' , 2010,'+998902234567'),
        (17 , 'Navroz' , 'Rajabov' , '9-A' , 2010,'+998901235567'),
        (18 , 'Salimbek' , 'Qurbonboyev' , '9-A' , 2010,'+998901454567'),
        (19 , 'Amirbek' , 'Yusupov' , '9-A' , 2010,'+998901236667'),
        (20 , 'Hikmat' , 'Zaripov' , '9-A' , 2010,'+998901235567'),
        (21 , 'Salimboy' , 'Rajabboyev' , '9-A' , 2010,'+998901004567'),
        (22 , 'Ilyos' , 'Toraboyev' , '9-A' , 2010,'+998901266567'),
        (23 , 'Xurmatjon' , 'Xolmurotov' , '9-A' , 2010,'+998905234567')   
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO oquvchilar VALUES (? , ? , ? , ? , ? , ?)",
        oquvchilar_royxati
    )
    
    fanlar_royxati = [
        (1, 'Matematika',             'Karimova Zulfiya Akmalovna',       6),
        (2, 'Fizika',                 'Rahimov Botir Sodiqovich',         4),
        (3, 'Kimyo',                  'Yusupova Mavluda Bahodirovna',     3),
        (4, 'Biologiya',              'Tursunov Sherzod Ravshanovich',    3),
        (5, 'Ona tili va adabiyot',   'Saidova Munira Akromovna',         5),
        (6, 'Ingliz tili',            'Olimova Nargiza Tolibovna',        4),
        (7, 'Tarix',                  'Nazarov Akmal Tursunovich',        2),
        (8, 'Informatika',            'Sharipov Jasur Komilovich',        3),
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO fanlar VALUES (?, ?, ?, ?)",
        fanlar_royxati
    )
    baholar_royxati = [
        (1,  1, 1, 92, '2026-04-05'),  (2,  1, 2, 78, '2026-04-08'),
        (3,  1, 3, 85, '2026-04-12'),  (4,  1, 5, 88, '2026-04-15'),
        (5,  1, 8, 95, '2026-04-18'),
        (6,  2, 1, 98, '2026-04-05'),  (7,  2, 2, 95, '2026-04-08'),
        (8,  2, 3, 90, '2026-04-12'),  (9,  2, 4, 96, '2026-04-14'),
        (10, 2, 5, 92, '2026-04-15'),
        (11, 3, 1, 65, '2026-04-05'),  (12, 3, 2, 70, '2026-04-08'),
        (13, 3, 3, 58, '2026-04-12'),  (14, 3, 6, 75, '2026-04-16'),
        (15, 4, 1, 88, '2026-04-05'),  (16, 4, 4, 94, '2026-04-14'),
        (17, 4, 5, 90, '2026-04-15'),  (18, 4, 6, 85, '2026-04-16'),
        (19, 5, 1, 72, '2026-04-05'),  (20, 5, 7, 80, '2026-04-17'),
        (21, 5, 8, 88, '2026-04-18'),
        (22, 6, 3, 95, '2026-04-12'),  (23, 6, 4, 92, '2026-04-14'),
        (24, 6, 6, 89, '2026-04-16'),
        (25, 7, 2, 82, '2026-04-08'),  (26, 7, 8, 91, '2026-04-18'),
        (27, 8, 1, 86, '2026-04-05'),  (28, 8, 5, 94, '2026-04-15'),
        (29, 8, 6, 88, '2026-04-16'),
        (30, 9, 2, 76, '2026-04-08'),  (31, 9, 7, 85, '2026-04-17'),
        (32, 10, 3, 89, '2026-04-12'), (33, 10, 4, 91, '2026-04-14'),
        (34, 10, 5, 87, '2026-04-15'),
        (35, 11, 1, 55, '2026-04-05'), (36, 11, 2, 60, '2026-04-08'),
        (37, 11, 8, 78, '2026-04-18'),
        (38, 12, 5, 96, '2026-04-15'), (39, 12, 6, 93, '2026-04-16'),
        (40, 12, 7, 90, '2026-04-17'),
        (38, 13, 5, 96, '2026-04-15'), (39, 13, 6, 93, '2026-04-16'),
        (40, 13, 7, 90, '2026-04-17'),
        (38, 14, 5, 96, '2026-04-15'), (39, 14, 6, 93, '2026-04-16'),
        (40, 14, 7, 90, '2026-04-17'),
        (38, 15, 5, 96, '2026-04-15'), (39, 15, 6, 93, '2026-04-16'),
        (40, 15, 7, 90, '2026-04-17'),
        (38, 16, 5, 96, '2026-04-15'), (39, 16, 6, 93, '2026-04-16'),
        (40, 16, 7, 90, '2026-04-17'),
        (38, 17, 5, 96, '2026-04-15'), (39, 17, 6, 93, '2026-04-16'),
        (40, 17, 7, 90, '2026-04-17'),
        (38, 18, 5, 96, '2026-04-15'), (39, 18, 6, 93, '2026-04-16'),
        (40, 18, 7, 90, '2026-04-17'),
        (38, 19, 5, 96, '2026-04-15'), (39, 19, 6, 93, '2026-04-16'),
        (40, 19, 7, 90, '2026-04-17'),
        (38, 20, 5, 96, '2026-04-15'), (39, 20, 6, 93, '2026-04-16'),
        (40, 20, 7, 90, '2026-04-17'),
        (38, 21, 5, 96, '2026-04-15'), (39, 21, 6, 93, '2026-04-16'),
        (40, 21, 7, 90, '2026-04-17'),
        (38, 22, 5, 96, '2026-04-15'), (39, 22, 6, 93, '2026-04-16'),
        (40, 22, 7, 90, '2026-04-17'),
        (38, 23, 5, 96, '2026-04-15'), (39, 23, 6, 93, '2026-04-16'),
        (40, 24, 7, 90, '2026-04-17'),
        
        
    ]
    cur.executemany(
        "INSERT OR IGNORE INTO baholar VALUES (?, ?, ?, ?, ?)",
        baholar_royxati
    )

    con.commit()

    