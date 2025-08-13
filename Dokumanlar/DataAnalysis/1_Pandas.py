# %% 
# Pandas kurulumu
# Terminalde çalıştırın: pip install pandas

# Temel import işlemleri
import pandas as pd
import numpy as np

print("Pandas sürümü:", pd.__version__)
print("NumPy sürümü:", np.__version__)

# %%
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

# DataFrame hakkında temel bilgiler
print("\nDataFrame Bilgileri:")
print(f"Boyut: {urun_df.shape}")
print(f"Veri Tipi: {urun_df.dtypes}")
print(f"Boş Değer Sayısı:\n{urun_df.isnull().sum()}")

# %%
# Series oluşturma
urun_fiyatlari = pd.Series([15000, 8500, 6000, 750, 450],
                          index=['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye'],
                          name="Ürün Fiyatları")

print("Ürün Fiyatları Series'i:")
print(urun_fiyatlari)
print(f"\nİlk ürün fiyatı: {urun_fiyatlari[0]}")
print(f"Laptop fiyatı: {urun_fiyatlari['Laptop']}")

# %%
# DataFrame oluşturma
data = {
    'Ürün': ['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye'],
    'Fiyat': [15000, 8500, 6000, 750, 450],
    'Stok': [25, 45, 30, 120, 80]
}

urun_df = pd.DataFrame(data, index=['P1', 'P2', 'P3', 'P4', 'P5'])

# DataFrame'in temel özellikleri
print("\nDataFrame'in Temel Özellikleri:")
print(f"İndeksler: {urun_df.index}")
print(f"Sütunlar: {urun_df.columns}")
print(f"Değerler:\n{urun_df.values}")

# %%
# Müşteri verilerini oluşturalım
musteri_data = {
    'MüşteriID': [101, 102, 103, 104, 105],
    'Ad': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali'],
    'Yaş': [28, 35, 24, 42, 31],
    'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya'],
    'Son_Sipariş_Tarihi': ['2023-05-15', '2023-06-02', '2023-04-28', '2023-07-10', '2023-06-18'],
    'Toplam_Harcama': [1250.50, 890.75, 2300.00, 450.25, 1575.80]
}

musteri_df = pd.DataFrame(musteri_data)

# Tarih sütununu datetime tipine dönüştürelim
musteri_df['Son_Sipariş_Tarihi'] = pd.to_datetime(musteri_df['Son_Sipariş_Tarihi'])

print("\nMüşteri DataFrame'i:")
print(musteri_df)
print(f"\nVeri tipleri:\n{musteri_df.dtypes}")

# %%
# CSV dosyası okuma
# Örnek bir CSV dosyası oluşturup okuyalım
import os

# Geçici CSV dosyası oluşturalım
csv_data = """Ürün,Fiyat,Stok,Kategori
Laptop,15000,25,Bilgisayar
Akıllı Telefon,8500,45,Telefon
Tablet,6000,30,Tablet
Kulaklık,750,120,Aksesuar
Klavye,450,80,Aksesuar"""

with open('datasets/urunler.csv', 'w', encoding='utf-8') as f:
    f.write(csv_data)

# CSV dosyasını okuma
urunler_df = pd.read_csv('datasets/urunler.csv')

print("\nCSV Dosyasından Okunan Veri:")
print(urunler_df)

# Dosyayı temizleyelim
os.remove('datasets/urunler.csv')

# %%
# Excel dosyası okuma için gerekli kütüphane
# Terminalde: pip install openpyxl

import openpyxl

# Geçici Excel dosyası oluşturalım
excel_data = urunler_df.copy()
excel_data.to_excel('datasets/urunler.xlsx', index=False)

# Excel dosyasını okuma
urunler_excel = pd.read_excel('urunler.xlsx')

print("\nExcel Dosyasından Okunan Veri:")
print(urunler_excel)

# Dosyayı temizleyelim
os.remove('urunler.xlsx')

# %%
# SQL desteği için gerekli kütüphane
# Terminalde: pip install sqlalchemy

from sqlalchemy import create_engine

