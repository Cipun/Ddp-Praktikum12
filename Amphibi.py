from Animal import Animal

# setiap class child itu memiliki 2 properti dan method
class Amphibi(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal(),
        print("Jenis Air \t\t\t : ", self.jenis_air,
              "\nBernapas \t\t\t : ", self.bernapas)
        
amphibi = Amphibi("Katak", "Serangga", "Dua alam", "Bertelur", "Air Tawar", "Kulit dan Paru-paru")
amphibi.info_amphibi()
print("==================================")
amphibi = Amphibi("Axolotl", "Serangga", "Danau", "Bertelur", "Air Tawar", "Insang dan Paru-paru")
amphibi.info_amphibi()
print("==================================")
amphibi3 = Amphibi("Kadal Air", "Serangga", "Dua alam", "Bertelur", "Air Tawar", "Paru-paru, Kulit dan Rongga mulut")
amphibi3.info_amphibi()