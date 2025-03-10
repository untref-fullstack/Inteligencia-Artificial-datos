from tabulate import tabulate

# Listas de estudiantes en dos cursos
curso_A = ["Ana", "Juan", "Pedro", "María", "Sofía", "Lucas"]
curso_B = ["Lucas", "María", "Carlos", "Sofía", "Elena", "Roberto"]

def crear_conjunto(lista):
    """Convierte una lista en un conjunto para eliminar duplicados."""
    return set(lista)

def union_conjuntos(conjunto1, conjunto2):
    """Devuelve la unión de dos conjuntos."""
    return conjunto1 | conjunto2

def interseccion_conjuntos(conjunto1, conjunto2):
    """Devuelve la intersección de dos conjuntos."""
    return conjunto1 & conjunto2

def mostrar_resultados(conjunto1, conjunto2, union, interseccion):
    """Muestra los conjuntos y sus operaciones en una tabla."""
    datos = [
        ["Curso A", ", ".join(conjunto1)],
        ["Curso B", ", ".join(conjunto2)],
        ["Unión", ", ".join(union)],
        ["Intersección", ", ".join(interseccion)]
    ]
    
    print(tabulate(datos, headers=["Operación", "Resultado"], tablefmt="pipe"))

# Creación de conjuntos
set_A = crear_conjunto(curso_A)
set_B = crear_conjunto(curso_B)

# Operaciones de conjuntos
union = union_conjuntos(set_A, set_B)
interseccion = interseccion_conjuntos(set_A, set_B)

# Mostrar resultados
mostrar_resultados(set_A, set_B, union, interseccion)
