# Gestion de bliblioteca.
# Una pequeña biblioteca necesita registrar sus libros en un sistema muy simple.

# Diccionario vacío al principio.
biblioteca = {}

# Ciclo de menú.
while True:  # Bucle infinito.
    print("\n MENÚ BIBLIOTECA")
    print("1. Agregar libro")  # Crear: Agrega nuevos libros al diccionario.
    print("2. Mostrar libro") # Leer: Muestra todos los libros almacenados.
    print("3. Buscar libro") # Buscar: Permite buscar un libro por su ID o Título.
    print("4. Actualizar libro") # Actualizar: Modifica la información de un libro dado su ID.
    print("5. Eliminar libro") # Eliminar: Elimina un libro de la biblioteca usando su ID.
    print("6. Salir")

    opcion = input("Seleccione una opción (1-6): ")

    # Opción 1: Agregar libro.
    if opcion == '1':
        id_libro = input("Digite el ID del libro: ")
        if id_libro in biblioteca:
            print("Ese ID ya existe.")
        else:
            titulo = input("Digite el título del libro: ")
            autor = input("Digite el autor del libro: ")
            año = int(input("Digite el año de publicación: "))
            biblioteca[id_libro] = {'titulo': titulo, 'autor': autor, 'año': año}
            print("Libro agregado.")

    # Opción 2: Mostrar todos los libros.
    elif opcion == '2':
        if len(biblioteca) == 0: # Devuelve el número de elementos de un objeto iterable como una lista, tupla, cadena o diccionario.
            print("La biblioteca está vacía.")
        else:
            print("\n--- Lista de libros ---")
            for id_libro in biblioteca:
                datos = biblioteca[id_libro]
                print(f"ID: {id_libro} | Título: {datos['titulo']} | Autor: {datos['autor']} | Año: {datos['año']}")

    # Opción 3: Buscar libro.
    elif opcion == '3':
        valor = input("Buscar por ID o Título: ").lower() # Es un método de cadena que convierte todos los caracteres de una cadena a minúsculas. 
        encontrado = False
        for id_libro in biblioteca:
            datos = biblioteca[id_libro]
            if id_libro == valor or datos['titulo'].lower() == valor:
                print(f"ID: {id_libro} | Título: {datos['titulo']} | Autor: {datos['autor']} | Año: {datos['año']}")
                encontrado = True
                break  # Interrumpir la ejecución de bucle.
        if not encontrado:
            print("Libro no encontrado.")

    # Opción 4: Actualizar libro.
    elif opcion == '4':
        id_libro = input("Digite el ID del libro a actualizar: ")
        if id_libro in biblioteca:
            print("Deje en blanco si no desea cambiar un dato.")
            nuevo_titulo = input("Nuevo título: ")
            nuevo_autor = input("Nuevo autor: ")
            nuevo_año = input("Nuevo año: ")

            if nuevo_titulo != "":
                biblioteca[id_libro]['titulo'] = nuevo_titulo
            if nuevo_autor != "":
                biblioteca[id_libro]['autor'] = nuevo_autor
            if nuevo_año != "":
                biblioteca[id_libro]['año'] = int(nuevo_año)
            print("Libro actualizado.")
        else:
            print("No se encontró ese ID.")

    # Opción 5: Eliminar libro.
    elif opcion == '5':
        id_libro = input("Digite el ID del libro a eliminar: ")
        if id_libro in biblioteca:
            del biblioteca[id_libro] # Se utiliza para eliminar referencias a objetos.
            print("Libro eliminado.")
        else:
            print("No se encontró ese ID.")

    # Opción 6: Salir del programa.
    elif opcion == '6':
        print("Gracias por usar la biblioteca.")
        break # Interrumpir la ejecución de bucle.
    # Si el usuario elige algo incorrecto.
    else:
        print("Opción no válida. Intente de nuevo.")

