class Quiz:
    def __init__(self, intrebare, r1, r2, r3, r_corect, punctaj):
        self.intrebare = intrebare
        self.r1 = r1
        self.r2 = r2
        self.r3 = r3
        self.r_corect = r_corect
        self.punctaj = punctaj

    def get_intrebare(self):
        return self.intrebare

    def get_r1(self):
        return self.r1

    def get_r2(self):
        return self.r2

    def get_r3(self):
        return self.r3

    def get_r_corect(self):
        return self.r_corect

    def get_punctaj(self):
        return self.punctaj