# Geçici bir SQLite veritabanı oluşturalım
engine = create_engine('sqlite:///urunler.db')

# DataFrame'i SQL tablosuna kaydet
urunler_df.to_sql('urunler', engine, if_exists='replace', index=False)

# SQL sorgusu ile veri okuma
sql_df = pd.read_sql('SELECT * FROM urunler', engine)

print("\nSQL Veritabanından Okunan Veri:")
print(sql_df)

# Veritabanını temizleyelim
os.remove('urunler.db')

# %%
# Farklı formatlara veri yazma
urunler_df.to_csv('urunler_yeni.csv', index=False)
urunler_df.to_excel('urunler_yeni.xlsx', index=False)
urunler_df.to_json('urunler_yeni.json', orient='records', force_ascii=False)

print("\nVeri farklı formatlara başarıyla yazıldı!")

# Dosyaları temizleyelim
os.remove('urunler_yeni.csv')
os.remove('urunler_yeni.xlsx')
os.remove('urunler_yeni.json')

# %%
# Gerçek bir senaryo simülasyonu
gunluk_satis = {
    'Tarih': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05'],
    'Toplam_Satis': [12500, 18750, 9500, 22300, 15600],
    'Musteri_Sayisi': [45, 67, 32, 89, 54],
    'Ortalama_Siparis': [277.78, 279.85, 296.88, 250.56, 288.89]
}

satis_df = pd.DataFrame(gunluk_satis)
satis_df['Tarih'] = pd.to_datetime(satis_df['Tarih'])

# CSV'ye kaydet
satis_df.to_csv('gunluk_satis_raporu.csv', index=False)

# CSV'den tekrar oku
rapor_df = pd.read_csv('gunluk_satis_raporu.csv')
rapor_df['Tarih'] = pd.to_datetime(rapor_df['Tarih'])

# Analiz yap
rapor_df['Haftanin_Gunu'] = rapor_df['Tarih'].dt.day_name()
haftalik_toplam = rapor_df.groupby('Haftanin_Gunu')['Toplam_Satis'].sum()

# Excel raporu oluştur
with pd.ExcelWriter('yonetici_raporu.xlsx') as writer:
    rapor_df.to_excel(writer, sheet_name='Günlük Satış', index=False)
    haftalik_toplam.to_excel(writer, sheet_name='Haftalık Toplam')

print("\nYönetici raporu başarıyla oluşturuldu!")

# Dosyaları temizleyelim
os.remove('gunluk_satis_raporu.csv')
os.remove('yonetici_raporu.xlsx')

# %%
# Eksik veri içeren örnek bir DataFrame oluşturalım
eksik_veri = {
    'Ürün': ['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye', 'Fare'],
    'Fiyat': [15000, 8500, None, 750, 450, 250],
    'Stok': [25, None, 30, 120, 80, None],
    'Kategori': ['Bilgisayar', 'Telefon', None, 'Aksesuar', 'Aksesuar', 'Aksesuar']
}

eksik_df = pd.DataFrame(eksik_veri)

print("\nEksik Veri İçeren DataFrame:")
print(eksik_df)
print(f"\nEksik değer sayısı:\n{eksik_df.isnull().sum()}")

# Eksik değerleri doldurma
eksik_df['Fiyat'] = eksik_df['Fiyat'].fillna(eksik_df['Fiyat'].mean())
eksik_df['Stok'] = eksik_df['Stok'].fillna(eksik_df['Stok'].median())
eksik_df['Kategori'] = eksik_df['Kategori'].fillna('Bilinmiyor')

print("\nDoldurulmuş DataFrame:")
print(eksik_df)

# %%
# Aykırı değer içeren örnek veri
aykiri_veri = {
    'MüşteriID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'Yaş': [28, 35, 24, 42, 31, 29, 33, 120, 27, 30],
    'Harcama': [1250, 890, 2300, 450, 1575, 950, 1100, 10000, 750, 1300]
}

musteri_df = pd.DataFrame(aykiri_veri)

print("\nAykırı Değer İçeren Müşteri Verisi:")
print(musteri_df)

