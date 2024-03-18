from statistics import mean
import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import preprocessing
from sklearn import utils
from sklearn.svm import SVR

skd = pd.read_excel("2-skdrevv.xlsx")
print(skd.head)

print("tabel nilai skd")
skd1 = skd.loc[:, [ 'skd.twk', 'skd.tiu', 'skd.tkp', 't1.ket']]
print(skd1.head())

skd1['skd.tiu'] = pd.to_numeric(skd1['skd.tiu'], errors='coerce')
print(skd1.head())

skd1['skd.twk'] = pd.to_numeric(skd1['skd.twk'], errors='coerce')


# MENDETEKSI DATA MISSING
print("Deteksi Missing Value")
print(skd1.isna().sum())

## MENGGANTI DATA MISSING VALUE DENGAN MEAN
print("Penanganan Missing Value 2")
# skd1['skd.tiu'] = np.where(skd1['skd.tiu'] == 'P/L', '0', skd1['skd.tiu'])
# skd1['skd.tiu'] = np.where(skd1['skd.tiu'] == 'P', '1', skd1['skd.tiu'])
# skd1['skd.tiu'] = np.where(skd1['skd.tiu'] == 'TL', '2', skd1['skd.tiu'])

print(skd1)

print("Deteksi Outlier")
outliers = []

def detect_outlier(skd1):
    threshold = 3
    mean_value = skd1.mean()
    std_dev = skd1.std()

    for x in skd1:
        z_score = (x - mean_value) / std_dev
        if np.abs(z_score) > threshold:
            outliers.append(x)
    return outliers

# outlier1 = detect_outlier(skd1['no.ujian'])
# print("Outlier kolom no.ujian : ", outlier1)
# print("Banyak outlier no.ujian : ", len(outlier1))
# print()

outlier1 = detect_outlier(skd1['skd.twk'])
print("Outlier kolom skd.twk : ", outlier1)
print("Banyak outlier skd.twk : ", len(outlier1))
print()

outlier2 = detect_outlier(skd1['skd.tiu'])
print("Outlier kolom skd.tiu : ", outlier2)
print("Banyak outlier skd.tiu : ", len(outlier2))
print()

outlier3 = detect_outlier(skd1['skd.tkp'])
print("Outlier kolom skd.tkp : ", outlier3)
print("Banyak outlier skd.tkp : ", len(outlier3))
print()

# Penanganan Outlier untuk Mengganti outlier dengan nilai rata-rata (mean)

variabel = ['skd.twk', 'skd.tiu', 'skd.tkp', 't1.ket']

for var in variabel:
    outlier_datapoints = detect_outlier(skd1[var])
    print("Outlier ", var, " = ", outlier_datapoints)

for var in variabel:
    outlier_datapoints = detect_outlier(skd1[var])
    rata = mean(skd1[var])
    skd1[var] = skd1[var].replace(outlier_datapoints, rata)
    
 # Menampilkan data setelah penanganan outlier
print("Data setelah penanganan outlier:")
print(skd1) 
# print(skd1.shape)

skd2 = skd1.dropna()
print(skd2)

# Grouping yang dibagi menjadi dua
print("GROUPING VARIABEL".center(100, "="))
# x=skd2.iloc[:,0:3].values
# y=skd2.iloc[:,3].values

x = skd2[['skd.twk', 'skd.tiu', 'skd.tkp']].values
y = skd2['t1.ket'].values

#convert y values to categorical values
lab = preprocessing.LabelEncoder()
y_transformed = lab.fit_transform(y)


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
svm_model = SVR()
svm_model.fit(x_train, y_train)
y_pred_svm = svm_model.predict(x_test)
print("Hasil prediksi SVM".center(75, "="))
print(y_pred_svm)
print("============================================================")
print()



# Menerima input dari pengguna
# input_no_ujian = input("Masukkan nomor ujian: ")
input_skd_twk = float(input("Masukkan nilai skd twk: "))
input_skd_tiu = float(input("Masukkan nilai skd tiu: "))
input_skd_tkp = float(input("Masukkan nilai skd tkp: "))



# Format input sesuai dengan kebutuhan model
input_data = [[ input_skd_twk, input_skd_tiu, input_skd_tkp]]

# Prediksi output menggunakan model yang sudah dilatih
hasil_prediksi = svm_model.predict(input_data)

# Tampilkan hasil prediksi kepada pengguna
print("Hasil prediksi untuk input yang diberikan:")
# print("Nomor Ujian:", input_no_ujian120)
print("Nilai skd twk:", input_skd_twk)
print("Nilai skd tiu:", input_skd_tiu)
print("Nilai skd tkp:", input_skd_tkp)
print("Prediksi lolos:", hasil_prediksi)

# print(skd2['t1.ket'].all)


