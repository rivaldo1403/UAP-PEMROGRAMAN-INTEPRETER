import json, requests, os, Menu

#superclass dari class subGunungApi
class superGunungApi:
  gunung = requests.get("https://indonesia-public-static-api.vercel.app/api/volcanoes")
  gunungSukses = gunung.json()
  #menu 1, tampilkan data---------------------------------------------#
  def show(self): 
    nomor = 0
    for i in self.gunungSukses:
      nomor = nomor+1
      #tampilan
      print("""
      {5}. Gunung {0}
      Bentuk                     : {1}
      Tinggi                     : {2}
      Estimasi letusan terakhir  : {3}
      Geolokasi                  : {4}
      """.format(i["nama"],i['bentuk'],i['tinggi_meter'],i['estimasi_letusan_terakhir'],i['geolokasi'],nomor))
    jeda = input("Tekan enter untuk melanjutkan")
    Menu.menu()
  #menu 2, cari data bedasarkan nama gunung---------------------------#
  def search(self): 
    namaGunung = input("Masukan Pilihan Nama Gunung : ")
    kondisi = False
    gung = superGunungApi()
    #-----------------------------------------------------------------#
    def pilihan2():
      jeda = input("Apakah anda ingin kembali ke menu utama? (y/n)")
      if jeda == 'y':
        Menu.menu()
      elif jeda == 'n':
        gung.search()
        print()
      else:
        pilihan2()
    #-----------------------------------------------------------------#
    def pilihan():     
      jeda = input("Apakah anda ingin mengeprint data ini? (y/n)")
      if jeda == 'y':
        bikinFile = open("Print_data_gunung_api.txt","a")
        bikinFile.write("""
        Nama Gunung               : {0}
        Bentuk Gunung             : {1}
        Tinggi Gunung             : {2}
        Estimasi Letusan Terakhir : {3}
        Geolokasi                 : {4}
        """.format(i["nama"],i["bentuk"],i["tinggi_meter"],i["estimasi_letusan_terakhir"],i["geolokasi"]))
        print("File berhasil di print!")
        jeda = input()