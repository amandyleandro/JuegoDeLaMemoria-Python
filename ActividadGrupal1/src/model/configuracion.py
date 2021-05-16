from abc import abstractmethod, ABC
import json
import os

dir_carp = "Archivos"
dir_arch = "arc_configuracion.json"
carpeta = os.path.join(os.getcwd(), dir_carp)

text = {"Comienzo": "Ahora comienza la partida",
        "Gano": "¡Ganaste!",
        "Perdio":"¡Perdiste!",
        "Quedan 30 segundos": "¡Quedan 30 segundos!"}

class configuracion():
    def __init__(self,textos = text, cant_casillas = "8x8", coincidencias = 2, tiempo = 120, estilo = "Predeterminado", tipo_elementos = "Ambos", ayudas = "No"):
        self.textos = textos
        self.cant_casillas = cant_casillas
        self.coincidencias = coincidencias
        self.tiempo = tiempo
        self.estilo = estilo
        self.tipo_elementos = tipo_elementos
        self.ayudas = ayudas
    @abstractmethod        
    def getUserName(self):
        raise NotImplementedError
    def guardarJson(self, username):
        #username = self.getUserName()
        try:
            with open(os.path.join(carpeta, dir_arch), "r", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion= {}
        with open(os.path.join(carpeta, dir_arch), "w", encoding="utf8") as file:
            data_configuracion[username] = {
                "textos" : self.textos,
                "cant_casillas" : self.cant_casillas,
                "coincidencias" : self.coincidencias,
                "tiempo" : self.tiempo,
                "estilo" : self.estilo,
                "tipo_elementos" : self.tipo_elementos,
                "ayudas" : self.ayudas,
                }   
            json.dump(data_configuracion,file, indent=4, ensure_ascii=False)

    def buscarConfig(self, username):
        #username = self.getUserName()
        try:
            with open(os.path.join(carpeta, dir_arch), "r", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion = {}
        if username in data_configuracion:
            self = configuracion(
                data_configuracion[self.username]["textos"],
                data_configuracion[self.username]["cant_casillas"],
                data_configuracion[self.username]["coincidencias"],
                data_configuracion[self.username]["tiempo"],
                data_configuracion[self.username]["estilo"],
                data_configuracion[self.username]["tipo_elementos"],
                data_configuracion[self.username]["ayudas"]
                )
        return self
    
    def setConfig(self,conf):
        self.textos = conf.textos
        self.cant_casillas = conf.cant_casillas
        self.coincidencias = conf.coincidencias
        self.tiempo = conf.tiempo
        self.estilo = conf.estilo
        self.tipo_elementos = conf.tipo_elementos
        self.ayudas = conf.ayudas
    
    def imprimirConfig(self):
        print(self.cant_casillas)
        print(self.coincidencias)
        print(self.tipo_elementos)
        print(self.estilo)
        print(self.tiempo)
        print(self.textos)
