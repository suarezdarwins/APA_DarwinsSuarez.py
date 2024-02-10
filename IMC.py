# Solicitar datos al usuario
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

    # Calcular IMC
    imc = calcular_imc(peso, altura)
    
    # Evaluar y mostrar mensaje
    evaluar_imc(imc)

def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC).
    
    Args:
    - peso (float): Peso en kilogramos.
    - altura (float): Altura en metros.
    
    Returns:
    - float: Valor del IMC.
    """
    imc = peso / (altura ** 2)
    return imc

def evaluar_imc(imc):
    """
    Evalúa el IMC y proporciona un mensaje de alerta o felicitación.
    
    Args:
    - imc (float): Índice de Masa Corporal.
    """
    if imc < 18.5:
        print("Tu IMC es {:.2f}, estás por debajo del peso normal. ¡Cuida tu salud!".format(imc))
    elif 18.5 <= imc < 25:
        print("Tu IMC es {:.2f}, estás dentro del rango de peso normal. ¡Felicidades por mantener tu salud!".format(imc))
    elif 25 <= imc < 30:
        print("Tu IMC es {:.2f}, estás en sobrepeso. ¡Cuida tu salud!".format(imc))
    else:
        print("Tu IMC es {:.2f}, estás en una categoría de obesidad. ¡Cuida tu salud y consulta a un profesional!".format(imc))


