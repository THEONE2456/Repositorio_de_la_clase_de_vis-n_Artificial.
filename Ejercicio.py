Nombre = str(input("¿cual_es_tu_nombre?"))
#X = "¿cual_es_tu_nombre?" #redundando
#print(X) #redumdando
Sueldo = int(input("¿cuanto_ganas_al_mes?"))
#Y = "¿cuanto_ganas_al_mes?"
#print("Y")
Renta = int(input("¿cuanto_gastas_en_renta?"))
#Z = "¿cuanto_gastas_en_renta?"
#print("Z")
Comida = int(input("¿cuanto_gastas_en_comida?"))
#W = "¿cuanto_gastas_en_comida?"
#print("W")
Pasaje = int(input("¿cuanto_gastas_en_transporte?"))
#Ø = "¿cuanto_gastas_en_transporte?"
#print("Ø")

gastosTotales = Renta + Comida + Pasaje
restante = Sueldo - gastosTotales

print(f"Hola, {Nombre}, tus gastos totales fueron {gastosTotales} y te queda {restante}")


#Dinero_total = int(input("X"))
#Dinero_restante = int(input("X-Y-Z-W-Ø"))
#print()
 