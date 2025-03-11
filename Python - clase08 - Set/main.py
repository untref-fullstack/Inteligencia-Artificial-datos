# USO DE SET

frutas = {"manzana", "pera", "naranja", "uva"}
print(frutas) 

frutas.add("uva")
print(frutas)

# Aplicando SET para limpiar duplicados
nombres = { "Fer", "July", "Greta", "Nico", "Laura", "Greta", "July" }

nombres_unicos = set(nombres)

print(nombres_unicos)

nombres = set({ "Fer", "July", "Greta", "Nico", "Laura", "Bianca", "Juampi" })

verificar = input("Ingresa el nombre a verificar: ")

if verificar:
    print(verificar in nombres)
else:
    print("⛔️ Debes ingresar un dato válido.")