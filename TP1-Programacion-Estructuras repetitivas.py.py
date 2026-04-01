#ejercicio 1
while True:
    nombre = input("Ingrese nombre del cliente(solo letras): ")
    if nombre.isalpha():  
        break
    else: 
        print("Error: El nombre debe contener solo letras. Intente nuevamente.")
        continue

while True:
    cantidad = input("Ingrese cantidad de productos(numero positivo): ")
    if cantidad.isdigit() and int(cantidad) > 0:
        break
    else:
        print("Error: La cantidad debe ser un número entero positivo. Intente nuevamente.")
        continue




precio_con_descuento = 0
precio_sin_descuento = 0

for i in range(1, int(cantidad) + 1):
    
        while True:
  
            precio = input(f"Ingrese el precio del producto {i} (número positivo): ")
            if precio.isdigit() and int(precio) > 0:
                pass
                tiene_descuento = input("el producto tiene descuento? (s/n): ")
                descuesto = tiene_descuento.lower() 
                precio_sin_descuento += int(precio)
                if tiene_descuento == "s":
                    descuento = int(precio) * 10 / 100 # Aplicar descuento del 10%
                    precio_con_descuento += precio_sin_descuento - descuento
                    print( "Producto con descuento guardado correctamente.")
    
                elif tiene_descuento == "n":
                    print( "Producto guardado correctamente.")
                else:
                    print("Error: Debe ingresar 's' para sí o 'n' para no. Intente nuevamente.")
                    continue
                break
             
            
            else:
                print("Error: El precio debe ser un número positivo. Intente nuevamente.")
                continue        
print(f"El cliente : {nombre}")
print(f"Cantidad de productos: {cantidad}")
print(f"El total sin descuento es: {precio_sin_descuento}")
print(f"El total con descuento es: {precio_con_descuento}")
print(f"El ahorro total es: {precio_sin_descuento - precio_con_descuento}")
print(f"El precio promedio por producto sin descuento es: {precio_sin_descuento / int(cantidad):.2f}")
print(f"El precio promedio por producto con descuento es: {precio_con_descuento / int(cantidad):.2f}")
print("Gracias por su compra.")

#------------------------------------------------------------------------------------------------
# ejercicio 2
usuario_Correcto = "alumno"
contraseña_Correcta = "python123"

print("Bienvenido/a al Campus.")

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    print(f"Intento {intentos + 1}/{max_intentos}")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario == usuario_Correcto and contraseña == contraseña_Correcta:
        print("¡Acceso concedido! Bienvenido/a al Campus.")

        while True:
            print("Menu:")
            print("1. Ver estado de inscripción")
            print("2. Cambiar clave")
            print("3. Mostrar mensaje motivacional")
            print("4. Salir")

            opcion = input("Seleccione una opción (1-4): ")

            if not opcion.isdigit():
                print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")
                continue

            opcion = int(opcion)

            if opcion < 1 or opcion > 4:
                print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")
                continue

            if opcion == 1:
                print("Estado de inscripción: Inscripto")

            elif opcion == 2:
                nueva_contraseña = input("Ingrese su nueva contraseña: ")

                while len(nueva_contraseña) < 6:
                    nueva_contraseña = input("Error: mínimo 6 caracteres. Intente nuevamente: ")

                confirmacion = input("Confirme su nueva contraseña: ")

                while confirmacion != nueva_contraseña:
                    print("Error: las contraseñas no coinciden.")
                    confirmacion = input("Confirme su nueva contraseña: ")

                contraseña_Correcta = nueva_contraseña
                print("Contraseña actualizada exitosamente.")

            elif opcion == 3:
                print("¡Sigue adelante! Tu potencial es ilimitado.")

            elif opcion == 4:
                print("Gracias por usar nuestro sistema.")
                break

        break

    else:
        intentos += 1
        print("Error: credenciales inválidas.")

