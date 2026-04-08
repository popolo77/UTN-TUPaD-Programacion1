# %% [markdown]
# <!-- Ejercicio 5 — “Escape Room:"La Arena del Gladiador" -->

# %%
print("--- BIENVENIDO A LA ARENA ---")

gladiador = input("Ingrese nombre de Gladiador: ")

while not gladiador.isalpha():
    print("Error: Solo se permiten letras")
    gladiador = input("Ingrese nombre de Gladiador: ")

vida_gladiador=100
vida_enemigo=100
pocion=3
daño_base_atq=15
daño_base_ene=12

while vida_gladiador > 0 and vida_enemigo > 0:
    print(f"Vida {gladiador}: {vida_gladiador} Vida Enemigo: {vida_enemigo}  Poción: {pocion}")
    print("1 - Ataque Pesado 2 - Ráfaga Veloz 3 - Curar ")
    opcion_menu = input("Ingrese una opción: ")

    while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 3:
        print("Error ingrese un número del 1 al 3")
        print("1 - Ataque Pesado 2 - Ráfaga Veloz 3 - Curar ")
        opcion_menu = input("Ingrese una opción: ")

    if int(opcion_menu) == 1:
        if vida_enemigo < 20:
            golpe_cri = float(daño_base_atq * 1.5)
            vida_enemigo -= golpe_cri
            print(f"¡Atacaste al enemigo por {golpe_cri} puntos de daño!")
        else:
            vida_enemigo -= daño_base_atq
            print(f"¡Atacaste al enemigo por {daño_base_atq} puntos de daño!")
    
    if int(opcion_menu) == 2:
        for x in range(3):
            vida_enemigo -= 5
            print(" > Golpe conectado por 5 de daño")
        else:
            vida_enemigo -= daño_base_atq
            print(f"¡Atacaste al enemigo por {daño_base_atq} puntos de daño!")
    
    if int(opcion_menu) == 3:
        if pocion > 0:
            vida_gladiador += 30
            pocion -= 1
        else:
            print("No tienes pociones")
    vida_gladiador -= daño_base_ene
    print("¡El enemigo te atacó por 12 puntos de daño!")
    
if vida_gladiador > 0:
        print(f"VICTORIA! {gladiador} ha ganado la batalla")
if vida_enemigo >= 0:
        print("DERROTA! Has caído en combate")


# %% [markdown]
# <!-- Ejercicio 4 — “Escape Room: La Bóveda” -->
# 

# %%
energia = 100
tiempo = 12
cerraduras_abiertas = 0
alarma = False
codigo_parcial = ""
anti_spam = 0

nombre_agente = input("Ingrese nombre de agente: ")
while not nombre_agente.isalpha():
    print("Error! Ingrese nombre solo con letras")
    nombre_agente = input("Ingrese nombre de agente: ")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:

    print(f"Energía: {energia} | Tiempo: {tiempo} | Cerraduras: {cerraduras_abiertas}")
    print("1- Forzar Cerradura")
    print("2- Hackear Panel")
    print("3- Descansar")

    opcion_menu = input("Ingrese Acción: ")

    while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 3:
        opcion_menu = input("Ingrese Acción válida (1-3): ")

    if int(opcion_menu) == 1:
        energia -= 20
        tiempo -= 2

        if energia < 40:
            num_for = input("Ingrese un número entre 1 y 3: ")
            while not num_for.isdigit() or int(num_for) < 1 or int(num_for) > 3:
                num_for = input("Debe ser un número entre 1 y 3: ")

            if int(num_for) == 3:
                alarma = True

        
        anti_spam += 1

        if anti_spam == 3:
            alarma = True

        
        if not alarma:
            cerraduras_abiertas += 1

    elif int(opcion_menu) == 2:
        energia -= 10
        tiempo -= 3

        for x in range(4):
            codigo_parcial += "A"
            print(codigo_parcial)

        if len(codigo_parcial) >= 8:
            cerraduras_abiertas += 1

        anti_spam = 0

    elif int(opcion_menu) == 3:
        energia += 15
        tiempo -= 1

        if alarma:
            energia -= 10

        if energia > 100:
            energia = 100

        anti_spam = 0


# RESULTADO FINAL
if cerraduras_abiertas == 3:
    print("VICTORIA")

elif alarma and tiempo <= 3:
    print("DERROTA, BLOQUEO")

elif energia <= 0 or tiempo <= 0:
    print("DERROTA")

# %% [markdown]
# <!-- Ejercicio 1— “Caja del Kiosco” -->
# 

# %%
total_desc = 0
total_sin_desc = 0

nombre = input("Ingrese su nombre: ")
while not nombre.isalpha():
    nombre = input("Error! Ingrese su nombre: ")
cant_prod = input("Ingrese la cantidad de productos: ")
while not cant_prod.isdigit() or int(cant_prod) < 1:
    cant_prod = input("Error! Ingrese la cantidad de productos: ")
print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cant_prod}")
for x in range(int(cant_prod)):
    precio = input("Ingrese precio de producto: ")
    while not precio.isdigit():
        precio = input("Error! Ingrese precio de producto: ")
    desc = input("Posee el producto un descuento? S/N: ").upper()
    while desc !="S" and desc !="N":
        desc = input("Error! Posee el producto un descuento? S/N: ").upper()
    if desc == "S":
        precio_desc = int(precio) * 10 / 100
        total_desc += precio_desc
    total_sin_desc += int(precio)

    
    print(f"Producto {x+1} - Precio: ${precio} - Descuento (S/N): {desc} ")
