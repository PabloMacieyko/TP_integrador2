from datetime import date

class Archivo:
    def __init__(self, nombre, formato):
        self._nombre = nombre
        self._fecha_hoy = date.today()
        self._formato = formato 

    def __str__(self):
        return f"Nombre: {self._nombre}, Fecha{self._fecha_hoy}, Formato: {self._formato}"