if intentos == max_intentos:
    print("Cuenta bloqueada.")


#----------------------------------------------------------------------------------      
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

while not Nombre_Operador.isalpha():
    print("El nombre ingresado es inválido. El nombre debe contener solo letras.")
    Nombre_Operador = input("Ingrese su nombre: ")

while True:
    print(f"\nBienvenido/a, {Nombre_Operador}.")
    print("Menu de opciones:")
    print("1. Reservar turno.")
    print("2. Cancelar turno.")
    print("3. Ver agenda del día")
    print("4. Ver resumen general")
    print("5. Cerrar sistema")

    while True:
        opcion = input("Seleccione una opción (1-5): ")

        if opcion.isdigit():
            opcion = int(opcion)
            if 1 <= opcion <= 5:
                break

        print("Entrada no válida. Debe ingresar un número del 1 al 5.")

    if opcion == 1:
        while True:
            paciente = input("Ingrese el nombre del paciente para reservar el turno: ")

            if not paciente.isalpha():
                print("El nombre del paciente es inválido. Debe contener solo letras.")
                continue

            Turno_seleccionado = input(
                "Seleccione el día para reservar el turno (Lunes/Martes): "
            ).lower()

            if Turno_seleccionado == "lunes":
                if (
                    paciente == lunes1
                    or paciente == lunes2
                    or paciente == lunes3
                    or paciente == lunes4
                ):
                    print("El nombre del paciente ya tiene un turno reservado. Ingrese otro nombre.")
                    continue
                elif Turnos_Lunes > 0:
                    if lunes1 == "":
                        lunes1 = paciente
                    elif lunes2 == "":
                        lunes2 = paciente
                    elif lunes3 == "":
                        lunes3 = paciente
                    elif lunes4 == "":
                        lunes4 = paciente

                    Turnos_Lunes -= 1
                    print(f"Turno reservado para {paciente} el Lunes.")
                    break
                else:
                    print("No hay más turnos disponibles para el Lunes.")
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
                else:
                    print("No hay más turnos disponibles para el Martes.")
                    break

            else:
                print("Día inválido. Debe ingresar Lunes o Martes.")
                continue

    elif opcion == 2:
        while True:
            dia_cancelar = input(
                "Seleccione el día del turno a cancelar (Lunes/Martes): "
            ).lower()

            if dia_cancelar != "lunes" and dia_cancelar != "martes":
                print("Día inválido. Debe ingresar Lunes o Martes.")
                continue

            paciente_cancelar = input("Ingrese el nombre del paciente a cancelar: ")

            if not paciente_cancelar.isalpha():
                print("El nombre del paciente es inválido. Debe contener solo letras.")
                continue

            if dia_cancelar == "lunes":
                if paciente_cancelar == lunes1:
                    lunes1 = ""
                    Turnos_Lunes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Lunes.")
                elif paciente_cancelar == lunes2:
                    lunes2 = ""
                    Turnos_Lunes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Lunes.")
                elif paciente_cancelar == lunes3:
                    lunes3 = ""
                    Turnos_Lunes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Lunes.")
                elif paciente_cancelar == lunes4:
                    lunes4 = ""
                    Turnos_Lunes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Lunes.")
                else:
                    print("Ese paciente no tiene turno reservado el Lunes.")

            elif dia_cancelar == "martes":
                if paciente_cancelar == martes1:
                    martes1 = ""
                    Turnos_Martes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Martes.")
                elif paciente_cancelar == martes2:
                    martes2 = ""
                    Turnos_Martes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Martes.")
                elif paciente_cancelar == martes3:
                    martes3 = ""
                    Turnos_Martes += 1
                    print(f"Turno de {paciente_cancelar} cancelado correctamente del Martes.")
                else:
                    print("Ese paciente no tiene turno reservado el Martes.")

            break

    elif opcion == 3:
        while True:
            dia_agenda = input(
                "Seleccione el día para ver la agenda (Lunes/Martes): "
            ).lower()

            if dia_agenda == "lunes":
                print("\nAgenda del Lunes:")
                if lunes1 == "":
                    print("Turno 1: (libre)")
                else:
                    print(f"Turno 1: {lunes1}")

                if lunes2 == "":
                    print("Turno 2: (libre)")
                else:
                    print(f"Turno 2: {lunes2}")

                if lunes3 == "":
                    print("Turno 3: (libre)")
                else:
                    print(f"Turno 3: {lunes3}")

                if lunes4 == "":
                    print("Turno 4: (libre)")
                else:
                    print(f"Turno 4: {lunes4}")
                break

            elif dia_agenda == "martes":
                print("\nAgenda del Martes:")
                if martes1 == "":
                    print("Turno 1: (libre)")
                else:
                    print(f"Turno 1: {martes1}")

                if martes2 == "":
                    print("Turno 2: (libre)")
                else:
                    print(f"Turno 2: {martes2}")

                if martes3 == "":
                    print("Turno 3: (libre)")
                else:
                    print(f"Turno 3: {martes3}")
                break

            else:
                print("Día inválido. Debe ingresar Lunes o Martes.")

    elif opcion == 4:
        ocupados_lunes = 4 - Turnos_Lunes
        ocupados_martes = 3 - Turnos_Martes

        print("\nResumen general:")
        print(f"Lunes -> Ocupados: {ocupados_lunes} | Disponibles: {Turnos_Lunes}")
        print(f"Martes -> Ocupados: {ocupados_martes} | Disponibles: {Turnos_Martes}")

        if ocupados_lunes > ocupados_martes:
            print("El día con más turnos ocupados es: Lunes")
        elif ocupados_martes > ocupados_lunes:
            print("El día con más turnos ocupados es: Martes")
        else:
            print("Hay empate en la cantidad de turnos ocupados entre Lunes y Martes.")

    elif opcion == 5:
        print("Sistema cerrado.")
        break


