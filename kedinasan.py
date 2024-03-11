from statistics import mean
import pandas as pd
import numpy as np

print("tabel formasi")
formasi = pd.read_excel("1-formasi.xlsx")
print(formasi.head(10))

# print("tabel nilai skd")

skd = pd.read_excel("2-skd.xlsx")
# print(skd.head(10))

# print("tabel nilai mtk")

mtk = pd.read_excel("3-mtk.xlsx")
# print(mtk.head(10))

#ngambil atribut

print("tabel nilai skd")
skd1 = skd.loc[:, ['no.peserta', 'skd.twk', 'skd.tiu', 'skd.tkp', 'skd.total', 't1.ket']]
print(skd1.head())

print("tabel nilai mtk")
mtk1 = mtk.loc[:, ['no.ujian', 'mtk.nilai', 't2.ket']]
print(mtk1.head())

mtk1['mtk.nilai'] = pd.to_numeric(mtk1['mtk.nilai'], errors='coerce')
mtk1['t2.ket'] = pd.to_numeric(mtk1['t2.ket'], errors='coerce')
skd1['t1.ket'] = pd.to_numeric(skd1['t1.ket'], errors='coerce')
skd1['no.peserta'] = pd.to_numeric(skd1['no.peserta'], errors='coerce')
skd1['skd.twk'] = pd.to_numeric(skd1['skd.twk'], errors='coerce')
skd1['skd.tiu'] = pd.to_numeric(skd1['skd.tiu'], errors='coerce')
skd1['skd.tkp'] = pd.to_numeric(skd1['skd.tkp'], errors='coerce')
# skd1['skp.total'] = pd.to_numeric(skd1['skp.total'], errors='coerce')





# variableskd = ['skd.twk', 'skd.tiu', 'skd.tkp', 'skp.total']





print("================================================")
# missing value
print("deteksi missing value")
print("================================================")
print(formasi.isna().sum())
print(skd1.isna().sum())
print(mtk1.isna().sum())
print("================================================")

# outlier formasi
print("deteksi outlier formasi")
print("================================================")

outliersformasi = []

def detect_outlier(formasi):
    threshold = 3
    mean_value = formasi.mean()
    std_dev = formasi.std()
    
    for x in formasi:
        z_score = (x - mean_value) / std_dev
        if np.abs(z_score) > threshold:
            outliersformasi.append(x)
    return outliersformasi

#cetak outlier formasi
outliersformasi1 = detect_outlier(formasi['formasi.d3st'])
print("outlier kolom formasi.d3st : ", outliersformasi1)
print("total outlier formasi.d3st : ", len(outliersformasi1))
print()

outliersformasi2 = detect_outlier(formasi['pendaftar.d3st'])
print("outlier kolom pendaftar.d3st : ", outliersformasi2)
print("total outlier pendaftar.d3st : ", len(outliersformasi2))
print()

outliersformasi3 = detect_outlier(formasi['formasi.d4st'])
print("outlier kolom formasi.d4st : ", outliersformasi3)
print("total outlier formasi.d4st : ", len(outliersformasi3))
print()

outliersformasi4 = detect_outlier(formasi['pendaftar.d4st'])
print("outlier kolom pendaftar.d4st : ", outliersformasi4)
print("total outlier pendaftar.d4st : ", len(outliersformasi4))
print()

outliersformasi5 = detect_outlier(formasi['formasi.d4ks'])
print("outlier kolom formasi.d4ks : ", outliersformasi5)
print("total outlier formasi.d4ks : ", len(outliersformasi5))
print()

outliersformasi6 = detect_outlier(formasi['pendaftar.d4ks'])
print("outlier kolom pendaftar.d4ks : ", outliersformasi6)
print("total outlier pendaftar.d4ks : ", len(outliersformasi6))
print()

# outlier skd
print("deteksi outlier skd")
print("================================================")

outliersskd = []

