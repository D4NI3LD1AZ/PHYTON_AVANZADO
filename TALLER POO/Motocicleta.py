class Motocicleta:

    def __init__(self, color, matricula, combustible_litros, numero_ruedas, marca, modelo, fecha_creacion, velocidad_punta, peso, motor = False, estado = "Nuevo") -> None:
        self.color = color
        self.matricula = matricula
        self.combustible_litros = combustible_litros
        self.numero_ruedas = numero_ruedas
        self.marca = marca
        self.modelo = modelo
        self.fecha_creacion = fecha_creacion
        self.velocidad_punta = velocidad_punta    
        self.peso = peso
        self.motor = motor
        self.estado = estado
    
    def getMotor(self):
        return self.motor
    
    def setMotor(self, motor):
        self.motor = motor

    def setEstado(self, motor):
        self.motor = motor

    def getEstado(self):
        return self.estado
    
    def setEstado(self, estado):
        self.estado = estado

    def arrancar(self):
        if self.motor:
            print("El motor ya estaba en marcha")
        else:
            self.motor = True
            print("El motor ha arrancado.")
    def detener(self):
        if not self.motor:
            print("El motor ya estaba detenido")
        else:
            self.motor == False
            print("El motor se ha detenido")

moto = Motocicleta(color="Negro", matricula="H3450", combustible_litros=20, numero_ruedas=4, marca="HONDA", modelo="2022", fecha_creacion="2022-03-19", velocidad_punta="75KM", peso="30KG")
print(moto.getEstado())
print(moto.getMotor())
moto.detener()
moto.arrancar()
moto.detener()

