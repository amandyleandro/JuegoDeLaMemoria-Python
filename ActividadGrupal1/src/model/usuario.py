import json
import os
class usuario(): 

    def __init__(self,username,password,genero = "desconocido", edad = 0,puntos = 0):
            self.username = username
            self.password = password
            self.genero = genero
            self.edad = edad
            self.puntos = puntos

            #self.configuracion = config.buscarConfig(usuario)

    def validarRegister(self,rep_pass):
        error = ""
        if not self.username:
            error += " - usuario vacio \n"
        if not self.password:
            error += " - contraseña vacio\n"
        if self.password != rep_pass:
            error += " - las contraseñas no coinciden\n"
        if self.existeUsuario():
            error += " - el nombre de usuario ya existe\n"
        return error

    def existeUsuario(self):
        try:
            with open("archivos" + os.sep + "arc_usuarios.json", encoding="utf8") as arc_usuarios:
                data_usuarios = json.load(arc_usuarios)
        except:
                data_usuarios= []
        for aux in data_usuarios:
            if self.username in aux:
                user = usuario(
                    self.username,
                    aux[self.username]["password"],
                    aux[self.username]["genero"],
                    aux[self.username]["edad"],
                    aux[self.username]["puntos"]
                    )
                return user
        return False

    def guardarUsuarioJson(self):
        try:
            with open("archivos"+ os.sep +"arc_usuarios.json", encoding="utf8") as arc_usuarios:
                data_usuarios = json.load(arc_usuarios)
        except:
                data_usuarios= []

        with open("archivos"+ os.sep +"arc_usuarios.json", "w", encoding="utf8") as file:
            data = {
                self.username : {
                "password" : self.password,
                "genero" : self.genero,
                "edad" : self.edad,
                "puntos" : self.puntos,
                }
            }
            data_usuarios.append(data)
            json.dump(data_usuarios,file, indent=4, ensure_ascii=False)

    def imprimir(self):
        print(self.username)
        print(self.password)
        print(self.genero)
        print(self.edad)
        print(self.puntos)