import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 1) Veriyi yükle
df = pd.read_csv("/workspace/DVAPYTHON11_14_082025/Egzersizler/datasets/titanic/train.csv")

# 2) Cinsiyete göre hayatta kalma sayılarını karşılaştır (crosstab)
ct = pd.crosstab(df["Sex"], df["Survived"])
print("Cinsiyete Göre Hayatta Kalma (Sayı):")
print(ct, end="\n\n")
ct.plot(kind="bar", rot=45)
# 3) Yaş gruplarının hayatta kalma oranlarını görselleştir
bins = [0, 12, 18, 30, 45, 60, np.inf]
labels = ["Child(0-12)", "Teen(13-18)", "Young(19-30)", "Adult(31-45)", "Mid(46-60)", "Senior(60+)"]
df = df.copy()
df["AgeGroup"] = pd.cut(df["Age"], bins=bins, labels=labels, right=True, include_lowest=True)
survival_by_agegroup = df.groupby("AgeGroup", observed=True)["Survived"].mean().reindex(labels)
print("Yaş Gruplarına Göre Hayatta Kalma Oranı:")
print(survival_by_agegroup, end="\n\n")

plt.figure()
survival_by_agegroup.plot(kind="bar", rot=45)
plt.title("Yaş Gruplarına Göre Hayatta Kalma Oranı")
plt.xlabel("Yaş Grubu")
plt.ylabel("Oran (0-1)")
plt.tight_layout()
plt.show()

# 4) Sınıflara göre bilet fiyatlarının ortalaması
fare_by_class = df.groupby("Pclass")["Fare"].mean().to_frame("MeanFare")
print("Sınıflara Göre Ortalama Bilet Fiyatı:")
print(fare_by_class, end="\n\n")
fare_by_class.plot(kind="bar", rot=45)
# 5) En çok hangi limandan yolcu bindi? (Embarked)
embark_counts = df["Embarked"].value_counts(dropna=False)
print("Limanlara Göre Biniş Sayıları:")
print(embark_counts, end="\n\n")
print("En çok biniş yapılan liman:", embark_counts.idxmax())
embark_counts.plot(kind="bar", rot=45)
# 6) Korelasyon matrisi (sayısal sütunlar)
numeric_df = df.select_dtypes(include=[np.number])
corr_matrix = numeric_df.corr(numeric_only=True)
print("\nKorelasyon Matrisi (sayısal sütunlar):")
print(corr_matrix)

# Isı haritası
sns.heatmap(corr_matrix,
            annot=True,
            fmt=".2f",
            cmap='coolwarm',
            linewidths=0.5,
            annot_kws={"size": 12})

plt.title('Korelasyon Matrisi', fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()