# Aykırı değer tespiti (IQR yöntemi)
def aykiri_tespit(df, sütun):
    Q1 = df[sütun].quantile(0.25)
    Q3 = df[sütun].quantile(0.75)
    IQR = Q3 - Q1
    alt_sinir = Q1 - 1.5 * IQR
    ust_sinir = Q3 + 1.5 * IQR
    return df[(df[sütun] < alt_sinir) | (df[sütun] > ust_sinir)]

print("\nYaş Sütunundaki Aykırı Değerler:")
print(aykiri_tespit(musteri_df, 'Yaş'))

print("\nHarcama Sütunundaki Aykırı Değerler:")
print(aykiri_tespit(musteri_df, 'Harcama'))

# Aykırı değerleri yönetme (ortalama ile değiştirme)
musteri_df.loc[musteri_df['Yaş'] > 100, 'Yaş'] = musteri_df['Yaş'].median()
musteri_df.loc[musteri_df['Harcama'] > 5000, 'Harcama'] = musteri_df['Harcama'].median()

print("\nAykırı Değerler Düzeltilmiş Veri:")
print(musteri_df)

# %%
# Veri dönüşümleri
urun_verisi = {
    'Ürün': ['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye'],
    'Fiyat': ['15.000 TL', '8.500 TL', '6.000 TL', '750 TL', '450 TL'],
    'Stok': [25, 45, 30, 120, 80],
    'Kategori': ['Bilgisayar', 'Telefon', 'Tablet', 'Aksesuar', 'Aksesuar']
}

urun_df = pd.DataFrame(urun_verisi)

print("\nOrijinal Ürün Verisi:")
print(urun_df)

# Fiyat sütununu temizleme ve sayısal hale getirme
urun_df['Fiyat'] = urun_df['Fiyat'].str.replace('.', '', regex=False)
urun_df['Fiyat'] = urun_df['Fiyat'].str.replace(' TL', '', regex=False)
urun_df['Fiyat'] = urun_df['Fiyat'].astype(int)

# Kategori sütununu kategorik veri tipine dönüştürme
urun_df['Kategori'] = urun_df['Kategori'].astype('category')

print("\nDönüştürülmüş Ürün Verisi:")
print(urun_df)
print(f"\nVeri tipleri:\n{urun_df.dtypes}")

# %%
# Müşteri segmentasyonu için veri hazırlama
musteri_verisi = {
    'MüşteriID': [1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010],
    'Ad': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali', 'Zeynep', 'Can', 'Deniz', 'Ece', 'Kemal'],
    'Yaş': [28, None, 24, 42, 31, 29, None, 33, 27, 30],
    'Cinsiyet': ['E', 'E', 'K', 'K', 'E', 'K', 'E', None, 'K', 'E'],
    'Son_Alışveriş': ['2023-05-15', '2023-06-02', '2023-04-28', None, '2023-06-18', '2023-07-10', '2023-03-22', '2023-06-25', '2023-05-30', '2023-07-05'],
    'Toplam_Harcama': [1250.50, 890.75, None, 450.25, 1575.80, 2300.00, 950.00, 1100.50, 750.25, 1300.75],
    'Sık_Alınan_Kategori': ['Giyim', 'Elektronik', 'Kozmetik', 'Giyim', 'Elektronik', 'Ev Eşyası', None, 'Giyim', 'Kozmetik', 'Spor']
}

musteri_df = pd.DataFrame(musteri_verisi)

print("\nOrijinal Müşteri Verisi:")
print(musteri_df.head())

# 1. Eksik değerleri doldurma
musteri_df['Yaş'] = musteri_df['Yaş'].fillna(musteri_df['Yaş'].median())
musteri_df['Cinsiyet'] = musteri_df['Cinsiyet'].fillna('Bilinmiyor')
musteri_df['Son_Alışveriş'] = musteri_df['Son_Alışveriş'].fillna(pd.Timestamp.now().strftime('%Y-%m-%d'))
musteri_df['Toplam_Harcama'] = musteri_df['Toplam_Harcama'].fillna(musteri_df['Toplam_Harcama'].mean())
musteri_df['Sık_Alınan_Kategori'] = musteri_df['Sık_Alınan_Kategori'].fillna('Diğer')

