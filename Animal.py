# Buat class animal sebagai parent class. class animal mempunyai properti 4 properti (name, makanan, hidup, berkembang biak)

class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print("Nama Hewan \t\t\t : ", self.name,
              "\nMakanan \t\t\t : ", self.makanan,
              "\nHidup \t\t\t\t : ", self.hidup,
              "\nBerkembang Biak \t\t : ", self.berkembang_biak)


# hewan = Animal("Kucing Garong", "Cimol", "Udara", "Bertelur")
# hewan.info_animal()

# buat animal 3 class child (Amphibi, Mamalia, Carnivora, dll) setiapclass child itu memiliki 2 properti dan method
# buat 3 objek dari masing masing class