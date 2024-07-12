import random
import csv


trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez",
                "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", 
                "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]


def asignar_sueldos_aleatorios():
    sueldos = []
    for _ in range(10):
        sueldo = random.randint(300000, 2500000)
        sueldos.append(sueldo)
    return sueldos


def clasificar_sueldos(sueldos):
    menor_800k = []
    entre_800k_y_2m = []
    mayor_2m = []
    
    for i in range(10):
        nombre = trabajadores[i]
        sueldo = sueldos[i]
        if sueldo < 800000:
            menor_800k.append((nombre, sueldo))
        elif sueldo >= 800000 and sueldo <= 2000000:
            entre_800k_y_2m.append((nombre, sueldo))
        else:
            mayor_2m.append((nombre, sueldo))
    
    print("Sueldos menores a $800.000")
    print("TOTAL:", len(menor_800k))
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in menor_800k:
        print(f"{nombre}\t${sueldo}")
    
    print("\nSueldos entre $800.000 y $2.000.000")
    print("TOTAL:", len(entre_800k_y_2m))
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in entre_800k_y_2m:
        print(f"{nombre}\t${sueldo}")
    
    print("\nSueldos superiores a $2.000.000")
    print("TOTAL:", len(mayor_2m))
    print("Nombre empleado\tSueldo")
    for nombre, sueldo in mayor_2m:
        print(f"{nombre}\t${sueldo}")
    
    total_sueldos = sum(sueldos)
    print("\nTOTAL SUELDOS: $", total_sueldos)


def ver_estadisticas(sueldos):
    sueldo_max = max(sueldos)
    sueldo_min = min(sueldos)
    promedio = sum(sueldos) / len(sueldos)
    

    media_geom = 1
    for sueldo in sueldos:
        media_geom *= sueldo
    media_geom **= (1 / len(sueldos))
    
    print("Sueldo más alto:", sueldo_max)
    print("Sueldo más bajo:", sueldo_min)
    print("Promedio de sueldos:", promedio)
    print("Media geométrica de sueldos:", media_geom)


def reporte_sueldos(sueldos):
    descuento_salud = 0.07
    descuento_afp = 0.12
    
    print("Nombre empleado\tSueldo Base\tDescuento Salud\tDescuento AFP\tSueldo Líquido")
    with open('reporte_sueldos.csv', mode='w', newline='') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Nombre empleado', 'Sueldo Base', 'Descuento Salud', 'Descuento AFP', 'Sueldo Líquido'])
        
        for i in range(10):
            nombre = trabajadores[i]
            sueldo = sueldos[i]
            desc_salud = sueldo * descuento_salud
            desc_afp = sueldo * descuento_afp
            sueldo_liquido = sueldo - desc_salud - desc_afp
            
            print(f"{nombre}\t${sueldo}\t${desc_salud:.2f}\t${desc_afp:.2f}\t${sueldo_liquido:.2f}")
            writer.writerow([nombre, sueldo, desc_salud, desc_afp, sueldo_liquido])


def main():
    sueldos = None
    while True:
        print("\n---- MENÚ ----")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            sueldos = asignar_sueldos_aleatorios()
            print("Sueldos aleatorios asignados.")
        elif opcion == '2':
            if sueldos:
                clasificar_sueldos(sueldos)
            else:
                print("Primero debe asignar sueldos aleatorios (opción 1).")
        elif opcion == '3':
            if sueldos:
                ver_estadisticas(sueldos)
            else:
                print("Primero debe asignar sueldos aleatorios (opción 1).")
        elif opcion == '4':
            if sueldos:
                reporte_sueldos(sueldos)
                print("Reporte generado en reporte_sueldos.csv")
            else:
                print("Primero debe asignar sueldos aleatorios (opción 1).")
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción del 1 al 5.")

if __name__ == "__main__":
    main()