# 2. Tarih sütununu datetime'a dönüştürme
musteri_df['Son_Alışveriş'] = pd.to_datetime(musteri_df['Son_Alışveriş'])

# 3. Müşteri segmentasyonu için yeni özellikler oluşturma
bugun = pd.Timestamp.now()
musteri_df['Son_Alışverişten_Itibaren_Gün'] = (bugun - musteri_df['Son_Alışveriş']).dt.days
musteri_df['Harcama_Segmenti'] = pd.cut(musteri_df['Toplam_Harcama'],
                                      bins=[0, 500, 1500, float('inf')],
                                      labels=['Düşük', 'Orta', 'Yüksek'])

print("\nTemizlenmiş ve Dönüşmüş Müşteri Verisi:")
print(musteri_df.head())

# 4. Veriyi kategorik sütunlar için kodlama
musteri_df['Cinsiyet_Kod'] = musteri_df['Cinsiyet'].map({'E': 0, 'K': 1, 'Bilinmiyor': 2})
musteri_df = pd.get_dummies(musteri_df, columns=['Sık_Alınan_Kategori'], prefix='Kategori')

print("\nSon Veri Yapısı:")
print(musteri_df.head())
print(f"\nSon veri boyutu: {musteri_df.shape}")

# %%# Ürün verisi oluşturalım
urun_verisi = {
    'ÜrünID': [1, 2, 3, 4, 5, 6, 7, 8],
    'Ürün': ['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye', 'Fare', 'Monitör', 'Yazıcı'],
    'Fiyat': [15000, 8500, 6000, 750, 450, 250, 3500, 2800],
    'Stok': [25, 45, 30, 120, 80, 100, 15, 20],
    'Kategori': ['Bilgisayar', 'Telefon', 'Tablet', 'Aksesuar', 'Aksesuar', 'Aksesuar', 'Bilgisayar', 'Yazıcı']
}

urun_df = pd.DataFrame(urun_verisi)

print("\nOrijinal Ürün Verisi:")
print(urun_df)

# 1. Belirli sütunları seçme
print("\nSadece Ürün ve Fiyat Sütunları:")
print(urun_df[['Ürün', 'Fiyat']])

# 2. Koşullu filtreleme
print("\nFiyatı 1000 TL üzerindeki ürünler:")
print(urun_df[urun_df['Fiyat'] > 1000])

# 3. Çoklu koşullu filtreleme
print("\nFiyatı 1000 TL üzerinde ve Stokta olan ürünler:")
print(urun_df[(urun_df['Fiyat'] > 1000) & (urun_df['Stok'] > 0)])

# 4. isin() ile filtreleme
print("\nBilgisayar veya Telefon kategorisindeki ürünler:")
print(urun_df[urun_df['Kategori'].isin(['Bilgisayar', 'Telefon'])])

# 5. String işlemleri ile filtreleme
print("\n'K' ile başlayan ürünler:")
print(urun_df[urun_df['Ürün'].str.startswith('K')])


# %%
# Satış verisi oluşturalım
satis_verisi = {
    'Tarih': ['2023-07-01', '2023-07-01', '2023-07-02', '2023-07-02', '2023-07-03', '2023-07-03'],
    'Ürün': ['Laptop', 'Kulaklık', 'Akıllı Telefon', 'Klavye', 'Tablet', 'Fare'],
    'Kategori': ['Bilgisayar', 'Aksesuar', 'Telefon', 'Aksesuar', 'Tablet', 'Aksesuar'],
    'Miktar': [2, 5, 3, 8, 4, 10],
    'Birim_Fiyat': [15000, 750, 8500, 450, 6000, 250],
    'Şehir': ['İstanbul', 'Ankara', 'İstanbul', 'İzmir', 'Ankara', 'İstanbul']
}

