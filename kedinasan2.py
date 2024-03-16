from statistics import mean
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

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

# delete data missing value
print("Penanganan Missing Value")
data_cleaned = kedinasan.dropna()
print("Data tanpa missing value")
print(data_cleaned)

#ganti missing value dgn mean
 print("Penanganan Missing Value 2")
data1['blood_glucose_random'].fillna(data1['blood_glucose_random'].mean(), inplace=True)
data1['blood_urea'].fillna(data1['blood_urea'].mean(), inplace=True)
data1['serum_creatinine'].fillna(data1['serum_creatinine'].mean(), inplace=True)
print("Missing data pada blood glucose =", data1['blood_glucose_random'].isna().sum())
print("Missing data pada blood urea =", data1['blood_urea'].isna().sum())
print("Missing data pada serum creatinine =", data1['serum_creatinine'].isna().sum())


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

outliersskd2= detect_outlier(kedinasan['skd.twk'])
print("outlier kolom skd.twk : ", outliersskd2)
print("total outlier skd.twk : ", len(outliersskd2))
print()

outliersskd3= detect_outlier(kedinasan['skd.tiu'])
print("outlier kolom skd.tiu : ", outliersskd3)
print("total outlier skd.tiu : ", len(outliersskd3))
print()

outliersskd4= detect_outlier(kedinasan['skd.tkp'])
print("outlier kolom skd.tkp : ", outliersskd4)
print("total outlier skd.tkp : ", len(outliersskd4))
print()

outliersskd5= detect_outlier(kedinasan['skd.total'])
print("outlier kolom skp.total : ", outliersskd5)
print("total outlier skp.total : ", len(outliersskd5))
print( )

outliersmtk1= detect_outlier(kedinasan['mtk.nilai'])
print("outlier kolom mtk.nilai : ", outliersmtk1)
print("total outlier mtk.nilai : ", len(outliersmtk1))
print( )


# Grouping yang dibagi menjadi dua
print("GROUPING VARIABEL".center(100, "="))
x=kedinasan.iloc[:,0:9].values
y=kedinasan.iloc[:,9].values

# Split data into training and testing
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=100)
print("Instance variabel data training".center(75, "="))
print(x_train)
print("Instance kelas data training".center(75, "="))
print(y_train)
print("Instance variabel data testing".center(75, "="))
print(x_test)
print("Instance kelas data testing".center(75, "="))
print(y_test)
print("============================================================")
print()


# Pemodelan SVM
svm_model = SVC()
svm_model.fit(x_train, y_train)
y_pred_svm = svm_model.predict(x_test)
print("Hasil prediksi SVM".center(75, "="))
print(y_pred_svm)
print("============================================================")
print()

# Evaluasi confusion matrix dan evaluasi akurasi SVM
print("Hasil confusion matrix SVM".center(75, "="))
print(confusion_matrix(y_test, y_pred_svm))
print("Hasil akurasi pemodelan SVM:", accuracy_score(y_test, y_pred_svm))
print("============================================================")
print()


