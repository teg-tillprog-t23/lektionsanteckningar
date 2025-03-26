class Kläder:
    def __init__(self, material, färg, storlek):
        self.material = material
        self.färg = färg
        self.storlek = storlek

    def ändra_storlek(self):
        ny_storlek = input("Vilken storlek ska den vara? ")
        self.storlek = ny_storlek


class Mössa(Kläder):
    def __init__(self, material, färg, storlek, tofs):
        super().__init__(material, färg, storlek)
        self.tofs = tofs

ny_mössa = Mössa("stickad", "blå","S",True)
ny_mössa.ändra_storlek()