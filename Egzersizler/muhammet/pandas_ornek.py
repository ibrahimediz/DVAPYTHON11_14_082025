import pandas as pd
import numpy as np

print("Pandas sürümü:", pd.__version__)
print("NumPy sürümü:", np.__version__)


# Basit bir DataFrame oluşturalım
data = {
    'Ürün': ['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye'],
    'Fiyat': [15000, 8500, 6000, 750, 450],
    'Stok': [25, 45, 30, 120, 80],
    'Kategori': ['Bilgisayar', 'Telefon', 'Tablet', 'Aksesuar', 'Aksesuar']
}

# DataFrame oluşturma
urun_df = pd.DataFrame(data)

# DataFrame'in ilk 3 satırını göster
print("Ürün DataFrame'inin İlk 3 Satırı:")
print(urun_df.head(3))