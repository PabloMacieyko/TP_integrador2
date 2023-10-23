from abc import ABC, abstractmethod
import random


class Usuario(ABC):
    def __init__(self, nombre, apellido, email, password):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.password = password

    def __str__(self):
        return self.email

    def validar_credenciales(self, email, password):
        return self.email == email and self.password == password


class Estudiante(Usuario):
    def __init__(self, nombre, apellido, email, password, legajo, anio_inscripcion_carrera):
        super().__init__(nombre, apellido, email, password)
        self.nombre = nombre
        self.apellido = apellido
        self.legajo = legajo
        self.anio_inscripcion_carrera = anio_inscripcion_carrera
        self.mi_cursos = []

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}, Legajo: {self.legajo}, Año de Inscripción: {self.anio_inscripcion_carrera}"

    def matricular_en_curso(self, curso):
        if curso not in self.mi_cursos:
            self.mi_cursos.append(curso)
            return True
        else:
            return False


class Profesor(Usuario):
    def __init__(self, nombre, apellido, email, password, titulo, anio_egreso):
        super().__init__(nombre, apellido, email, password)
        self.nombre = nombre
        self.apellido = apellido
        self.titulo = titulo
        self.anio_egreso = anio_egreso
        self.mis_cursos = []

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}, Título: {self.titulo}, Año de Egreso: {self.anio_egreso}"

    def dictar_curso(self, curso):
        self.mis_cursos.append(curso)


class Curso:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contraseña = ''.join(random.choice(
            '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(6))
        self.archivos = []

    def __str__(self):
        return f"Nombre: {self.nombre}\nContraseña: {self.contraseña}"

    def agregar_archivo(self, archivo):
        self.archivos.append(archivo)


alumno1 = Estudiante("Juan", "Pérez", "juan@gmail.com",
                     "password1", 12345, 2022)
profesor1 = Profesor("Profesor", "Ejemplo",
                     "prof@gmail.com", "password2", "PhD", 2010)

curso1 = Curso("Ingles I")
curso2 = Curso("Ingles II")
curso3 = Curso("Laboratorio I")
curso4 = Curso("Laboratorio II")
curso5 = Curso("Programación I")
curso6 = Curso("Programación II")

profesor1.dictar_curso(curso1)
profesor1.dictar_curso(curso2)
profesor1.dictar_curso(curso3)
profesor1.dictar_curso(curso4)
profesor1.dictar_curso(curso5)
profesor1.dictar_curso(curso6)


def login_alumno(email, password):
    for alumno in alumnos:
        if alumno.validar_credenciales(email, password):
            return alumno
    return None


def login_profesor(email, password):
    for profesor in profesores:
        if profesor.validar_credenciales(email, password):
            return profesor
    return None


alumnos = [alumno1]
profesores = [profesor1]

cursos_sistema = [curso1, curso2, curso3, curso4, curso5, curso6]

while True:
    print("\nMenú Principal:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        email = input("Ingrese su email como alumno: ")
        password = input("Ingrese su contraseña: ")

        alumno = login_alumno(email, password)

        if alumno:
            while True:
                print("\nSubmenú Alumno:")
                print("1. Matricularse en un curso")
                print("2. Ver cursos matriculados")
                print("3. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    print("\nCursos disponibles:")
                    for i, curso in enumerate(cursos_sistema, start=1):
                        print(f"{i}. {curso.nombre}")

                    curso_index = int(input("Seleccione un curso para matricularse: ")) - 1

                    if 0 <= curso_index < len(cursos_sistema):
                        curso_seleccionado = cursos_sistema[curso_index]
                        matriculado = alumno.matricular_en_curso(
                            curso_seleccionado)

                        if matriculado:
                            print(
                                f"Matriculación exitosa en {curso_seleccionado.nombre}")
                        else:
                            print(
                                f"Ya está matriculado en {curso_seleccionado.nombre}")

                elif sub_opcion == "2":
                    print("\nCursos matriculados:")
                    for i, curso in enumerate(alumno.mi_cursos, start=1):
                        print(f"{i}. {curso.nombre}")

                    curso_index = int(
                        input("Seleccione un curso para ver archivos: ")) - 1

                    if 0 <= curso_index < len(alumno.mi_cursos):
                        curso_seleccionado = alumno.mi_cursos[curso_index]
                        print(f"Archivos en {curso_seleccionado.nombre}:")
                        for archivo in curso_seleccionado.archivos:
                            print(archivo)

                elif sub_opcion == "3":
                    break
        else:
            print("El email o contraseña ingresados no se encuentran registrados. Por favor registrese")

    elif opcion == "2":
        email = input("Ingrese su email como profesor: ")
        password = input("Ingrese su contraseña: ")

        profesor = login_profesor(email, password)

        if profesor:
            while True:
                print("\nSubmenú Profesor:")
                print("1. Dictar un curso")
                print("2. Ver cursos dictados")
                print("3. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    nombre_curso = input(
                        "Ingrese el nombre del curso a dar de alta: ")
                    nuevo_curso = Curso(nombre_curso)
                    profesor.dictar_curso(nuevo_curso)
                    print(f"Curso dado de alta:\n{str(nuevo_curso)}")

                elif sub_opcion == "2":
                    print("\nCursos dictados:")
                    for i, curso in enumerate(profesor.mis_cursos, start=1):
                        print(
                            f"{i}. {curso.nombre}\nContraseña: {curso.contraseña}")

                elif sub_opcion == "3":
                    break
        else:
            print("El email o contraseña ingresados no se encuentran registrados. Por favor hable en alumnado")

    elif opcion == "3":
        print("\nCursos en el sistema:")
        for i, curso in enumerate(cursos_sistema, start=1):
            print(
                f"{i}. Materia: {curso.nombre} Carrera: Tecnicatura Universitaria en Programación")

    elif opcion == "4":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
