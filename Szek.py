class Szek:
    def __init__(self, szin:str, labszam:int):
        self.szin = szin
        self.labszam = labszam

    def __str__(self):
        return (f"Szín: {self.szin}, lábszám: {self.labszam}")