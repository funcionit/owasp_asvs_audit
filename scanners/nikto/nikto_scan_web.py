import subprocess

# Pedir al usuario la URL a analizar
url = input("Ingrese la URL a analizar: ")

# Ejecutar Nikto para realizar el análisis de la URL
output = subprocess.check_output(["nikto", "-h", url, "-output", "nikto_report.txt"])

# Imprimir la salida de la ejecución de Nikto
print(output.decode())

# Abrir el archivo de reporte generado por Nikto
subprocess.call(["xdg-open", "nikto_report.txt"])
