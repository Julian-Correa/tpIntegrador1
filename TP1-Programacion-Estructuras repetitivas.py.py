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

#ejercicio 2


#ejercicio 2
usuario_Correcto = "alumno"
contraseña_Correcta = "python123"

print("Bienvenido/a al Campus.")

intentos = 0
max_intentos = 3

while intentos < max_intentos:
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if intentos == max_intentos - 1 :      
        print("Has alcanzado el número máximo de intentos. Acceso bloqueado.")
        break
    elif usuario != usuario_Correcto or contraseña != contraseña_Correcta:
         print("Usuario o contraseña incorrectos. Intente nuevamente.")
         intentos += 1
    else:
         print("¡Acceso concedido! Bienvenido/a al Campus.")
         while True:
                print("Menu:")
                print("1. Ver estado de inscripción")
                print("2. Cambiar clave")
                print("3. Mostrar mensaje motivacional")
                print("4. Salir")

                opcion = input("Seleccione una opción (1-4): ")
                if opcion.isdigit() and 1 <= int(opcion) <= 4:
                        opcion = int(opcion) 
                else:
                        print("Entrada no válida. Por favor, ingrese un número del 1 al 4.")
                        continue 
                if opcion == 1:
                        print("Estado de inscripción: Inscrito")
                        continue
                elif opcion == 2:
                        nueva_contraseña = input("Ingrese su nueva contraseña: ")
                        while len(nueva_contraseña) < 6:
                                 nueva_contraseña = input("La nueva contraseña debe tener al menos 6 caracteres. Intente nuevamente: ")
                        contraseña_Correcta = nueva_contraseña
                        print("Contraseña actualizada exitosamente.")
                        continue
                elif opcion == 3:
                        print("¡Sigue adelante! Tu potencial es ilimitado.")
                        continue
                elif opcion == 4:
                        print("Gracias por usar nuestro sistema.")
                        break

                break


                        


