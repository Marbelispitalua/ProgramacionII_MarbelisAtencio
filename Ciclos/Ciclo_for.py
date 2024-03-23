Vuelo = {
"Aerolinea": "Avianca",
"Vuelo": "AV3102",
"Origen": "CARTAGENA",
"Destino": "EE.UU",
"Tipo_Maleta": ['Cabina', 'Mano', 'Bodega']
}

print("Valores del diccionario:")
for key, value in Vuelo.items():
    print(f"{key}: {value}")

print("\nValores de tipo de maleta:")
for maleta in Vuelo["Tipo_Maleta"]:
    print(maleta)