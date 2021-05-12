
import json
import os
class configuracion():

    def __init__(self,username,textos = "", cant_casillas = "8x8", coincidencias = 2, tiempo = 120, estilo = "Predeterminado", tipo_elementos = "Ambos", ayudas = "No"):
        self.username = username
        self.textos = textos
        self.cant_casillas = cant_casillas
        self.coicidencias = coincidencias
        self.tiempo = tiempo
        self.estilo = estilo
        self.tipo_elementos = tipo_elementos
        self.ayudas = ayudas
        
    def guardarJson(self):
        try:
            with open("Archivos"+ os.sep +"arc_configuracion.json","r", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion= {}
        with open("Archivos"+ os.sep +"arc_configuracion.json", "w", encoding="utf8") as file:
            data_configuracion[self.username] = {
                "textos" : self.textos,
                "cant_casillas" : self.cant_casillas,
                "coincidencias" : self.coicidencias,
                "tiempo" : self.tiempo,
                "estilo" : self.estilo,
                "tipo_elementos" : self.tipo_elementos,
                "ayudas" : self.ayudas,
                }
            json.dump(data_configuracion,file, indent=4, ensure_ascii=False)

    def buscarConfig(self):
        try:
            with open("Archivos"+ os.sep +"arc_configuracion.json", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion = {}
        if self.username in data_configuracion:
            self = configuracion(
                self.username,
                data_configuracion[self.username]["textos"],
                data_configuracion[self.username]["cant_casillas"],
                data_configuracion[self.username]["coincidencias"],
                data_configuracion[self.username]["tiempo"],
                data_configuracion[self.username]["estilo"],
                data_configuracion[self.username]["tipo_elementos"],
                data_configuracion[self.username]["ayudas"]
                )
        return self
    # def imprimir(self):
    #     print(self.username)
    #     print(self.cant_casillas)
    #     print(self.coicidencias)
    #     print(self.tipo_elementos)
    #     print(self.estilo)
    #     print(self.tiempo)
    #     print(self.textos)
