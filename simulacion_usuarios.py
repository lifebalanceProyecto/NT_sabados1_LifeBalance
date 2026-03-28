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

        usuarios.append(usuario)
    
    return usuarios

        