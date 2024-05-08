class Diccionario:
    def __init__(self):
        self.diccionario = {}

    def agregar_palabra(self, palabra, definiciones):
        if palabra not in self.diccionario:
            self.diccionario[palabra] = definiciones
            print(f'Se ha agregado la palabra "{palabra}" al diccionario.')
        else:
            print(f'La palabra "{palabra}" ya existe en el diccionario.')

    def mostrar_diccionario(self):
        if self.diccionario:
            print("Diccionario:")
            for palabra, definiciones in self.diccionario.items():
                print(f"{palabra}:")
                for definicion, significado in definiciones.items():
                    print(f" - {definicion}: {significado}")
        else:
            print("El diccionario está vacío.")

    def modificar_definicion(self, palabra, definicion, nuevo_significado):
        if palabra in self.diccionario and definicion in self.diccionario[palabra]:
            self.diccionario[palabra][definicion] = nuevo_significado
            print(f'Se ha modificado la definición de "{definicion}" para la palabra "{palabra}".')
        else:
            print(f'La palabra "{palabra}" o la definición "{definicion}" no existen en el diccionario.')

    def eliminar_definicion(self, palabra, definicion):
        if palabra in self.diccionario and definicion in self.diccionario[palabra]:
            del self.diccionario[palabra][definicion]
            print(f'Se ha eliminado la definición "{definicion}" de la palabra "{palabra}".')
        else:
            print(f'La palabra "{palabra}" o la definición "{definicion}" no existen en el diccionario.')

    def eliminar_palabra(self, palabra):
        if palabra in self.diccionario:
            del self.diccionario[palabra]
            print(f'Se ha eliminado la palabra "{palabra}" del diccionario.')
        else:
            print(f'La palabra "{palabra}" no existe en el diccionario.')

def main():
    diccionario = Diccionario()

    while True:
        print("\nBienvenido al Llibre de les Accepcions")
        print("1. Agregar palabra")
        print("2. Mostrar diccionario")
        print("3. Modificar definición")
        print("4. Eliminar definición")
        print("5. Eliminar palabra")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            palabra = input("Introduce la palabra: ")
            num_definiciones = int(input("¿Cuántas definiciones tiene esta palabra?: "))
            definiciones = {}
            for _ in range(num_definiciones):
                definicion = input("Introduce la definición: ")
                significado = input("Introduce el significado: ")
                definiciones[definicion] = significado
            diccionario.agregar_palabra(palabra, definiciones)
        elif opcion == "2":
            diccionario.mostrar_diccionario()
        elif opcion == "3":
            palabra = input("Introduce la palabra: ")
            definicion = input("Introduce la definición que quieres modificar: ")
            nuevo_significado = input("Introduce el nuevo significado: ")
            diccionario.modificar_definicion(palabra, definicion, nuevo_significado)
        elif opcion == "4":
            palabra = input("Introduce la palabra: ")
            definicion = input("Introduce la definición que quieres eliminar: ")
            diccionario.eliminar_definicion(palabra, definicion)
        elif opcion == "5":
            palabra = input("Introduce la palabra que quieres eliminar: ")
            diccionario.eliminar_palabra(palabra)
        elif opcion == "6":
            print("Gracias por usar el Llibre de les Accepcions. Adéu!")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

if __name__ == "__main__":
    main()
