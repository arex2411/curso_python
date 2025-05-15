nombres = ["ana","hugo","valeria"]
edades=(65,29,42)
ciudades=["lima ","madrid","mexico"]

combinados=list(zip(nombres,edades,ciudades))
for nombres,edades,ciudades in combinados:
    print((f"{nombres} tiene {edades} años y vive en {ciudades}"))