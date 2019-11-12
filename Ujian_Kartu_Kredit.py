# Disediakan sebuah file JSON (ccNasabah.json, unduh di sini) berisi data nomor kartu kredit nasabah sebuah bank, 
# yang belum diverifikasi validitas kartu kreditnya. 
# Buatlah sebuah file python (.py) yang dapat membaca file JSON tersebut, 
# kemudian memisahkan antara nasabah dengan nomor kartu kredit valid & invalid, 
# lalu menyimpan hasilnya dalam file JSON yang terpisah (ccValid.json dan ccInvalid.json).

# Adapun kriteria nomor kartu kredit yang valid adalah sebagai berikut:

# Diawali dengan angka 4, 5 atau 6.
# Terdiri atas tepat 16 digit angka.
# Hanya mengandung angka 0-9.
# Boleh dituliskan berupa grup 4 digit yang dipisahkan dengan tanda hubung "-"
# Tidak boleh terdapat 1 angka yang diulang >3x & tertulis secara beruntun, misal: 3333.

import json
import string

nama = []
nomorcc = []
valid = []
invalid = []

with open("ccNasabah.json") as json_file:
    data = json.load(json_file)
    for p in data:
        nama.append(p["nama"])
        nomorcc.append(p["noCreditCard"]) 

abjad  = list(string.ascii_lowercase)

for i in range(len(nomorcc)):
    if nomorcc[i][0] == "4" or nomorcc[i][0] == "5" or nomorcc[i][0] == "6":
        if " " in nomorcc[i] or "." in nomorcc[i]:
            invalid.append(i)
        else:
            if "-" in nomorcc[i]:
                nomorcc[i] = nomorcc[i].split("-")
                for val in nomorcc[i]:
                    if len(val) != 4:
                        invalid.append(i)
                        break
                    else:
                        nomorcc[i] = "".join(nomorcc[i])
                        if len(nomorcc[i]) == 16:
                            for alphabet in abjad:
                                if alphabet in nomorcc[i]:
                                    invalid.append(i)
                                    break
                                else:
                                    for j in range(len(nomorcc[i])):
                                        try:
                                            if (nomorcc[i][j] == nomorcc[i][j+1]):
                                                if (nomorcc[i][j+1] == nomorcc[i][j+2]):
                                                    if (nomorcc[i][j+2] == nomorcc[i][j+3]):
                                                        invalid.append(i)
                                        except IndexError:
                                            pass
                                    pass
                        else:
                            invalid.append(i)
                            break
            else:
                if len(nomorcc[i]) == 16:
                    for alphabet in abjad:
                        if alphabet in nomorcc[i]:
                            invalid.append(i)
                        else:
                            for j in range(len(nomorcc[i])):
                                try:
                                    if (nomorcc[i][j] == nomorcc[i][j+1]):
                                        if (nomorcc[i][j+1] == nomorcc[i][j+2]):
                                            if (nomorcc[i][j+2] == nomorcc[i][j+3]):
                                                invalid.append(i)
                                except IndexError:
                                    pass
                            pass
                else:
                    invalid.append(i)
    else:
        invalid.append(i)

invalid = list(set(invalid))

invalidcc = []

for i in invalid:
    invalidcc.append(nomorcc[i])

print(invalidcc)
    

