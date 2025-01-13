# 🐿️ Central Park Mókus Népszámlálás Elemző

<div align="center">

![Mókus Banner](https://img.shields.io/badge/🐿️-Mókus_Elemző-brightgreen)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/pandas-latest-blue)
![Licensz](https://img.shields.io/badge/license-MIT-green)

</div>

## 📋 Projekt Leírás

Ez a projekt a 2018-as Central Park mókus népszámlálási adatokat dolgozza fel, különös tekintettel a mókusok bundaszínére. Az elemzés során megszámoljuk a különböző színű (szürke, fahéjszínű, fekete) mókusokat, és az eredményeket egy könnyen feldolgozható CSV formátumban mentjük el.

## ⚙️ Függőségek

| Függőség | Verzió |
|----------|---------|
| Python   | 3.x+    |
| pandas   | latest  |

## 📁 Fájl Struktúra

```
project/
│
├── 2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250113.csv   # Bemeneti adatok
├── squirrel_analysis.py                                              # Feldolgozó script
└── squirrels_color.csv                                              # Kimeneti adatok
```

## 🚀 Telepítés és Használat

### 1. Környezet Előkészítése

```bash
# Virtual environment létrehozása (opcionális)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# vagy
venv\Scripts\activate     # Windows

# Függőségek telepítése
pip install pandas
```

### 2. Script Futtatása

```bash
python squirrel_analysis.py
```

## 💻 Kód Részlet

```python
import pandas

# Adatok beolvasása
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250113.csv')

# Mókusok számolása színek szerint
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

# Új adatstruktúra létrehozása
data_dict = {
    "students": ["Gray", "Cinnamon", "Black"],
    "scores": [grey_squirrels_count, cinnamon_squirrels_count, black_squirrels_count],
}

# Eredmények mentése
data = pandas.DataFrame(data_dict)
data.to_csv('squirrels_color.csv')
```

## 📊 Adatstruktúra

### Kimeneti CSV Formátum

| Oszlop    | Leírás                               |
|-----------|--------------------------------------|
| students  | Mókus bundaszíne (Gray/Cinnamon/Black)|
| scores    | Az adott színű mókusok száma         |

## 🤝 Közreműködés

A projekthez való hozzájárulásokat szívesen fogadjuk! Kérjük, kövesse ezeket a lépéseket:

1. Fork-olja a repository-t
2. Hozzon létre egy új branch-et (`git checkout -b feature/ujfunkcio`)
3. Commit-olja a változtatásokat (`git commit -am 'Új funkció hozzáadása'`)
4. Push-olja a branch-et (`git push origin feature/ujfunkcio`)
5. Nyisson egy Pull Request-et

## ✨ Szerző

[Az Ön Neve]

## 📝 Licensz

Ez a projekt [MIT](LICENSE) licensz alatt áll. A részletekért tekintse meg a LICENSE fájlt.

---

<div align="center">
Készült ❤️ és ☕ segítségével

[Jelentsen Hibát](https://github.com/namezor90/repo/issues) · [Kérjen Funkciót](https://github.com/namezor90/repo/issues)
</div>
