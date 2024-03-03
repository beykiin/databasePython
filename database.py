import sqlite3 as sql
baglanti=sql.connect("ornek.db") #ornek.sqlite3
cursor=baglanti.cursor()

def tablo_olustur():
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ogrenciler (
            id INTEGER,
            adSoyad TEXT,
            yas INTEGER,
            PRIMARY KEY ('id' AUTOINCREMENT) )""")
    baglanti.commit()

tablo_olustur()
# 1.YÖNTEM
def veri_ekle():
    cursor.execute("""
    INSERT INTO ogrenciler (adSoyad,yas) VALUES('Yasin Beken',25)""")
    baglanti.commit()
# veri_ekle()

# 2.YÖNTEM
def veri_ekle2(ad,yas):
    cursor.execute(f"""
    INSERT INTO ogrenciler (adSoyad,yas) VALUES('{ad}',{yas})""")
    baglanti.commit()
# veri_ekle2("Texaslı Billy",25)

# 3.YÖNTEM
def veri_ekle3(ad,yas):
    cursor.execute("insert into ogrenciler (adSoyad,yas) values (?,?)",(ad,yas))
    baglanti.commit()
# "x=input("Ad Yaz: ")
# y=int(input("Yaşınnı Yaz: "))"
# veri_ekle3(x,y)

def veri_oku():
    cursor.execute("select * from ogrenciler")
    bilgiler=cursor.fetchall()
    for i in bilgiler:
        print(i)
# veri_oku()
def veri_oku2():
    cursor.execute("select * from ogrenciler")
    bilgiler=cursor.fetchone()
    print(bilgiler)
    # for i in bilgiler:
    #     print(i)
# veri_oku2()
def veri_oku3():
    cursor.execute("select * from ogrenciler")
    bilgiler=cursor.fetchmany()
    for i in bilgiler:
        print(i)
# veri_oku3()

def veri_guncelle():
    cursor.execute("update ogrenciler set adSoyad='Boklu Kazım' where id=2")
    baglanti.commit()
# veri_guncelle()

def veri_guncelle2(ad,yas):
    cursor.execute(f"update ogrenciler set adSoyad='{ad}',yas={yas} where id=4")
    baglanti.commit()
# veri_guncelle2("Texaslı Billy",55)

def veri_guncelle3(ad,yas):
    cursor.execute("update ogrenciler set adSoyad=(?),yas=(?) where id=4",(ad,yas))
    baglanti.commit()
# veri_guncelle3("Karizmatik Serkan",20)

def veri_guncelle4(ad,yas):
    cursor.execute(f"update ogrenciler set adSoyad='{ad}',yas={yas} where id=1")
    baglanti.commit()
# x=input("İsim Gir: ")
# y=int(input("Yasını Gir: "))
# veri_guncelle4(x,y)

def veri_sil():
    cursor.execute("delete from ogrenciler where id=2")
    baglanti.commit()
# veri_sil()
