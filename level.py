def choose_level(n_pregunta, p_level):
    
    # Paso 3: número de pregunta y las preguntas por nivel mediante un if/elif/else
    if p_level == 1:
        return 'basicas'
    elif p_level == 2:
        if n_pregunta <= 2:
            return 'basicas'
        elif 3 <= n_pregunta <= 4:
            return 'intermedias'
        elif 5 <= n_pregunta <= 6:
            return 'avanzadas'
    elif p_level == 3:
        if n_pregunta <= 3:
            return 'basicas'
        elif 4 <= n_pregunta <= 6:
            return 'intermedias'
        elif 7 <= n_pregunta <= 9:
            return 'avanzadas'

if __name__ == '__main__':
    # verificar resultados
    print(choose_level(2, 2)) # básicas
    print(choose_level(3, 2)) # intermedias
    print(choose_level(7, 2)) # avanzadas
    print(choose_level(4, 3)) # intermedias