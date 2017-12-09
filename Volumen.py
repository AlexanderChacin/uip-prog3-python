


class sphere(object):
    def __init__(self, r):
        self.radius = r
        self.volume = 0

    def vol(self):
        r = self.radius
        self.volume = (4 / 3) * 3.14 * (r *r *r )
        return self.volume


class Cone(object):
    def __init__(self, r, h):
        self.radius = r
        self.altitude = h
        self.volume = 0

    def vol(self):
        r = self.radius
        h = self.altitude
        self.volume = (1 / 3) * 3.14 * (r * r) * h
        return self.volume

class cylinder(object):
    def __init__(self, r, h):
        self.radius = r
        self.altitude = h
        self.volume = 0


    def vol(self):
        r = self.radius
        h = self.altitude
        self.volume = 3.14 * (r * r) * h
        return self.volume

if __name__ == '__main__':
    o = 'si'

    while o == "si" :

        opc = input("Que figura vamos a usar? (cilindro, cono, esfera) ").lower()
        if opc == "esfera":
            r = int(input("Cual es el radio de la esfera: "))
            x = sphere(r)
            print("Cual es el volumen de la esfera es: ", x.vol())
        elif opc == "cono":
            r = int(input("Cual es el radio de el cono: "))
            h = int(input("Cual es la altura de el cono: "))
            y = Cone(r, h)
            print("El volumen de el cono es: ", y.vol())
        elif opc == "cilindro":
            r = int(input("Cual es el radio del cilindro?: "))
            h = int(input("Cual es la altura de el cilindro: "))
            z = cylinder(r, h)
            print("El volumen de el cilindro es: ", z.vol())
        else:
            print("Figura no encontrada")

        o = input("Desea continuar? si o no: ")