from statistics import mean
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

mtk = pd.read_excel("3-mtkrev.xlsx")
print(mtk.head)

print("tabel nilai mtk")
mtk1 = mtk.loc[:, [ 'mtk.nilai', 't2.ket']]
print(mtk1.head())

mtk1['t2.ket'] = pd.to_numeric(mtk1['t2.ket'], errors='coerce')
print(mtk1.head())

mtk1['mtk.nilai'] = pd.to_numeric(mtk1['mtk.nilai'], errors='coerce')


# MENDETEKSI DATA MISSING
print("Deteksi Missing Value")
print(mtk1.isna().sum())

## MENGGANTI DATA MISSING VALUE DENGAN MEAN
print("Penanganan Missing Value 2")
# mtk1['t2.ket'] = np.where(mtk1['t2.ket'] == 'P/L', '0', mtk1['t2.ket'])
# mtk1['t2.ket'] = np.where(mtk1['t2.ket'] == 'P', '1', mtk1['t2.ket'])
# mtk1['t2.ket'] = np.where(mtk1['t2.ket'] == 'TL', '2', mtk1['t2.ket'])

print(mtk1)

print("Deteksi Outlier")
outliers = []

def detect_outlier(mtk1):
    threshold = 3
    mean_value = mtk1.mean()
    std_dev = mtk1.std()

    for x in mtk1:
        z_score = (x - mean_value) / std_dev
        if np.abs(z_score) > threshold:
            outliers.append(x)
    return outliers

# outlier1 = detect_outlier(mtk1['no.ujian'])
# print("Outlier kolom no.ujian : ", outlier1)
# print("Banyak outlier no.ujian : ", len(outlier1))
# print()

outlier2 = detect_outlier(mtk1['mtk.nilai'])
print("Outlier kolom mtk.nilai : ", outlier2)
print("Banyak outlier mtk.nilai : ", len(outlier2))
print()

outlier3 = detect_outlier(mtk1['t2.ket'])
print("Outlier kolom t2.ket : ", outlier3)
print("Banyak outlier t2.ket : ", len(outlier3))
print()

# Penanganan Outlier untuk Mengganti outlier dengan nilai rata-rata (mean)

variabel = ['mtk.nilai']

for var in variabel:
    outlier_datapoints = detect_outlier(mtk1[var])
    print("Outlier ", var, " = ", outlier_datapoints)

for var in variabel:
    outlier_datapoints = detect_outlier(mtk1[var])
    rata = mean(mtk1[var])
    mtk1[var] = mtk1[var].replace(outlier_datapoints, rata)
    
 # Menampilkan data setelah penanganan outlier
print("Data setelah penanganan outlier:")
print(mtk1) 
# print(mtk1.shape)

mtk2 = mtk1.dropna()
print(mtk2)

# Grouping yang dibagi menjadi dua
print("GROUPING VARIABEL".center(100, "="))
x=mtk2.iloc[:,0:1].values
y=mtk2.iloc[:,1].values

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


# Menerima input dari pengguna
# input_no_ujian = input("Masukkan nomor ujian: ")
input_mtk_nilai = float(input("Masukkan nilai Matematika: "))

# Format input sesuai dengan kebutuhan model
input_data = [[ input_mtk_nilai]]

# Prediksi output menggunakan model yang sudah dilatih
hasil_prediksi = svm_model.predict(input_data)

# Tampilkan hasil prediksi kepada pengguna
print("Hasil prediksi untuk input yang diberikan:")
# print("Nomor Ujian:", input_no_ujian120)
print("Nilai Matematika:", input_mtk_nilai)
print("Prediksi Kelas:", hasil_prediksi)