satis_df = pd.DataFrame(satis_verisi)
satis_df['Tarih'] = pd.to_datetime(satis_df['Tarih'])
satis_df['Toplam_Tutar'] = satis_df['Miktar'] * satis_df['Birim_Fiyat']

print("\nSatış Verisi:")
print(satis_df)

# 1. Kategoriye göre gruplama ve toplama
kategori_toplam = satis_df.groupby('Kategori').agg({
    'Miktar': 'sum',
    'Toplam_Tutar': 'sum'
}).reset_index()

print("\nKategoriye Göre Toplam Satışlar:")
print(kategori_toplam)

# 2. Tarih ve kategoriye göre gruplama
tarih_kategori = satis_df.groupby([pd.Grouper(key='Tarih', freq='D'), 'Kategori']).agg({
    'Miktar': 'sum',
    'Toplam_Tutar': 'sum'
}).reset_index()

print("\nGünlük ve Kategoriye Göre Satışlar:")
print(tarih_kategori)

# 3. Pivot tablo oluşturma
pivot_tablo = satis_df.pivot_table(
    values='Toplam_Tutar',
    index='Tarih',
    columns='Kategori',
    aggfunc='sum',
    fill_value=0
)

print("\nPivot Tablo (Kategorilere Göre Günlük Satışlar):")
print(pivot_tablo)

# %%
# İki farklı veri seti oluşturalım
urun_verisi = {
    'ÜrünID': [1, 2, 3, 4, 5],
    'Ürün': ['Laptop', 'Akıllı Telefon', 'Tablet', 'Kulaklık', 'Klavye'],
    'Fiyat': [15000, 8500, 6000, 750, 450],
    'Kategori': ['Bilgisayar', 'Telefon', 'Tablet', 'Aksesuar', 'Aksesuar']
}

musteri_verisi = {
    'MüşteriID': [101, 102, 103, 104, 105],
    'Ad': ['Ahmet', 'Mehmet', 'Ayşe', 'Fatma', 'Ali'],
    'Şehir': ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya']
}

satis_verisi = {
    'SatisID': [1001, 1002, 1003, 1004, 1005],
    'MüşteriID': [101, 102, 103, 104, 105],
    'ÜrünID': [1, 2, 3, 4, 5],
    'Miktar': [1, 2, 1, 3, 2],
    'Tarih': ['2023-07-01', '2023-07-02', '2023-07-03', '2023-07-04', '2023-07-05']
}

urun_df = pd.DataFrame(urun_verisi)
musteri_df = pd.DataFrame(musteri_verisi)
satis_df = pd.DataFrame(satis_verisi)
satis_df['Tarih'] = pd.to_datetime(satis_df['Tarih'])

print("\nÜrün Verisi:")
print(urun_df)
print("\nMüşteri Verisi:")
print(musteri_df)
print("\nSatış Verisi:")
print(satis_df)

# 1. Satış ve ürün verisini birleştirme (inner join)
satis_urun = pd.merge(satis_df, urun_df, on='ÜrünID', how='inner')
print("\nSatış ve Ürün Verisi Birleştirme (Inner Join):")
print(satis_urun)

# 2. Tüm verileri birleştirme (left join)
tam_veri = pd.merge(satis_urun, musteri_df, on='MüşteriID', how='left')
print("\nTüm Veri Birleştirme (Left Join):")
print(tam_veri)

# 3. Pivot tablo ile raporlama
rapor = tam_veri.pivot_table(
    values='Miktar',
    index='Şehir',
    columns='Kategori',
    aggfunc='sum',
    fill_value=0
)

print("\nŞehir ve Kategoriye Göre Satış Raporu:")
print(rapor)

# %%
# Gerçekçi satış verisi oluşturalım
np.random.seed(42)  # Sonuçların tekrarlanabilir olması için

# Tarih aralığı
tarihler = pd.date_range(start='2023-01-01', end='2023-06-30', freq='D')

# Ürün kategorileri
kategoriler = ['Giyim', 'Elektronik', 'Kozmetik', 'Ev Eşyası', 'Spor']

# Şehirler
sehirler = ['İstanbul', 'Ankara', 'İzmir', 'Bursa', 'Antalya', 'Adana']

