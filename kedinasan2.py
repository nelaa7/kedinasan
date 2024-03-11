from statistics import mean
import pandas as pd
import numpy as np

formasi = pd.read_excel("1-formasi.xlsx")
skd = pd.read_excel("2-skd.xlsx")
mtk = pd.read_excel("3-mtk.xlsx")

# data_merge =  formasi._append(skd, ignore_index=True)

data_merge =  pd.concat([formasi,skd,mtk], ignore_index=True)
print(data_merge)

# atribut
kedinasan = data_merge.loc[:, ['lokasi.formasi','formasi.d3st', 'pendaftar.d3st','formasi.d4st',
                               'pendaftar.d4st','formasi.d4ks','pendaftar.d4ks','no.peserta', 'skd.twk',
                               'skd.tiu', 'skd.tkp', 'skd.total', 't1.ket', 'no.ujian', 'mtk.nilai', 't2.ket']]

kedinasan['lokasi.formasi'] = pd.to_numeric(kedinasan['lokasi.formasi'], errors='coerce')

print(kedinasan.head())

print("================================================")
# missing value
print("deteksi missing value")
print("================================================")
print(kedinasan.isna().sum())
print("================================================")

# outlier formasi
print("deteksi outlier formasi")
print("================================================")

outliers = []

def detect_outlier(kedinasan):
    threshold = 3
    mean_value = kedinasan.mean()
    std_dev = kedinasan.std()
    
    for x in kedinasan:
        z_score = (x - mean_value) / std_dev
        if np.abs(z_score) > threshold:
            outliers.append(x)
    return outliers

outliers1 = detect_outlier(kedinasan['formasi.d3st'])
print("outlier kolom formasi.d3st : ", outliers1)
print("total outlier formasi.d3st : ", len(outliers1))
print()

outliers2 = detect_outlier(kedinasan['pendaftar.d3st'])
print("outlier kolom pendaftar.d3st : ", outliers2)
print("total outlier pendaftar.d3st : ", len(outliers2))
print()

outliers3 = detect_outlier(kedinasan['formasi.d4st'])
print("outlier kolom formasi.d4st : ", outliers3)
print("total outlier formasi.d4st : ", len(outliers3))
print()

outliers4 = detect_outlier(kedinasan['pendaftar.d4st'])
print("outlier kolom pendaftar.d4st : ", outliers4)
print("total outlier pendaftar.d4st : ", len(outliers4))
print()

outliers5 = detect_outlier(kedinasan['formasi.d4ks'])
print("outlier kolom formasi.d4ks : ", outliers5)
print("total outlier formasi.d4ks : ", len(outliers5))
print()

outliers6= detect_outlier(kedinasan['no.peserta'])
print("outlier kolom no peserta : ", outliers6)
print("total outlier no peserta : ", len(outliers6))
print()

outliersskd2= detect_outlier(skd1['skd.twk'])
print("outlier kolom skd.twk : ", outliersskd2)
print("total outlier skd.twk : ", len(outliersskd2))
print()


