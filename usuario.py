from abc import ABC, abstractmethod

class Usuario(ABC):
    def __init__(self, nombre, apellido, email, password):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._password = password

    def __str__(self):
        return f"{self._nombre}\n, {self._apellido}\n, {self._email}"

    def validar_credenciales(self, email, password):
        return self._email == email and self._password == password


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, password, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, password)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mi_cursos = []

    def __str__(self):
        return f"Estudiante: {self._nombre} {self._apellido}, Legajo: {self._legajo}, Año de Inscripción: {self._anio_inscripcion_carrera}"

    def matricular_en_curso(self, curso):
        if curso not in self.mi_cursos:
            self.mi_cursos.append(curso)
            return True
        else:
            return False
        
    def desmatricular_del_curso(self, curso):
        if curso in self.mi_cursos:
            self.mi_cursos.remove(curso)
            print(f"Desmatriculación exitosa de {curso._nombre}")
        else:
            print(f"No estás matriculado en {curso._nombre}, por lo que no puedes desmatricularte de él.")
        
class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, password, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, password)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        self.mis_cursos = []

    def __str__(self):
        return f"Profesor: {self._nombre} {self._apellido}, Título: {self._titulo}, Año de Egreso: {self._anio_egreso}"

    def dictar_curso(self, curso):
        self.mis_cursos.append(curso)
