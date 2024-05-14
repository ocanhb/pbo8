# -*- coding: utf-8 -*-
"""
Created on Sat Apr 20 09:21:17 2024

@author: ocanh
"""

class MasyarakatKampus:
    def __init__(self, golongan="LAINNYA", gaji=150000):
        self.golongan = golongan
        self.gaji = gaji

    def Gaji(self):
        return self.gaji

    def Penjelasan(self):
        print(f"Golongan {self.golongan} mendapatkan gaji: {self.Gaji()}")

class Dosen(MasyarakatKampus):
    def Gaji(self):
        if self.golongan == "DOSEN":
            return 4500000
        else:
            return self.gaji

class Staff(MasyarakatKampus):
    def Gaji(self):
        if self.golongan == "STAFF":
            return 3500000
        else:
            return self.gaji

# Contoh penggunaan
print("---------")
print("Nama : Hasanul Bashori")
print("Nim : 064002300041")
print("---------")

dosen1 = Dosen("DOSEN")
dosen1.Penjelasan()

staff1 = Staff("STAFF")
staff1.Penjelasan()

lainnya = MasyarakatKampus()
lainnya.Penjelasan()
