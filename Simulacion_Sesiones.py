import random

def simular_sesiones(numeroSesiones):
    

    listaNombres=["Meditacion para dormir","Respiracion","Pausa Activa Oficina","Estiramiento"]
    listaTipo=["Meditacion","Respiracion","Pausa","Estiramiento"]
    listaMinutos=[5,10,15,20]

    sesiones=[]

    for _ in range(numeroSesiones):
        sesion={
            "id":random.randint(1,100),
            "nombre":random.choice(listaNombres),
            "tipo":random.choice(listaTipo),
            "duracion":random.choice(listaMinutos)
        }
        sesiones.append(sesion)
    
    return sesiones
