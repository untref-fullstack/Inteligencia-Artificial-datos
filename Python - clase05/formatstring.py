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
        print(f'{indice + 1} - {lang}')

# enumerar_lenguajes()

