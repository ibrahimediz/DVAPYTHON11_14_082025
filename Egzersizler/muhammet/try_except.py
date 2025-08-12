# try:
#     a=int(input("İlk sayıyı giriniz:"))
#     b=int(input("İkinci sayiyiy giriniz:"))
#     print(a/b)
# except Exception as hata:
#     print("Hata olustu:", hata)

try:
    a=int(input("İlk sayıyı giriniz:"))
    b=int(input("İkinci sayiyiy giriniz:"))
    print(a/b)
except ZeroDivisionError:
    print("fgdf")
finally:
    print("final olarak çalışır4")

