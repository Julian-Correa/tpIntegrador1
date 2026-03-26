# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

Turnos_Lunes = 4
Turnos_Martes = 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

Nombre_Operador = input("Ingrese su nombre: ")

if not Nombre_Operador.isalpha():
    print("El nombre ingresado es invalido. El nombre debe contener solo letras.")
else:
    while True:
        print(f"Bienvenido/a, {Nombre_Operador}.")
        print(" Menu de opciones:")
        print("1. Reservar turno.")
        print("2. Cancelar turno.")  # por nombre
        print("3. Ver agenda del dia")
        print("4. Ver resumen general")
        print("5. Cerrar sistema")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            while True:
                paciente = input("Ingrese el nombre del paciente para reservar el turno: ")

                if not paciente.isalpha():
                    print("El nombre del paciente es inválido. Debe contener solo letras.")

                Turno_seleccionado = input("Seleccione el día para reservar el turno (Lunes/Martes): ").lower()


                if Turno_seleccionado == "lunes":
                    if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
                        print("El nombre del paciente ya tiene un turno reservado. Ingrese otro nombre.")
                        continue
                    elif Turnos_Lunes > 0:
                        if lunes1 == "":
                            lunes1 = paciente
                        elif lunes2 == "":
                         lunes2 = paciente
                        elif lunes3 =="":
                                lunes3 = paciente
                        elif lunes4 == "":
                                lunes4 = paciente
                        Turnos_Lunes -= 1
                        print(f"Turno reservado para {paciente} el Lunes.")
                        break

                elif Turno_seleccionado == "martes":
                    if paciente == martes1 or paciente == martes2 or paciente == martes3:
                        print("El nombre del paciente ya tiene un turno reservado. Ingrese otro nombre.")
                        continue

 

                elif Turnos_Martes > 0:
                    if martes1 == "":
                        martes1 = paciente
                    elif martes2 == "":
                        martes2 = paciente
                    elif martes3 == "":
                        martes3 = paciente

                    Turnos_Martes -= 1
                    print(f"Turno reservado para {paciente} el Martes.")
                    break