from logica.analizador_regex import AnalizadorRegex
from logica.motor_validacion import MotorValidacion

if __name__ == "__main__":
    # Ingresar la expresión regular y la cadena
    expresion = "(a|b)*abb"
    cadena = "aabb"

    # Crear el analizador y compilar la expresión regular
    analizador = AnalizadorRegex(expresion)
    if analizador.compilar_regex():
        # Crear el motor de validación
        motor = MotorValidacion(analizador)

        # Validar la cadena con el motor
        resultado = motor.validar(cadena)
        print(f"La cadena '{cadena}' {'es aceptada' if resultado else 'es rechazada'} por la expresion '{expresion}'.")
 