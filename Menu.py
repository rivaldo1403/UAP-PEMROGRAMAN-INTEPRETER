import os
import PkgGunungAPI

#menu utama
def menu(): 
  gung = PkgGunungAPI.superGunungApi.superGunungApi() #deklarasi nama object dari class gunungApi
  os.system('cls') #menghapus layar
  #tampilan menu utama
  print("Menu Utama") 
  print("1. Menampilkan Data")
  print("2. Search")
  print("3. Filter")
  print("9. Exit")
  pilih = eval(input("Masukan Pilihan : "))