def detect_outlier(skd1):
    threshold = 3 #batas
    mean_value = skd1.mean()
    std_dev = skd1.std()
    
    for x in skd1:
        z_score = (x - mean_value) / std_dev
        if np.abs(z_score) > threshold:
            outliersskd.append(x)
    return outliersskd

# cetak oulier skd

outliersskd1= detect_outlier(skd1['no.peserta'])
print("outlier kolom no peserta : ", outliersskd1)
print("total outlier no peserta : ", len(outliersskd1))
print()

outliersskd2= detect_outlier(skd1['skd.twk'])
print("outlier kolom skd.twk : ", outliersskd2)
print("total outlier skd.twk : ", len(outliersskd2))
print()

outliersskd3= detect_outlier(skd1['skd.tiu'])
print("outlier kolom skd.tiu : ", outliersskd3)
print("total outlier skd.tiu : ", len(outliersskd3))
print()

outliersskd4= detect_outlier(skd1['skd.tkp'])
print("outlier kolom skd.tkp : ", outliersskd4)
print("total outlier skd.tkp : ", len(outliersskd4))
print()

outliersskd5= detect_outlier(skd1['skd.total'])
print("outlier kolom skd.total : ", outliersskd5)
print("total outlier skd.total : ", len(outliersskd5))
print()

outliersskd6= detect_outlier(skd1['t1.ket'])
print("outlier kolom t1.ket : ", outliersskd6)
print("total outlier t1.ket : ", len(outliersskd6))
print()

# outlier mtk
print("deteksi outlier mtk")
print("================================================")

outliersmtk = []

def detect_outlier(mtk1):
    threshold = 3 #batas
    mean_value = mtk1.mean()
    std_dev = mtk1.std()
    
    for x in mtk1:
        z_score = (x - mean_value) / std_dev
        if np.abs(z_score) > threshold:
            outliersmtk.append(x)
    return outliersmtk

outliersmtk1 = detect_outlier(mtk1['no.ujian'])
print("outlier kolom no.ujian : ", outliersmtk1)
print("total outlier no.ujian: ", len(outliersmtk1))
print()

outliersmtk2 = detect_outlier(mtk1['mtk.nilai'])
print("outlier kolom mtk.nilai : ", outliersmtk2)
print("total outlier mtk.nilai: ", len(outliersmtk2))
print()

outliersmtk3 = detect_outlier(mtk1['t2.ket'])
print("outlier kolom t2.ket : ", outliersmtk3)
print("total outlier t2.ket: ", len(outliersmtk3))
print()


print("================================================================")
# penanganan outlier 
variable = ['pendaftar.d4st', 'formasi.d4ks', 'pendaftar.d4ks']
for var in variable:
    outlier_datapoints = detect_outlier(formasi[var])
    print("Outlier ", var, " = ", outlier_datapoints)

# Penanganan Outlier untuk Mengganti outlier dengan nilai rata-rata (mean)
for var in variable:
    outlier_datapoints = detect_outlier(formasi[var])
    rata = mean(formasi[var])
    formasi[var] = formasi[var].replace(outlier_datapoints, rata)
    
# Menampilkan data setelah penanganan outlier
print("Data setelah penanganan outlier:")
print(formasi) 


print("================================================================")
variableskd = ['skd.twk', 'skd.tiu', 'skd.tkp', 'skp.total']



for var in variableskd:
    outlier_datapoints = detect_outlier(variableskd[var])
    print("Outlier ", var, " = ", outlier_datapoints)

for var in variableskd:
    outlier_datapoints = detect_outlier(skd1[var])
    rataskd = mean(skd1[var])
    skd1[var] = skd1[var].replace(outlier_datapoints, rataskd)
    
print(variableskd)

# ku ambil 
# pelatih ph
# dan juga godlane ph
# tapi hasilnya 
# tetap sama saja
# masih tetap 
# papan bawah
# jual tazz
# jual tazz
# milih jungler aura
# dikasih jungler kelas dunia
# milih jungler papan bawah

