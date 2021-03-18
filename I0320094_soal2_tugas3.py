print("==== Dictionary Identitas Diri ====")

#Identitas Diri
dictionary = {"Nama":["Sekar Zaneta Amirulputri"],
              "Hobi":["Menonton film","Tidur","Membaca buku"],
              "Sosial Media":["Instagram","Twitter","Line"],
              "Lagu Kesukaan":["Heart-Shaped Box","Fiance","Stockholm Syndrome","Gang Berry"],
              "Makanan Favorit":["Pempek","Dimsum","Tekwan"]}
print(dictionary)

#Mengubah dictionary
dictionary["Hobi"][0]=("Makan")
dictionary["Sosial Media"][2]=("Whatsapp")

#Menghapus salah satu dictionary
del dictionary["Makanan Favorit"][1:3]

#Menambah dictionary
dictionary["Hobi"].append("Mendengarkan lagu")

print(dictionary)