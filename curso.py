import random

class Curso:
    def __init__(self, nombre):
        self._nombre = nombre
        self._contraseña = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(5))
        self.archivos = []
        self.codigo = self.generar_codigo()

    def __str__(self):
        return f"Nombre: {self._nombre}\nCodigo: {self.obtener_codigo()}\nContraseña: {self._contraseña}"

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)
        
    def generar_codigo(self):
        return random.randint(1000, 9999)
    
    def obtener_codigo(self):
        return self.codigo
