import sys

# Autor: Fran Fdz. Guardia <ffergua056@g.educaand.es>

var = sys.argv[1] if len(sys.argv) > 1 else "Mundo" 
# El valor por defecto es Mundo
print(f"Hola {var}")
