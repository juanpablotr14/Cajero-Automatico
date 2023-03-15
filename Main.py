from Components import dinero_disp, total, conteo, inicio, ingresar, retirar, lista_string;

salida = True;

while salida:
    print("");
    print("-------Bienvenido al Cajero Automatico-------");
    print("");
    print("Por favor ingrese el numero correspondiente a la opcción:");
    print("");
    print("1• Inicio");
    print("2• Consignación");
    print("3• Retiro");
    print("4• Conteo de denominaciones");
    print("5• Total");
    print("6• Salir");
    print("");
    
    try: 
        
        eleccion = int(input("Ingresa el numero de tu elección: "));
    
        if eleccion == 1:
            
            print("");
            print("-------Sección de Inicio del Cajero-------");
            print("");
            print("El cajero cuenta con:");
            
            conteo();
                
            print("!¿Desea ingresar mas dinero?!");
            print("1•Si");
            print("2•No");
            
            try:
                
                deci = int(input("Ingresa el numero de tu elección: "));
                
                if deci == 1:
                    inicio();
                    prueba = open('Archivos/cajero.txt', 'a');
                    for code in lista_string(dinero_disp):
                        prueba.write(f"Inicio({code})");
                    prueba.write("\n");
                    prueba.close();
                    
                elif deci == 2:
                    print("Volviendo al menu principal! :D");
                    
                else:
                    print("Ese valor no esta permitido! :D");
                    
            except ValueError:
                print("Por favor ingresa un entero!");
                
        elif eleccion == 2:
            
            print("");
            print("-------Consignación-------");     
            print("");    
            
            prueba = open('Archivos/cajero.txt', 'a');
            for i in lista_string(ingresar()):
                prueba.write(f"Consignación({i})");
            prueba.write("\n");
            prueba.close();
            
        elif eleccion == 3:
            
            print("");
            print("-------Retirar-------");   
            print("");         
            
            retiro = int(input("!¿Cuanto dinero deseas retirar?!"));
            retirar(retiro);
            prueba = open('Archivos/cajero.txt', 'a');
            prueba.write(f"Retiro({retiro})");
            prueba.write("\n");
            prueba.close();
            
        elif eleccion == 4:
            
            print("");
            print("-------Contar Denominaciones-------");
            print("");   
            
            conteo();        
            
        elif eleccion == 5:
            
            print("");
            print("-------Total-------");
            print("");
            print(f"El total de dinero en el cajero es: {total()}");
            
            
        elif eleccion == 6:
            
            print("");
            print("Hasta luego, Vuelve Pronto!");
            salida = False;
            
        elif 1 < eleccion < 7 :
            print("Por favor ingrese un numero entero positivo! :D");
            
    except ValueError:
        print("Por favor ingresa un entero!");
        