#---------------------------------------------------------------------------------------------------------  
# EJERCICIO 4 — Escape Room: La Bóveda

energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
anti_spam = 0

Nombre_agente = input("Ingrese nombre del agente: ")

while not Nombre_agente.isalpha():
    print("El nombre del agente no puede estar vacío y debe contener solo letras.")
    Nombre_agente = input("Ingrese nombre del agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:
    print("\n--- ESTADO ACTUAL ---")
    print(f"Agente: {Nombre_agente}")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {'ACTIVADA' if alarma else 'DESACTIVADA'}")
    print(f"Código parcial: {codigo_parcial}")

    print("\nMenú de acciones:")
    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Seleccione una opción (1-3): ")

    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Opción inválida. Debe ingresar un número del 1 al 3.")
        opcion = input("Seleccione una opción (1-3): ")

    opcion = int(opcion)

    if opcion == 1:
        energia -= 20
        tiempo -= 2
        anti_spam += 1

        if anti_spam == 3:
            alarma = True
            print("La cerradura se trabó por forzar 3 veces seguidas.")
            print("Se activó la alarma automáticamente.")
        else:
            if energia < 40:
                print("Tu energía está por debajo de 40. Hay riesgo de alarma.")
                riesgo = input("Seleccione un número del 1 al 3: ")

                while not riesgo.isdigit() or not (1 <= int(riesgo) <= 3):
                    print("Entrada inválida. Debe ingresar un número del 1 al 3.")
                    riesgo = input("Seleccione un número del 1 al 3: ")

                riesgo = int(riesgo)

                if riesgo == 3:
                    alarma = True
                    print("Fallaste. Se activó la alarma.")
                else:
                    cerraduras_abiertas += 1
                    print("Lograste forzar la cerradura y abrirla.")
            else:
                cerraduras_abiertas += 1
                print("Lograste forzar la cerradura y abrirla.")

    elif opcion == 2:
        anti_spam = 0
        energia -= 10
        tiempo -= 3

        print("Iniciando hackeo del panel...")
        for paso in range(1, 5):
            print(f"Progreso del hackeo: paso {paso}/4")
            codigo_parcial += "A"

        print(f"Código parcial actual: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("El hackeo fue suficiente para abrir automáticamente una cerradura.")

    elif opcion == 3:
        anti_spam = 0
        energia += 15

        if energia > 100:
            energia = 100

        tiempo -= 1

        if alarma:
            energia -= 10
            print("Descansaste, pero la alarma te desgastó: perdiste 10 de energía extra.")

        print("Descansaste y recuperaste energía.")

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("\nEl sistema se bloqueó por la alarma.")
        print("DERROTA: no lograste abrir la bóveda a tiempo.")
        break

if cerraduras_abiertas == 3:
    print(f"\nVICTORIA: {Nombre_agente} abrió las 3 cerraduras y accedió a la bóveda.")
elif energia <= 0 or tiempo <= 0:
    print(f"\nDERROTA: {Nombre_agente} se quedó sin energía o sin tiempo.")

#-------------------------------------------------------------------------------------------------
#Ejercicio 5  — “Escape Room:"La Arena del Gladiador"

while True:
    nombre_del_gladeador = input("Ingrese el nombre del gladiador: ")
    
    if nombre_del_gladeador.isalpha():
        print("Nombre válido.")
        break
    else:
        print("Nombre inválido. Solo se permiten letras.")

gladeador = nombre_del_gladeador
vida_del_gladeador = 100
vida_del_enemigo = 100
pociones_de_vida = 3
daño_base_ataque_pesado = 15
daño_base_enemigo = 12
turno_gladeador = True

while vida_del_gladeador > 0 and vida_del_enemigo > 0:
    if turno_gladeador:
        print(f"\nTurno de {gladeador}:")
        print("1. Ataque pesado (15 de daño)")
        print("2. Rafaga veloz ")
        print("3. Curar (restaura 20 de vida)")
        accion = input("Elige tu acción (1/2/3): ")

        if accion.isdigit() and accion == "1":
            vida_del_enemigo -= 15
            print(f"{gladeador} realiza un ataque pesado. Vida del enemigo: {vida_del_enemigo}")
            if vida_del_enemigo < 20:
                print("¡Golpe crítico!")
                daño_base_ataque_pesado *=  1.5
                vida_del_enemigo -= daño_base_ataque_pesado
                print(f"Daño adicional por golpe crítico: {daño_base_ataque_pesado}. Vida del enemigo: {vida_del_enemigo}")
        elif accion.isdigit() and accion == "2":
            for i in range(3):
                vida_del_enemigo -= 5
                print(f"Ataque veloz {i+1}: Vida del enemigo: {vida_del_enemigo}")
            print(f"{gladeador} realiza un ataque veloz¡. Vida del enemigo: {vida_del_enemigo}")
        elif accion.isdigit() and accion == "3":
            if pociones_de_vida > 0:
                vida_del_gladeador += 30
                pociones_de_vida -= 1
                print(f"{gladeador} usa una poción de vida. Vida actual: {vida_del_gladeador}, Pociones restantes: {pociones_de_vida}")
            else:
                print("¡No quedan pociones! Pierdes el turno.")
                continue
        else:
            print("Acción inválida. Intenta de nuevo.")
            continue

        turno_gladeador = False
    else:
        vida_del_gladeador -= daño_base_enemigo
        print(f"El enemigo te ataco por 12 puntos de daño¡. Vida de {gladeador}: {vida_del_gladeador}")
        turno_gladeador = True

if vida_del_gladeador <= 0:
    print(f"\n DERROTA. Has caído en combate.")
elif vida_del_enemigo <= 0:
    print(f"\n VICTORIA! {gladeador} has ganado la batalla.")