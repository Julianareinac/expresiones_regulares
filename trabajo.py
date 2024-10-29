import tkinter as tk
from tkinter import messagebox
import re
import unittest


class RegexValidatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Validador de Expresiones Regulares")

        # Etiquetas y campos de entrada
        tk.Label(root, text="Expresión Regular:").grid(row=0, column=0, padx=10, pady=5)
        self.regex_entry = tk.Entry(root, width=50)
        self.regex_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Cadenas (una por línea):").grid(row=1, column=0, padx=10, pady=5)
        self.strings_entry = tk.Text(root, height=10, width=50)
        self.strings_entry.grid(row=1, column=1, padx=10, pady=5)

        # Botón de validación
        self.validate_button = tk.Button(root, text="Validar", command=self.validate)
        self.validate_button.grid(row=2, column=1, padx=10, pady=5, sticky="e")

        # Área de resultados
        tk.Label(root, text="Resultados:").grid(row=3, column=0, padx=10, pady=5)
        self.result_area = tk.Text(root, height=10, width=50, state="disabled")
        self.result_area.grid(row=3, column=1, padx=10, pady=5)

        # Botón para mostrar la explicación de la expresión regular
        self.explain_button = tk.Button(root, text="Explicar Expresión", command=self.explain_regex)
        self.explain_button.grid(row=4, column=1, padx=10, pady=5, sticky="e")

    def validate(self):
        # Obtener la expresión regular y las cadenas
        regex = self.regex_entry.get()
        strings = self.strings_entry.get("1.0", tk.END).strip().splitlines()

        # Limpiar el área de resultados
        self.result_area.config(state="normal")
        self.result_area.delete("1.0", tk.END)

        try:
            pattern = re.compile(regex)  # Compilar la expresión regular
        except re.error as e:
            messagebox.showerror("Error", f"Expresión regular inválida: {e}")
            return

        # Validar cada cadena
        results = []
        for string in strings:
            if pattern.fullmatch(string):
                results.append(f"'{string}' es aceptada.")
            else:
                results.append(f"'{string}' es rechazada.")

        # Mostrar los resultados
        self.result_area.insert(tk.END, "\n".join(results))
        self.result_area.config(state="disabled")

    def explain_regex(self):
        regex = self.regex_entry.get()
        explanation = self._explain_regex_helper(regex)

        # Mostrar la explicación en un cuadro de diálogo
        messagebox.showinfo("Explicación de la Expresión Regular", explanation)

    def _explain_regex_helper(self, pattern):
        explanations = {
            ".": "cualquier carácter",
            "*": "cero o más repeticiones",
            "+": "una o más repeticiones",
            "?": "cero o una repetición",
            "\\d": "un dígito",
            "\\w": "cualquier carácter alfanumérico",
            "\\s": "un espacio en blanco"
            # Puedes agregar más símbolos aquí...
        }
        explanation = []
        for symbol in pattern:
            if symbol in explanations:
                explanation.append(f"{symbol}: {explanations[symbol]}")
            else:
                explanation.append(f"{symbol}: símbolo desconocido o literal")
        return "\n".join(explanation)


# Pruebas unitarias
class TestRegexValidator(unittest.TestCase):
    def test_valid_regex(self):
        pattern = re.compile(r"\d{3}-\d{2}-\d{4}")
        self.assertTrue(pattern.fullmatch("123-45-6789"))
        self.assertFalse(pattern.fullmatch("123-456-789"))

    def test_invalid_regex(self):
        with self.assertRaises(re.error):
            re.compile(r"(\d{3-}")


# Correr la aplicación
if __name__ == "__main__":
    # Crear la ventana de la aplicación
    root = tk.Tk()
    app = RegexValidatorApp(root)
    root.mainloop()

    # Correr las pruebas unitarias
    unittest.main(exit=False)
