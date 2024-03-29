class Asiento:
    def __init__(self,color, precio, registro):
        self.color = color
        self.precio= precio
        self.registro= registro
    
    def cambiarColor(self,color):
        colores=["rojo", "verde","amarillo","negro","blanco"]
        if color in colores:
            self.color= color

class Auto:
    cantidadCreados= 0
    def __init__(self,modelo, precio,marca, motor, registro,asientos):
        self.modelo= modelo
        self.precio= precio
        self.asientos = asientos
        self.marca= marca
        self.motor= motor
        self.registro= registro

    def cantidadAsientos(self):
        numero_asientos=0
        for elemento in self.asientos:
            if elemento != None:
                numero_asientos += 1
        return numero_asientos

    def verificarIntegridad(self):
        if self.registro == self.motor.registro:
            for i in self.asientos:
                if i!= None and i.registro!= self.registro:
                    return "Las piezas no son originales"
                else:
                    "Auto original"
        else:
            "Auto original"

class Motor:
    def __init__(self, numeroCilindros,tipo, registro):
        self.numeroCilindros=numeroCilindros
        self.tipo= tipo
        self.registro= registro

    def cambiarRegistro(self,registro):
        self.registro= registro

    def asignarTipo(self, tipo):
        if tipo == "electrico" or tipo == "gasolina":
            self.tipo= tipo

