from datetime import datetime

print("Iniciando app de Python dentro del contenedor...")
a, b = 7, 8
print(f"La suma es {a + b}")
print("Y la fecha es:", datetime.now().strftime("%d/%m/%Y"))
