from pathlib import Path
yol = Path("Egzersizler") / "ecetin" / "ornek.csv"

yol.parent.mkdir(parents=True, exist_ok=True)

dosya = open(yol, "a+", encoding="utf-8")
print(f"{yol} başarıyla açıldı.")