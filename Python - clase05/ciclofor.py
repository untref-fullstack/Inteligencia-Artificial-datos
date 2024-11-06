import os

lenguajes = ['C', 'C++', 'C#', 'Python', 'GoLang', 'JavaScript', 'Java', 'Rust']

def limpiar_pantalla():
    import os

    if (os.system.__name__ == 'MacOS' or 'Linux'):
        os.system('clear')
    else:
        os.system('cls')

def enumerar_lenguajes():
    limpiar_pantalla()

    for indice, lang in enumerate(lenguajes):
        print(str(indice) + ' - ' + lang)

def iterar_un_rango():
    limpiar_pantalla()

    for i in range(21):
        print('Iteración número: ' + str(i))

def listar_lenguajes():
    limpiar_pantalla()

    print('Lista de lenguajes:')

    for lang in lenguajes:
        print('➡️ ' + lang)
    else:
        print('✅ Iteración completada con éxito.')

# LLAMAR A LA FUNCIÓN PRINCIPAL

# iterar_un_rango() # iteración sobre rangos
# enumerar_lenguajes() # iteración sobre índices y elementos
# listar_lenguajes() # iteración sobre una lista
