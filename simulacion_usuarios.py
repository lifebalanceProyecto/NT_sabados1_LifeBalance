from datetime import datetime,timedelta
import random

def simular_usuarios(numeroUsuarios):
    #semilla de datos
    listaNombres=["Camila Gomez","Pedro Perez","Juan Ramirez","David Carvajal","Alexander Ruiz","Julian Cuartas"]

    listaCorreos=["camila123@yopmail","hermoxx123@yopmail.com","bebe@yopmail.com","terreneitor@yopmail.com","cuajo@yopmail.com","alien@yopmail.com"]

    listaPass=["ASD123","DSA47","KRE765","KOF654","KOL000","POP666","KKK898"]
    listaSexo=["femenino","masculino","no binario"]

    fechaInicial=datetime[2025,1,1]

    usuarios=[]


    for _ in range(numeroUsuarios):
        fechaSimulada=fechaInicial+timedelta(days=random.randint(0,365))
        usuario={
            "id":random.randint(20000000,1500000000),
            "nombre":random.choice(listaNombres),
            "correo": random.choice(listaCorreos),
            "contrasena":random.choice(listaPass),
            "sexo":random.choice(listaSexo),
            "fecha_creacion":fechaSimulada.strftime("%Y/%m/%d")
        }

         # 🔥 inyección de errores
        probabilidadError = random.random()

        if probabilidadError < 0.1:
            # IDs inválidos y nombre con espacios
            usuario["id"] = random.choice([None, -1, 0])
            usuario["nombre"] = " " + usuario["nombre"] + " "

        elif probabilidadError < 0.2:
            # correo mal formado
            usuario["correo"] = random.choice([
                "sin_arroba.com",
                "correo@.com",
                "correo@gmail",
                "",
                None
            ])

        elif probabilidadError < 0.3:
            # contraseña débil o vacía
            usuario["contrasena"] = random.choice([
                "123",
                "abc",
                "",
                None
            ])

        elif probabilidadError < 0.4:
            # sexo inválido
            usuario["sexo"] = random.choice([
                "otro",
                "desconocido",
                "",
                None
            ])

        elif probabilidadError < 0.5:
            # fecha nula
            usuario["fecha_creacion"] = None

        elif probabilidadError < 0.6:
            # fecha mal formateada
            usuario["fecha_creacion"] = fechaSimulada.strftime("%d-%m-%Y")

        elif probabilidadError < 0.7:
            # nombre vacío
            usuario["nombre"] = random.choice(["", None])

        elif probabilidadError < 0.85:
            # mezcla de errores
            usuario["id"] = None
            usuario["correo"] = "malcorreo"
            usuario["contrasena"] = "123"


        usuarios.append(usuario)
    
    return usuarios

        