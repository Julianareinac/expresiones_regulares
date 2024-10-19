import re

class AnalizadorRegex:
    def __init__(self, regex):
        self.regex = regex
        self.compilado = None

    def compilar_regex(self):
        """Compila la expresión regular y maneja errores de sintaxis."""
        try:
            self.compilado = re.compile(self.regex)
            return True
        except re.error as e:
            print(f"Error en la expresión regular: {e}")
            return False