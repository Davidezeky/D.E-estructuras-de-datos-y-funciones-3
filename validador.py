
def validate(opciones, eleccion):
    # Definir validación de eleccion
      # Paso 1: Un ciclo while que no termine si es que la elección dada no es parte de las opciones.
    while eleccion not in opciones:
    # Paso 2:  solicitar mediante input una elección nueva que sí esté entre las opciones dadas
     eleccion = input('Opción no válida, ingrese una de las opciones válidas: ')
    return eleccion


if __name__ == '__main__':
    
    eleccion = input('Ingresa una Opción: ').lower()
    # letras = ['a','b','c','d'] # pueden probar con letras también para verificar su funcionamiento.
    numeros = ['0','1','2','3']
    # Si se ingresan valores no validos a eleccion debe seguir preguntando
    eleccion_validada = validate(numeros, eleccion)
    print("Eleccion validada:", eleccion_validada)
    
