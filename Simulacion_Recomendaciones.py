from datetime import datetime, timedelta
import random

def simulacion_recomendaciones():

    lista_recomendaciones = [
        "Recomendación 1: Mantén una dieta equilibrada y saludable.",
        "Recomendación 2: Realiza ejercicio regularmente para mantener un estilo de vida activo.",
        "Recomendación 3: Duerme al menos 7-8 horas por noche para asegurar un buen descanso.",
        "Recomendación 4: Bebe suficiente agua para mantener tu cuerpo hidratado.",
        "Recomendación 5: Evita el consumo excesivo de alcohol y tabaco para proteger tu salud."
    ]

    listaCodigo = ["RO1", "RO2", "RO3", "RO4", "RO5"]

    fechainicial = datetime(2025, 1, 1)

    recomendaciones = []

    # número de registros a generar (puedes cambiarlo)
    for _ in range(10):
        fechasimulada = fechainicial + timedelta(days=random.randint(0, 365))

        recomendacion = {
            "id": random.randint(1, 500),
            "usuario_id": f"Usuario{random.randint(1, 100)}",
            "sesion_id": f"Sesion{random.randint(1, 100)}",
            "motivo": random.choice(["Salud", "Bienestar", "Ejercicio", "Dieta", "Descanso"]),
            "lista_recomendaciones": random.choice(lista_recomendaciones),
            "codigo_recomendacion": random.choice(listaCodigo),
            "fecha": fechasimulada.strftime("%Y-%m-%d")
        }

        recomendaciones.append(recomendacion)

    return recomendaciones