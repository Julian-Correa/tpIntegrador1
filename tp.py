#EJERCICIO 4 = Escape Room : La boveda

energia = 100
tiempo = 12
cerraduras_abiertas=0
alarma = False
codigo_parcial= ""
anti_spam = 0


while True:
    Nombre_agente = input('Ingrese nombre del agente:')
    if not Nombre_agente.isalpha() or Nombre_agente == '':
        print("El nombre del agente no puede estar vacio y debe de tener solo letras. ")
    else:
        while True:
            print("Menu")
            print("1-Forzar Cerradura")
            print("2-Hackear panel")
            print("3-Descansar")
            opcion = input("seleccione una opcion del menu (numero):")
            match opcion :
                case 1 :
                    energia -= 20 
                    tiempo -= 2
                    anti_spam =+ 1
                    if anti-spam == 3:
                        print("se encendio la alarma por forzar tantas veces la cerradura!")
                        break
                    if energia <= 40:
                        print("Energia por debajo de 40. Riesgo de alarma.")
                        riesgo_alarma = input("Seleccione un numero del 1 al 3.")
                        if not riesgo_alarma.isdigit() and (riesgo_alarma != 1 or riesgo_alarma !=2 or riesgo_alarma !=3):
                            print("debe de seleccionar un numero del 1 al 3") 
                        elif riesgo_alarma == 3 : 
                            alarma = True
                            print("Se encendio la alarma!!")
                        else :
                            print("Felicidades abriste la cerradura!")
                            cerraduras_abiertas += 1


                        
                        
                            
 #               case 2 :
                    #codigo
 #               case 3 :
                    #codigo
    #            case _:
    #                print("opcion invalida, debe de seleccionar un numero dentro del menu de opciones ")


        