# Rastgele satış verisi oluşturma
satis_verisi = []
for tarih in tarihler:
    for _ in range(np.random.randint(50, 150)):
        musteri_id = np.random.randint(1000, 9999)
        urun_id = np.random.randint(1, 100)
        kategori = np.random.choice(kategoriler)
        sehir = np.random.choice(sehirler)
        miktar = np.random.randint(1, 5)
        birim_fiyat = np.random.uniform(50, 2000)

        satis_verisi.append([
            musteri_id, urun_id, kategori, sehir,
            tarih, miktar, birim_fiyat, miktar * birim_fiyat
        ])

# DataFrame oluşturma
sutunlar = ['MüşteriID', 'ÜrünID', 'Kategori', 'Şehir',
            'Tarih', 'Miktar', 'Birim_Fiyat', 'Toplam_Tutar']
satis_df = pd.DataFrame(satis_verisi, columns=sutunlar)

print("\nOluşturulan Satış Verisi (İlk 5 Satır):")
print(satis_df.head())

# 1. Temel analizler
print("\nTemel İstatistikler:")
print(satis_df.describe())

# 2. Aylık toplam satışlar
satis_df['Ay'] = satis_df['Tarih'].dt.to_period('M')
aylik_satis = satis_df.groupby('Ay')['Toplam_Tutar'].sum().reset_index()
aylik_satis.columns = ['Ay', 'Toplam_Satis']

print("\nAylık Toplam Satışlar:")
print(aylik_satis)

# 3. Kategori bazlı satış analizi
kategori_satis = satis_df.groupby('Kategori').agg(
    Toplam_Satis=('Toplam_Tutar', 'sum'),
    Satis_Sayisi=('Miktar', 'sum'),
    Ortalama_Satis=('Toplam_Tutar', 'mean')
).sort_values('Toplam_Satis', ascending=False).reset_index()

print("\nKategori Bazlı Satış Analizi:")
print(kategori_satis)

# 4. Şehir ve kategori kesişimi
sehir_kategori = satis_df.pivot_table(
    values='Toplam_Tutar',
    index='Şehir',
    columns='Kategori',
    aggfunc='sum',
    fill_value=0
)

print("\nŞehir ve Kategori Kesişimi:")
print(sehir_kategori)

# 5. En çok harcama yapan müşteriler
en_cok_harcama = satis_df.groupby('MüşteriID')['Toplam_Tutar'].sum().sort_values(ascending=False).head(10).reset_index()
en_cok_harcama.columns = ['MüşteriID', 'Toplam_Harcama']

print("\nEn Çok Harcama Yapan 10 Müşteri:")
print(en_cok_harcama)

# %%
# Satış verisi oluşturalım
aylik_satis = {
    'Ay': ['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran'],
    'Elektronik': [125000, 135000, 110000, 145000, 155000, 165000],
    'Giyim': [95000, 105000, 115000, 100000, 105000, 110000],
    'Kozmetik': [75000, 80000, 85000, 90000, 95000, 100000]
}

satis_df = pd.DataFrame(aylik_satis)

print("\nAylık Satış Verisi:")
print(satis_df)

# 1. Çizgi grafiği
satis_df.set_index('Ay').plot(
    kind='line',
    title='Aylık Kategori Bazlı Satışlar',
    xlabel='Ay',
    ylabel='Satış Tutarı (TL)',
    figsize=(10, 6)
)

# 2. Çubuk grafiği
satis_df.set_index('Ay').plot(
    kind='bar',
    title='Aylık Kategori Bazlı Satışlar',
    xlabel='Ay',
    ylabel='Satış Tutarı (TL)',
    figsize=(10, 6)
)

# 3. Pasta grafiği (Haziran ayı için)
haziran_satis = satis_df[satis_df['Ay'] == 'Haziran'].iloc[0, 1:].to_dict()
pd.Series(haziran_satis).plot(
    kind='pie',
    title='Haziran Ayı Kategori Dağılımı',
    autopct='%1.1f%%',
    figsize=(8, 8)
)

# %%
