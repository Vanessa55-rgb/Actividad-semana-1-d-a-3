#Agenda de contactos 
#Vas a construir una agenda que guarda información de contactos personales.
contactos = {}

# Ciclo del menú
while True:
    print("\nMENÚ CONTACTOS")
    print("1. Agregar contacto")  # Crear: Agrega contacto.
    print("2. Mostrar contacto")  # Leer: Muestra todos los contactos almacenados.
    print("3. Buscar contacto")  # Buscar: Permite buscar un contacto.
    print("4. Actualizar contacto")  # Actualizar: Modifica la información de contacto.
    print("5. Eliminar contacto") # Eliminar: Elimina un contacto.
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    # Opción 1: Agregar contacto
    if opcion == '1':
        nombre = input("Digite el nombre del contacto: ")
        if nombre in contactos:
            print("El contacto ya existe.")
        else:
            telefono = input("Digite el número de teléfono (10 dígitos): ")
            if len(telefono) != 10 or not telefono.isdigit():  # Validación: debe tener exactamente 10 dígitos numéricos
                print("Número inválido. Debe tener exactamente 10 dígitos numéricos.")
            else:
                email = input("Digite el email del contacto: ")
                contactos[nombre] = {'telefono': telefono, 'email': email}  # Se guarda el contacto con el nombre como clave
                print("Contacto agregado.")

    # Opción 2: Mostrar todos los contactos
    elif opcion == '2':
        if len(contactos) == 0:
            print("La lista de contactos está vacía.")
        else:
            print("\n--- Lista de contactos ---")
            for nombre, datos in contactos.items():  # .items() permite recorrer las claves y valores del diccionario
                print(f"Nombre: {nombre} | Teléfono: {datos['telefono']} | Email: {datos['email']}")

    # Opción 3: Buscar contacto por nombre
    elif opcion == '3':
        valor = input("Buscar por nombre: ").lower()  # Se convierte a minúsculas para hacer la búsqueda sin importar mayúsculas/minúsculas
        encontrado = False
        for nombre, datos in contactos.items():
            if nombre.lower() == valor:
                print(f"Nombre: {nombre} | Teléfono: {datos['telefono']} | Email: {datos['email']}")
                encontrado = True
                break  # Se detiene el ciclo si se encuentra el contacto
        if not encontrado:
            print("Contacto no encontrado.")

    # Opción 4: Actualizar contacto
    elif opcion == '4':
        nombre = input("Digite el nombre del contacto a actualizar: ")
        if nombre in contactos:
            print("Deje en blanco si no desea cambiar un dato.")
            nuevo_telefono = input("Nuevo teléfono (10 dígitos): ")
            nuevo_email = input("Nuevo email: ")

            if nuevo_telefono != "":
                if len(nuevo_telefono) == 10 and nuevo_telefono.isdigit():  # Se valida el nuevo número si se proporciona
                    contactos[nombre]['telefono'] = nuevo_telefono
                else:
                    print("Número inválido. No se actualizó el teléfono.")
            if nuevo_email != "":
                contactos[nombre]['email'] = nuevo_email
            print("Contacto actualizado.")
        else:
            print("No se encontró el contacto.")

    # Opción 5: Eliminar contacto
    elif opcion == '5':
        nombre = input("Digite el nombre del contacto a eliminar: ")
        if nombre in contactos:
            del contactos[nombre]  # Se elimina el contacto del diccionario
            print("Contacto eliminado.")
        else:
            print("No se encontró el contacto.")

    # Opción 6: Salir del programa
    elif opcion == '6':
        print("Gracias por usar la lista de contactos.")
        break

    # Opción inválida
    else:
        print("Opción no válida. Intente de nuevo.")
