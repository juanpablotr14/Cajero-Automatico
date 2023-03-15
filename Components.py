nombre_billetes = ["Billetes de 100k pesos: ", "Billetes de 50k pesos: ", "Billetes de 20k pesos: ", "Billetes de 10k pesos: ", "Billetes de 5k pesos: ", "Billetes de 2k pesos: ", "Billetes de 1k pesos: "];
dinero_disp = [100, 100, 100, 100, 100, 100, 100];

def conteo():
    for i, j in zip(nombre_billetes, dinero_disp):
        print(i, j);

def inicio():
    billete_100 = int(input("Ingrese la cantidad de billetes de 100k que va a consignar: "));
    dinero_disp[0] += billete_100;
    billete_50 = int(input("Ingrese la cantidad de billetes de 50k que va a consignar: "));
    dinero_disp[1] += billete_50;
    billete_20 = int(input("Ingrese la cantidad de billetes de 20k que va a consignar: "));
    dinero_disp[2] += billete_20;
    billete_10 = int(input("Ingrese la cantidad de billetes de 10k que va a consignar: "));
    dinero_disp[3] += billete_10;
    billete_5 = int(input("Ingrese la cantidad de billetes de 5k que va a consignar: "));
    dinero_disp[4] += billete_5;
    billete_2 = int(input("Ingrese la cantidad de billetes de 2k que va a consignar: "));
    dinero_disp[5] += billete_2;
    billete_1 = int(input("Ingrese la cantidad de billetes de 1k que va a consignar: "));
    dinero_disp[6] += billete_1;
    print(f"Has ingresado {(billete_100*100)+(billete_50*50)+(billete_20*20)+(billete_10*10)+(billete_5*5)+(billete_2*2)+(billete_1)}k exitosamente! :D");
    
    
def ingresar():
    lista_consignacion = []
    billete_100 = int(input("Ingrese la cantidad de billetes de 100k que va a consignar: "));
    dinero_disp[0] += billete_100;
    lista_consignacion.append(billete_100);
    billete_50 = int(input("Ingrese la cantidad de billetes de 50k que va a consignar: "));
    dinero_disp[1] += billete_50;
    lista_consignacion.append(billete_50);
    billete_20 = int(input("Ingrese la cantidad de billetes de 20k que va a consignar: "));
    dinero_disp[2] += billete_20;
    lista_consignacion.append(billete_20);
    billete_10 = int(input("Ingrese la cantidad de billetes de 10k que va a consignar: "));
    dinero_disp[3] += billete_10;
    lista_consignacion.append(billete_10);
    billete_5 = int(input("Ingrese la cantidad de billetes de 5k que va a consignar: "));
    dinero_disp[4] += billete_5;
    lista_consignacion.append(billete_5);
    billete_2 = int(input("Ingrese la cantidad de billetes de 2k que va a consignar: "));
    dinero_disp[5] += billete_2;
    lista_consignacion.append(billete_2);
    billete_1 = int(input("Ingrese la cantidad de billetes de 1k que va a consignar: "));
    dinero_disp[6] += billete_1;
    lista_consignacion.append(billete_1);
    print(f"Has ingresado {(billete_100*100)+(billete_50*50)+(billete_20*20)+(billete_10*10)+(billete_5*5)+(billete_2*2)+(billete_1)}k exitosamente! :D");
    return lista_consignacion;

def retirar(monto):
    denominaciones = [100, 50, 20, 10, 5, 2, 1]
    billetes_entregados = []
    cantidad_entregada = 0
    
    if total() > monto:
        
        for i in range(len(denominaciones)):
            billetes_a_entregar = min(monto // denominaciones[i], dinero_disp[i])
            billetes_entregados.append(billetes_a_entregar)
            cantidad_entregada += billetes_a_entregar * denominaciones[i]
            monto -= billetes_a_entregar * denominaciones[i]
            dinero_disp[i] -= billetes_a_entregar
            print(f"Billetes de {denominaciones[i]}: {billetes_a_entregar}")
            
            if cantidad_entregada == monto:
                break
            
        billetes_entregados.append(monto // denominaciones[-1])
        dinero_disp[-1] -= monto // denominaciones[-1]
    else:
        print("No hay suficiente dinero en cajero :(");
    
    return billetes_entregados;
    
def lista_string(lista):
    aux_string = lista.copy();
    lista_string = [str(num) for num in aux_string];
    string = [','.join(lista_string)];
    return string

def total():
    total = 0;
    total = total + (dinero_disp[0] * 100);
    total = total + (dinero_disp[1] * 50);
    total = total + (dinero_disp[2] * 20);
    total = total + (dinero_disp[3] * 10);
    total = total + (dinero_disp[4] * 5);
    total = total + (dinero_disp[5] * 2);
    total = total + dinero_disp[6];
    return total;