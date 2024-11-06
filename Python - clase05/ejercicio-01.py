lenguajes = ['Python', 'JavaScript', 'TypeScript', 'Go', 'Rust', 'Kotlin', 'Swift', 'Dart', 'Ruby', 'Elixir']
sistemas_operativos = ['Windows', 'MacOS', 'Linux''Android', 'iOS']
stacks = ['MERN', 'MEAN', 'MEVN', 'LAMP / XAMP', 'Django', 'Ruby on Rails', 'Flutter', 'Serverless', 'Jamstack']

def limpiar_pantalla():
    import os

    if (os.system.__name__ == 'MacOS' or 'Linux'):
        os.system('clear')
    else:
        os.system('cls')

