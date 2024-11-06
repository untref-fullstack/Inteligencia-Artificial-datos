from tabulate import tabulate

productos_electronicos = [
    {'id': 1, 'nombre': 'Notebook i5', 'importe': 920, 'categoria': 'Portátiles'},
    {'id': 2, 'nombre': 'Macbook Air M2', 'importe': 1100, 'categoria': 'Portátiles'},
    {'id': 3, 'nombre': 'Lenovo IdeaPad 3', 'importe': 750, 'categoria': 'Portátiles'},
    {'id': 4, 'nombre': 'HP Pavilion 15', 'importe': 800, 'categoria': 'Portátiles'},
    {'id': 5, 'nombre': 'Asus VivoBook 14', 'importe': 780, 'categoria': 'Portátiles'},
    {'id': 6, 'nombre': 'Dell Inspiron 15', 'importe': 850, 'categoria': 'Portátiles'},
    {'id': 7, 'nombre': 'Acer Aspire 5', 'importe': 700, 'categoria': 'Portátiles'},
    {'id': 8, 'nombre': 'Microsoft Surface Laptop 4', 'importe': 1300, 'categoria': 'Portátiles'},
    {'id': 9, 'nombre': 'Razer Blade Stealth', 'importe': 1400, 'categoria': 'Portátiles'},
    {'id': 10, 'nombre': 'Samsung Galaxy Book Pro', 'importe': 1200, 'categoria': 'Portátiles'},
]


def limpiar_pantalla():
    import os

    if os.__name__ == 'MacOS' or 'Linux':
        os.system('clear')
    else:
        os.system('cls')

