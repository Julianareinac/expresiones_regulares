from logica.analizador_regex import AnalizadorRegex

class MotorValidacion:
    def __init__(self, analizador):
        self.analizador = analizador

    def validar(self, cadena):
        """Valida la cadena contra la expresión regular compilada."""
        if self.analizador.compilado:
            if self.analizador.compilado.fullmatch(cadena):
                return True
            else:
                return False
        else:
            print("No se ha compilado ninguna expresión regular válida.")
            return False