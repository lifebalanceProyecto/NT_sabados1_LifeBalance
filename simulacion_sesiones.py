import random

def simular_sesiones(numeroSesiones):
    
    listaNombresSesiones = [
        "Meditacion",
        "Dormir",
        "Estiramientos",
        "Pausas activas",
        "Ejercicio"
    ]

    listaTipo = ["M001", "D100", "E200", "P300", "P400", "E500"]

    listaMinutos = list(range(0, 60, 5))

    sesiones = []

    for _ in range(numeroSesiones):
        sesion = {
            "nombre": random.choice(listaNombresSesiones),
            "tipo": random.choice(listaTipo),
            "duracion_minutos": random.choice(listaMinutos)
        }
        sesiones.append(sesion)

    return sesiones

