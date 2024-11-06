universidad = {
    'nombre': 'Untref',
    'sedes': ['Caseros', 'Aromos', 'CABA', 'Villa Lynch', 'Saenz Peña']
}

import os

productos_electronicos = [{'id': 1, 'nombre': 'Notebook i5', 'importe': 920, 'categoria': 'Portátiles'},
                          {'id': 2, 'nombre': 'Macbook Air M2', 'importe': 1100, 'categoria': 'Portátiles'},
                          ]

def listar_productos():
    if len(productos_electronicos) > 0:
        for producto in productos_electronicos:
            print(f'ID: {producto['id']}, Nombre: {producto['nombre']}, Importe: $ {producto['importe']}')
        else:
            print('')

if os.__name__ == 'MacOS' or 'Linux':
    os.system('clear')
else:
    os.system('cls')


# listar_productos() # llamar la función para listar productos