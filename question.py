import preguntas as p
import random
from shuffle import shuffle_alt

# Opciones dadas para escoger.
###############################################
opciones = {'basicas': set([1,2,3]),
            'intermedias': set([1,2,3]),
            'avanzadas': set([1,2,3])}
###############################################

def choose_q(dificultad):
    # Paso 5: Llamar al pool de preguntas de dificultad.
    #escoger preguntas por dificultad
    preguntas = p.pool_preguntas[dificultad]
    # Paso 6: Se debe escoger alguna de las opciones disponibles.
    
    # usar opciones desde ambiente global
    global opciones
    # escoger una pregunta
    n_elegido = random.choice(list(opciones[dificultad]))
    # eliminarla del ambiente global para no escogerla de nuevo
    opciones[dificultad].remove(n_elegido)
    
    # Paso 7: Desacoplar la pregunta en enunciado según la opción escogida y su respectivas alternativas mezcladas con la función shuffle_alt().
    pregunta = preguntas[f'pregunta_{n_elegido}']
    alternativas = shuffle_alt(pregunta)
    
    
    return pregunta['enunciado'], alternativas

if __name__ == '__main__':
    # si ejecuto el programa, las preguntas cambian de orden, pero nunca debieran repetirse
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')
    
    pregunta, alternativas = choose_q('basicas')
    print(f'El enunciado es: {pregunta}')
    print(f'Las alternativas son: {alternativas}')