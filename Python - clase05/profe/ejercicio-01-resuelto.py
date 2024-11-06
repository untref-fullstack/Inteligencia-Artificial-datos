lenguajes = ['Python', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'Kotlin', 'Swift', 'Dart', 'Ruby', 'Elixir']
sistemas_operativos = ['Windows', 'MacOS', 'Linux''Android', 'iOS']
stacks = ['MERN', 'MEAN', 'MEVN', 'LAMP / XAMP', 'Django', 'Ruby on Rails', 'Flutter', 'Serverless', 'Jamstack']

def listar_lenguajes():
    if len(lenguajes) > 0:
        for lang in lenguajes:
            print(lang)

def listar_so():
    if len(sistemas_operativos) > 0:
        for so in sistemas_operativos:
            print(so)

def listar_stacks():
    if len(stacks) > 0:
        for stack in stacks:
            print(stack)

def limpiar_pantalla():
    import os

    if (os.system.__name__ == 'MacOS' or 'Linux'):
        os.system('clear')
    else:
        os.system('cls')

def mostrar_menu():
    limpiar_pantalla()

    opcion = 9

    while opcion != 0:
        print('')
        print('1. Listar lenguajes de programación')
        print('2. Listar sistemas operativos')
        print('3. Listar stacks tecnológicos')
        print('0. Para salir')

        seleccion = input('Ingresa la opción a visualizar:')

        if seleccion == '1':
            limpiar_pantalla()
            listar_lenguajes()
            
            accion = input('Ingresa cualquier caracter para continuar:')

            if accion.strip() != '':
                mostrar_menu()
            else:
                print('⛔️ Opción incorrecta.')
        elif seleccion == '2':
            limpiar_pantalla()
            listar_so()
            
            accion = input('Ingresa cualquier caracter para continuar:')

            if accion.strip() != '':
                mostrar_menu()
            else:
                print('⛔️ Opción incorrecta.')
        elif seleccion == '3':
            limpiar_pantalla()
            listar_stacks()
            
            accion = input('Ingresa cualquier caracter para continuar:')

            if accion.strip() != '':
                mostrar_menu()
            else:
                print('⛔️ Opción incorrecta.')

        elif seleccion == '0':
            print("Saliendo del programa...")
            break  # Esto corta el ciclo while

        else:
            print('⛔️ Opción incorrecta.')

mostrar_menu()

print("Programa finalizado.")