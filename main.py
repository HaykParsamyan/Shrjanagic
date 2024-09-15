import math

class Shrjanagic:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def makeres(self):

        makeres = math.pi  * self.r**2

        return makeres

    def paragic(self):

        paragic = 2 * math.pi * self.r

        return paragic

    def hatum(self, Shrjanagic2):

        r_gumar = self.r + Shrjanagic2.r

        d = math.sqrt((Shrjanagic2.x - self.x)**2 + (Shrjanagic2.y - self.y)**2)

        if r_gumar > d:
            return 'uni 2 hatum'
        elif r_gumar == d:
            return 'uni 1 hatum'
        else:
            return 'chuni hatum'

a = Shrjanagic(0, 0, 2)
b = Shrjanagic(4, 0, 1)
print(a.paragic())

print(a.makeres())

print(a.hatum(b))





