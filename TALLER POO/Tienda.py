from Motocicleta import *
class Tienda(Motocicleta):
    def __init__(self,color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso,precio,motor=False):
        super().__init__(color,matricula,combustible_litros,numero_ruedas,marca,modelo,fecha_fabricacion,velocidad_punta,peso,motor)
        self.__precio=precio
    
    def getMarca(self):
        return self.marca
    
    def setMarca(self, marca):
        self.marca = marca
    
    def getModelo(self):
        return self.modelo
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getPrecio(self):
        return self.__precio
       
    def setPrecio(self,precio):
        self.__precio=precio

    def getDescripcion(self):
        return "El precio de la motocicleta " + self.getMarca() +" "+ self.getModelo() + " es de " + str(self.getPrecio())
       
moto3 = Tienda("Azul","d54110","75 litros","3","LEGACY","2020","2012","250 km/h","35k",380000)
print(moto3.getDescripcion())


