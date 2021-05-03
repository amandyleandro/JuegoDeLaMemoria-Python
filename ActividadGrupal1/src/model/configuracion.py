
class configuracion():

    def __init__(self,usuario,tema = "", cant_casillas = 0, tiempo = 120, estilo = "t1",ayudas = 0):
        self.usuario = usuario,
        self.tema = tema,
        self.cant_casillas = cant_casillas,
        self.tiempo = tiempo,
        self.estilo = estilo,
        self.ayudas = ayudas,
        
    def guardarJson(self):
        return print ("guardar json")

    def buscarConfig(self):
        return print("buscar config")