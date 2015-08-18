

class Bodega:

    def __init__(self):
        self.espacio=[]

    def AgregarObjeto(self,objeto):
        self.espacio.append(objeto)
        


class Electronicos:

    lista_electronicos = []
    def __init__(self, Voltaje, Consumo):
        self.Voltaje=Voltaje
        self.Consumo=Consumo
        Electronicos.lista_electronicos.append(self)


class Vestibles:

    lista_vestibles = []
    def __init__(self, Talla, Material):
        self.Talla=Talla
        self.Material=Material
        Vestibles.lista_vestibles.append(self)

class Lujo:
    lista_lujo:
    def __init__(self, Costo):
        self.Costo=Costo
        Lujo.lista_lujo.append(self)

class Ilegal:

    lista_ilegal=[]
    def __init__(self, Alerta):
        self.Alerta=Alerta
        Ilegal.lista_ilegal.append(self)

class Domesticos:
    lista_domesticos=[]

    def __init__(self,Reseña):
        self.Reseña=Reseña
        Domesticos.lista_domesticos.append(self)

class Obras_de_Arte:
    lista_obras = []

    def __init__(self,Nombre,Autor,Año):
        self.Nombre=Nombre
        self.Autor=Autor
        self.Año=Año
        Obras_de_Arte.lista_obras.append(self)

class Comestible:

    def __init__(self, Calorias):
        self.Calorias=Calorias

class Refrigerador(Electronicos, Domesticos):

    def __init__(self, Peso, Volumen, Voltaje, Consumo, Reseña):
        Electronicos.__init__(self,Voltaje,Consumo)
        Domesticos.__init__(self, Reseña)
        self.Peso=Peso
        self.Volumen=Volumen

class Apple_Watch(Electronicos, Lujo):

    def __init__(self, Peso, Volumen, Voltaje, Consumo, Costo):
        Electronicos.__init__(self,Voltaje,Consumo)
        Lujo.__init__(self,Costo)
        self.Peso=Peso
        self.Volumen=Volumen

class Mona_Lisa_Robada(Obras_de_Arte, Ilegal, Lujo):

    def __init__(self, Peso, Volumen, Nombre, Autor, Año, Alerta, Costo):
        Obra_de_Arte.__init__(self, Nombre, Autor, Año)
        Ilegal.__init__(self, Alerta)
        Lujo.__init__(self,Costo)
        self.Peso=Peso
        self.Volumen=Volumen

class Abrigo(Vestible, Lujo, Ilegal):

    def __init__(self, Peso, Volumen, Talla, Material, Costo, Alerta):
        Vestible.__init__(self, Talla, Material)
        Lujo.__init__(self, Costo)
        Ilegal.__init__(self, Alerta)

class Jarron(Lujo, Obras_de_Arte, Domestico):

    def __init__(self, Peso, Volumen, Costo, Nombre, Autor, Año, Reseña):
        Lujo.__init__(self, Costo)
        Obras_de_Arte.__init__(self,Nombre,Autor,Año)
        Domestico.__init__(self, Reseña)
        self.Peso=Peso
        self.Volumen=Volumen

class PapasFritas(Comestible,Domestico):

    def __init__(self, Peso, Volumen, Calorias, Reseña):
        Comestible.__init__(self, Calorias)
        Domestico.__init__(self, Reseña)
        self.Peso=Peso
        self.Volumen=Volumen






        

    
