import preguntas as p
import random

def shuffle_alt(pregunta):
    #mezclar alternativas
    #######################################################################
     # Paso 4: Tomar de las preguntas sólo la clave correspondiente a alternativas y estas deben ser mezcladas.

    alternativas = pregunta['alternativas']
    random.shuffle(alternativas)
    return alternativas
    
    
    
    #######################################################################
    

if __name__ == '__main__':
    # si se ejecuta el  programa varias veces las alternativas debieran aparecer en distinto orden
    pregunta_ejemplo = p.pool_preguntas['basicas']['pregunta_1']
    alternativas_mezcladas = shuffle_alt(pregunta_ejemplo)
    print("Alternativas mezcladas:", alternativas_mezcladas)
    # a modo de ejemplo
    # [['alt_1', 0], ['alt_3', 0], ['alt_2', 1], ['alt_4', 0]]