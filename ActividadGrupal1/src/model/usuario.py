import json
import os
from src.model import configuracion

dir_carp = "Archivos"
dir_arch = "arc_usuarios.json"
carpeta = os.path.join(os.getcwd(), dir_carp)

class usuario(): 

    def __init__(self,username,password,genero = "desconocido", edad = 0,puntos = 0):
            self.username = username
            self.password = password
            self.genero = genero
            self.edad = edad
            self.puntos = puntos
            config = configuracion.configuracion(self.username)
            self.configuracion = config.buscarConfig()

    def validarRegister(self,rep_pass):
        error = ""
        if not self.username:
            error += " - Usuario vacío \n"
        if not self.password:
            error += " - Contraseña vacía\n"
        if self.password != rep_pass:
            error += " - Las contraseñas no coinciden\n"
        if self.existeUsuario():
            error += " - El nombre de usuario ya existe\n"
        return error

    def existeUsuario(self):
        try:
            with open(os.path.join(carpeta, dir_arch), "r", encoding="utf8") as arc_usuarios:

                data_usuarios = json.load(arc_usuarios)
        except:
                data_usuarios= {}
        if self.username in data_usuarios:
            user = usuario(
                self.username,
                data_usuarios[self.username]["password"],
                data_usuarios[self.username]["genero"],
                data_usuarios[self.username]["edad"],
                data_usuarios[self.username]["puntos"]
                )
            return user
        return False

    def guardarUsuarioJson(self):
        try:
            with open(os.path.join(carpeta, dir_arch), "r", encoding="utf8") as arc_usuarios:

                data_usuarios = json.load(arc_usuarios)
        except:
                data_usuarios= {}
        with open(os.path.join(carpeta, dir_arch), "w", encoding="utf8") as file:
            data_usuarios[self.username] = {
                "password" : self.password,
                "genero" : self.genero,
                "edad" : self.edad,
                "puntos" : self.puntos,
                }
            json.dump(data_usuarios,file, indent=4, ensure_ascii=False)

    def imprimir(self):
        print(self.username)
        print(self.password)
        print(self.genero)
        print(self.edad)
        print(self.puntos)