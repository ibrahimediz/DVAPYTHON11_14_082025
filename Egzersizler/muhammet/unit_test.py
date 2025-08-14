def faktoriyel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktoriyel(n-1)

# Örnek kullanım:
sayi = 5
print(f"{sayi}! = {faktoriyel(sayi)}")