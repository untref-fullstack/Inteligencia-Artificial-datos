from tabulate import tabulate

lenguajes = ['Python', 'JavaScript', 'Java', 'C++', 'Ruby', 'Swift', 'PHP', 'GoLang', 'Rust', 'Kotlin']

def listar_lenguajes():
    tabla = [[id + 1, lenguajes] for id, lenguajes in enumerate(lenguajes)]
    import os 
    os.system('clear')
    print("")
    print(tabulate(tabla, headers=['Id', 'Lenguajes de programación']))
    print("")

listar_lenguajes()