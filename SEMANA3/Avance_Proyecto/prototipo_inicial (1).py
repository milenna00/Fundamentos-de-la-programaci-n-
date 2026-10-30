# ============================================================
# SISTEMA DE CAFETERIA
# Proyecto de la asignatura:Fundamentos de Programacion
# ============================================================

# Lista de productos y sus precios
productos = ["Cafe", "Sandwich", "Jugo"]
precios = [35.00, 45.00, 25.00]

# Variable para acumular las ventas del dia
total_dia = 0.00

# Menu principal
while True:
    print("\n===== SISTEMA DE CAFETERIA =====")
    print("1. Registrar pedido")
    print("2. Consultar ventas del dia")
    print("3. Salir")

    # Validacion de la opcion del menu
    try:
        opcion = int(input("Selecciona una opcion: "))
    except ValueError:
        print("Opcion no valida. Escribe un numero.")
        continue

    # ========================================================
    # OPCION 1: REGISTRAR PEDIDO
    # ========================================================
    if opcion == 1:

        # Solicitar nombre del cliente
        nombre = input("Nombre del cliente: ").strip()

        while nombre == "":
            print("El nombre no puede quedar vacio.")
            nombre = input("Nombre del cliente: ").strip()

        # Validar si el cliente es estudiante
        respuesta = input(
            "El cliente es estudiante? (S/N): "
        ).strip().lower()

        while respuesta not in ("s", "n"):
            print("Respuesta no valida. Escribe S o N.")
            respuesta = input(
                "El cliente es estudiante? (S/N): "
            ).strip().lower()

        es_estudiante = respuesta == "s"

        # Solicitar las cantidades de cada producto
        cantidades = []

        for producto in productos:
            while True:
                try:
                    cantidad = int(
                        input(
                            f"Cantidad de {producto.lower()}: "
                        )
                    )

                    if cantidad < 0:
                        print(
                            "La cantidad no puede ser negativa."
                        )
                    else:
                        cantidades.append(cantidad)
                        break

                except ValueError:
                    print(
                        "Ingresa una cantidad usando numeros enteros."
                    )

        # Calcular el subtotal
        subtotal = 0.00

        for i in range(len(productos)):
            subtotal += cantidades[i] * precios[i]

        subtotal = round(subtotal, 2)

        # Aplicar descuento del 10 % a estudiantes
        # cuando el subtotal sea igual o mayor a $150
        descuento = 0.00

        if es_estudiante and subtotal >= 150:
            descuento = round(subtotal * 0.10, 2)

        # Calcular IVA del 16 % despues del descuento
        iva = round((subtotal - descuento) * 0.16, 2)

        # Calcular total a pagar
        total = round(subtotal - descuento + iva, 2)

        # Acumular las ventas del dia
        total_dia = round(total_dia + total, 2)

        # Mostrar resumen del pedido
        print("\n===== RESUMEN DEL PEDIDO =====")
        print(f"Cliente: {nombre}")

        for i in range(len(productos)):
            importe = cantidades[i] * precios[i]

            print(
                f"{productos[i]}: {cantidades[i]} x "
                f"${precios[i]:.2f} = ${importe:.2f}"
            )

        print("------------------------------")
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"Descuento: ${descuento:.2f}")
        print(f"IVA (16%): ${iva:.2f}")
        print(f"Total a pagar: ${total:.2f}")

    # ========================================================
    # OPCION 2: CONSULTAR VENTAS DEL DIA
    # ========================================================
    elif opcion == 2:
        print(
            f"\nVentas acumuladas del dia: ${total_dia:.2f}"
        )

    # ========================================================
    # OPCION 3: SALIR DEL SISTEMA
    # ========================================================
    elif opcion == 3:
        print("\nCerrando el sistema.")
        print(f"Ventas finales del dia: ${total_dia:.2f}")
        break

    # ========================================================
    # OPCION NO VALIDA
    # ========================================================
    else:
        print("Opcion no valida. Selecciona 1, 2 o 3.")