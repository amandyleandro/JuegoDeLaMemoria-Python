
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
                data_configuracion= []
        data = {
                self.username : {
                "textos" : self.textos,
                "cant_casillas" : self.cant_casillas,
                "coincidencias" : self.coicidencias,
                "tiempo" : self.tiempo,
                "estilo" : self.estilo,
                "tipo_elementos" : self.tipo_elementos,
                "ayudas" : self.ayudas,
                }
            }
        with open("Archivos"+ os.sep +"arc_configuracion.json", "w", encoding="utf8") as file:
            i = 0
            while(i<len(data_configuracion) and self.username not in data_configuracion[i]):
                i = i + 1
            if i < len(data_configuracion):
                data_configuracion[i] = data
            else:
                data_configuracion.append(data)
            json.dump(data_configuracion,file, indent=4, ensure_ascii=False)

    def buscarConfig(self):
        try:
            with open("Archivos"+ os.sep +"arc_configuracion.json", encoding="utf8") as arc_configuracion:
                data_configuracion = json.load(arc_configuracion)
        except:
                data_configuracion = []
        for aux in data_configuracion:
            if self.username in aux:
                self = configuracion(
                    self.username,
                    aux[self.username]["textos"],
                    aux[self.username]["cant_casillas"],
                    aux[self.username]["coincidencias"],
                    aux[self.username]["tiempo"],
                    aux[self.username]["estilo"],
                    aux[self.username]["tipo_elementos"],
                    aux[self.username]["ayudas"]
                    )
        return self
    def imprimir(self):
        print(self.username)
        print(self.cant_casillas)
        print(self.coicidencias)
        print(self.tipo_elementos)
        print(self.estilo)
        print(self.tiempo)
        print(self.textos)
