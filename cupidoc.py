def calcular_ddc(edad: int, peso_kg: float, creatinina_mg_dl: float, es_mujer: int) -> float:
    """
    Calcula la depuración de creatinina (DDC).

    Parámetros:
        edad (int): Edad de la persona en años.
        peso_kg (float): Peso corporal en kilogramos.
        creatinina_mg_dl (float): Nivel de creatinina en sangre en mg/dL.
        es_mujer (int): 1 si es mujer, 0 si es hombre.

    Retorno:
        float: DDC, redondeado a dos decimales.
    """
    ajuste = 0.85 + (1 - es_mujer) * 0.15
    ddc = ((140 - edad) * peso_kg) / (72 * creatinina_mg_dl) * ajuste
    return round(ddc, 2)

print(calcular_ddc(40, 70, 1.0, 0)) 