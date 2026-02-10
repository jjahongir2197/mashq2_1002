class Talaba:
    def __init__(self, ism, familiya):
        self.ism = ism
        self.familiya = familiya
        self.baholar = []

    def baho_qoshish(self, baho):
        if 0 <= baho <= 100:
            self.baholar.append(baho)
        else:
            print("Baho 0-100 oralig'ida bo'lishi kerak!")

    def orta_baho(self):
        if len(self.baholar) == 0:
            return 0
        return sum(self.baholar) / len(self.baholar)

    def info(self):
        print(f"\nTalaba: {self.ism} {self.familiya}")
        print(f"Baholar: {self.baholar}")
        print(f"O'rtacha baho: {self.orta_baho():.2f}")


t1 = Talaba("Jahongir", "Jumaboyev")

t1.baho_qoshish(90)
t1.baho_qoshish(85)
t1.baho_qoshish(88)

t1.info()