print()
promedio = int(total_sin_desc) / int(cant_prod)
total_con_desc = total_sin_desc - total_desc
ahorro = total_desc
print(f"Total sin descuentos: ${total_sin_desc}")
print(f"Total con descuentos: ${total_con_desc}")
print(f"Ahorro: ${total_desc}")
print(f"Promedio por producto: ${promedio:.2f}")



# %% [markdown]
# <!-- Ejercicio 2 — “Acceso al Campus y Menú Seguro” -->
# 

# %%
usuario_correcto = "alumno"
clave_correcta = "Python123"

intentos = 0

usuario_ingresado = ""
clave_ingresada = ""

while (usuario_ingresado != usuario_correcto or clave_ingresada != clave_correcta) and intentos < 3:
    usuario_ingresado = input("Ingrese usuario: ")
    clave_ingresada = input("Ingrese clave: ")
    
    intentos += 1

    if usuario_ingresado != usuario_correcto or clave_ingresada != clave_correcta:
        print("Usuario o clave incorrectos")


if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
    print("Acceso concedido")
    
    opcion = 0
    while opcion != 4:
        opcion = input("1-Ver estado 2-Cambiar clave 3-Mensaje 4-Salir: ")
        
        while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4:
            opcion = input("Ingrese opción válida (1-4): ")

        if int(opcion) == 1:
            print("Estado del sistema OK")

        elif int(opcion) == 2:
            nueva_clave = input("Ingrese nueva clave: ")
            clave_correcta = nueva_clave
            print("Clave actualizada")

        elif int(opcion) == 3:
            print("Sigue así, vas bien!")

else:
    print("Cuenta bloqueada")

# %% [markdown]
# <!-- Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)” -->

# %%

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""


operador = input("Ingrese nombre del operador: ")
while not operador.isalpha():
    operador = input("Error! Ingrese nombre válido: ")

menu = 0

while menu != 5:

    print("\n1- Reservar turno")
    print("2- Cancelar turno")
    print("3- Ver agenda del día")
    print("4- Ver resumen")
    print("5- Cerrar sistema")

    menu = input("Ingrese opción: ")

    while not menu.isdigit() or int(menu) < 1 or int(menu) > 5:
        menu = input("Ingrese opción válida (1-5): ")

    
    if int(menu) == 1:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
            dia = input("Ingrese día válido: ")

        nombre = input("Ingrese nombre del paciente: ")
        while not nombre.isalpha():
            nombre = input("Error! Ingrese nombre válido: ")

        if int(dia) == 1:
            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                print("Paciente repetido")
            else:
                if lunes1 == "":
                    lunes1 = nombre
                elif lunes2 == "":
                    lunes2 = nombre
                elif lunes3 == "":
                    lunes3 = nombre
                elif lunes4 == "":
                    lunes4 = nombre
                else:
                    print("Sin lugar en Lunes")

        else:
            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                print("Paciente repetido")
            else:
                if martes1 == "":
                    martes1 = nombre
                elif martes2 == "":
                    martes2 = nombre
                elif martes3 == "":
                    martes3 = nombre
                else:
                    print("Sin lugar en Martes")

    
    elif int(menu) == 2:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")
        nombre = input("Ingrese nombre a cancelar: ")

        if int(dia) == 1:
            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            elif nombre == lunes3:
                lunes3 = ""
            elif nombre == lunes4:
                lunes4 = ""
            else:
                print("No encontrado")
        else:
            if nombre == martes1:
                martes1 = ""
            elif nombre == martes2:
                martes2 = ""
            elif nombre == martes3:
                martes3 = ""
            else:
                print("No encontrado")

    
    elif int(menu) == 3:
        dia = input("Ingrese día (1=Lunes, 2=Martes): ")

        if int(dia) == 1:
            print("Lunes:")
            print(f"Turno 1: {lunes1 if lunes1 else '(libre)'}")
            print(f"Turno 2: {lunes2 if lunes2 else '(libre)'}")
            print(f"Turno 3: {lunes3 if lunes3 else '(libre)'}")
            print(f"Turno 4: {lunes4 if lunes4 else '(libre)'}")
        else:
            print("Martes:")
            print(f"Turno 1: {martes1 if martes1 else '(libre)'}")
            print(f"Turno 2: {martes2 if martes2 else '(libre)'}")
            print(f"Turno 3: {martes3 if martes3 else '(libre)'}")

    
    elif int(menu) == 4:
        ocupados_lunes = 0
        if lunes1 != "": ocupados_lunes += 1
        if lunes2 != "": ocupados_lunes += 1
        if lunes3 != "": ocupados_lunes += 1
        if lunes4 != "": ocupados_lunes += 1

        ocupados_martes = 0
        if martes1 != "": ocupados_martes += 1
        if martes2 != "": ocupados_martes += 1
        if martes3 != "": ocupados_martes += 1

        print(f"Lunes: {ocupados_lunes} ocupados, {4 - ocupados_lunes} libres")
        print(f"Martes: {ocupados_martes} ocupados, {3 - ocupados_martes} libres")

        if ocupados_lunes > ocupados_martes:
            print("Lunes tiene más turnos")
        elif ocupados_martes > ocupados_lunes:
            print("Martes tiene más turnos")
        else:
            print("Empate")




