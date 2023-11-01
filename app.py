from usuario import Usuario, Estudiante, Profesor
from curso import Curso
from archivo import Archivo

#usuarios de prueba:
alumno1 = Estudiante("Juan", "Pérez", "juan@gmail.com", "password1", 12345, 2022)
profesor1 = Profesor("Profesor", "Ejemplo", "prof@gmail.com", "password2", "PhD", 2010)

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

#funcion para buscar alumno
def login_alumno(email, password):
    for alumno in alumnos:
        if alumno._email == email:

            if alumno.validar_credenciales(email, password):
                return alumno
            else:
                print("Error de ingreso. La contraseña es incorrecta.")
            return None

    print("Error de ingreso. No se encontro un alumno con ese correo.")
    print("Debe darse de alta en alumnado.")
    return None

#para buscar profesor
def login_profesor(email, password):
    for profesor in profesores:
        if profesor._email == email:
            if profesor.validar_credenciales(email, password):
                return profesor
            else:
                print("Error de ingreso. Contraseña incorrecta.")
            return None
    print("Error de ingreso. No se encontro email registrado.")
    print("Por favor, debe darse de alta en alumnado. ")


# Lista de alumnos y profesores
alumnos = [alumno1]
profesores = [profesor1]

cursos_sistema = [curso1, curso2, curso3, curso4, curso5, curso6]

codigo_admin = "admiutn"

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
                print("2. Desmatricularse de un curso")
                print("3. Ver cursos matriculados")
                print("4. Volver al menú principal")
                sub_opcion = input("Seleccione una opción: ")

                if sub_opcion == "1":
                    print("\nCursos disponibles:")
                    for i, curso in enumerate(cursos_sistema, start=1):
                        print(f"{i}. {curso._nombre}")

                    curso_index = int(input("Seleccione un curso para matricularse: ")) - 1

                    if 0 <= curso_index < len(cursos_sistema):
                        curso_seleccionado = cursos_sistema[curso_index]

                        if curso_seleccionado not in alumno.mi_cursos:
                            contraseña_curso = input(f"Ingrese la contraseña para {curso_seleccionado._nombre}: ")

                            if contraseña_curso == curso_seleccionado._contraseña:
                                matriculado = alumno.matricular_en_curso(curso_seleccionado)
                                if matriculado:
                                    print(f"Matriculación exitosa en {curso_seleccionado._nombre}")
                                else:
                                    print("Error: No se pudo matricular en el curso.")
                            else:
                                print("Error: Contraseña incorrecta para el curso.")
                        else:
                            print("Error: Ya se encuentra matriculado en este curso.")
                    else:
                        print("Error: Selección no válida.")

                elif sub_opcion == "2":
                    print("\nCursos matriculados:")
                    for i, curso in enumerate(alumno.mi_cursos, start=1):
                        print(f"{i}. {curso._nombre}")
                    opc = int(input("Ingrese el número de curso del que desea desmatricularse: "))

                    while opc < 1 or opc > len(alumno.mi_cursos):
                        opc = int(input("\nError! Ingrese un número de curso válido:\n"))

                    seleccionado_desmatricular = alumno.mi_cursos[opc - 1]
                    alumno.desmatricular_del_curso(seleccionado_desmatricular)      

                elif sub_opcion == "3":
                    print("\nCursos matriculados:")
                    for i, curso in enumerate(alumno.mi_cursos, start=1):
                        print(f"{i}. {curso._nombre}")

                elif sub_opcion == "4":
                    break

                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")

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
                    nombre_curso = input("Ingrese el nombre del curso a dar de alta: ")
                    
                    curso_existente = None
                    for curso in profesor.mis_cursos:
                        if curso._nombre == nombre_curso:
                            curso_existente = curso
                            break
                    if curso_existente:
                        print(f"El curso '{nombre_curso}' ya ha sido dado de alta!")
                    else:
                        nuevo_curso = Curso(nombre_curso)
                        profesor.dictar_curso(nuevo_curso)
                        print(f"Curso dado de alta:\n{str(nuevo_curso)}")
                elif sub_opcion == "2":
                    print("\nCursos dictados:")
                    for i, curso in enumerate(profesor.mis_cursos, start=1):
                        print(f"{i}. {curso._nombre}\nContraseña: {curso._contraseña}")

                    agregar_archivos = input("¿Desea agregar un archivo adjunto a uno de sus cursos dictados? (Si/No): ").lower()
    
                    if agregar_archivos == "si":
                        print("\nCursos dictados:")
                        for i, curso in enumerate(profesor.mis_cursos, start=1):
                            print(f"{i}. {curso._nombre}\nContraseña: {curso._contraseña}")
                        
                        opc_curso = int(input("Seleccione un curso al que desea agregar un archivo adjunto: ")) - 1

                        if 0 <= opc_curso < len(profesor.mis_cursos):
                            curso_seleccionado = profesor.mis_cursos[opc_curso]

                            while True:
                                nombre_archivo = input("Ingrese el nombre del archivo: ")
                                formato_archivo = input("Ingrese el formato del archivo: ")
                                archivo = Archivo(nombre_archivo, formato_archivo)
                                curso_seleccionado.agregar_archivo(archivo)
                                print("Archivo adjunto agregado con éxito.")

                                continuar = input("¿Desea agregar otro archivo adjunto? (Si/No): ").lower()
                                if continuar != "si":
                                    break
                        else:
                            print("Selección no válida. Por favor, elija un curso válido.")
                    elif agregar_archivos == "no":
                        print("Volviendo al menú principal.")
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida (Si/No).")

                elif sub_opcion == "3":
                    break
                else:
                    print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            codigo_admin_ingresado = input("Ingrese el código para darse de alta como profesor: ")
            if codigo_admin_ingresado == codigo_admin:
                nombre = input("Ingrese su nombre: ")
                apellido = input("Ingrese su apellido: ")
                email = input("Ingrese su email: ")
                password = input("Ingrese su contraseña: ")
                titulo = input("Ingrese su título: ")
                anio_egreso = input("Ingrese el año de egreso: ")

                nuevo_profesor = Profesor(nombre, apellido, email, password, titulo, anio_egreso)
                profesores.append(nuevo_profesor)

                print("Registro de profesor exitoso.")
            else:
                print("Código incorrecto. No se pudo registrar como profesor.")

    elif opcion == "3":
        print("\nCursos en el sistema:")
        
        sorted_cursos = sorted(cursos_sistema, key=lambda curso: curso._nombre)
        for curso in sorted_cursos:
            print(f"Materia: {curso._nombre} Carrera: Tecnicatura Universitaria en Programación")

    elif opcion == "4":
        print("Saliendo del sistema. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
