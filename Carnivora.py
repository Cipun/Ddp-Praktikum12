from Animal import Animal

class Carnivora(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, taring, cakar):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.taring = taring
        self.cakar = cakar

    def info_berburu(self):
        super().info_animal(),
        print("Taring \t\t\t\t : ", self.taring,
              "\nCakar \t\t\t\t : ", self.cakar)


singa = Carnivora("Singa", "Daging", "Darat", "Melahirkan", "Taring Panjang", "Cakar Tajam")
singa.info_berburu()
print("==================================")
serigala = Carnivora("Serigala", "Hewan", "Darat", "Melahirkan", "Taring Panjang", "Cakar Tajam")
serigala.info_berburu()
print("==================================")
elang = Carnivora("Elang", "Daging", "Udara", "Bertelur", "Taring Panjang", "Cakar Tajam")
elang.info_berburu()