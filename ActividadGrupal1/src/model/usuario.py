import json
import os
from src.model.configuracion import configuracion

dir_carp = "Archivos"
dir_arch = "arc_usuarios.json"
carpeta = os.path.join(os.getcwd(), dir_carp)

class usuario(configuracion): 

    def __init__(self,username,password,genero = "desconocido", edad = 0,puntos = 0):
            self.username = username
            self.password = password
            self.genero = genero
            self.edad = edad
            self.puntos = puntos
            configuracion.__init__(self)

    def getUserName(self):
        """Esta función retorna el nombre de usuario"""
        return self.username

    def validarRegister(self,rep_pass):
        """Esta función valida si alguno de los parámetros está vacío o si son erróneos"""
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
        """Esta función guarda en data_usuarios lo que se encuentra en el archivo json de usuarios, luego
        verifica si el usuario actual se encuentra en la estructura de datos, de ser así lo devuelve, si no, 
        devuelve falso"""
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
        """Esta función abre el archivo json donde se encuentran guardadas las configuraciones
        y devuelve en data_usuarios la estructura allí guardada, en caso de no haber nada en
        el archivo, crea un nuevo diccionario. Luego modifica la estructura recibida y 
        sobrescribe el archivo."""
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
        """Esta función imprime los valores de las variables de clase"""
        self.imprimirConfig()
        print(self.username)
        print(self.password)
        print(self.genero)
        print(self.edad)
        print(self.puntos)