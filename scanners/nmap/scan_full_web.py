#La función urlparse de la biblioteca urllib.parse divide la URL en sus componentes: protocolo, dominio, ruta, etc. Luego, usamos el método geturl() para recuperar la URL completa, el atributo netloc para extraer el dominio y la función socket.gethostbyname para obtener la dirección IP correspondiente al dominio.
import socket
import os
import re
import nmap
import subprocess

from urllib.parse import urlparse

#--------------------------- URL - Domain - ip --------------------------------------
#Desde la url completa guarda en variable la url, dominio y la ip para más abajo usarlas
url = input("Ingrese la URL completa: ")
parsed_url = urlparse(url)

url_completa = parsed_url.geturl()
dominio = parsed_url.netloc.split(':')[0]
ip_dominio = socket.gethostbyname(dominio)

print("URL completa:", url_completa)
print("Dominio:", dominio)
print("IP del dominio:", ip_dominio)

#--------------------------- nmap --------------------------------------
#Usar todos los script de seguridad de nmap de Sql injections, java injections, command injections, xml injections, xss, xxs, csrf, ssrf, path transversal, y otros, para scanear el dominio de la variable dominio, ip, y url_completa, para este resultado sacar las vulnerabilidades encontradas y hacer un reporte de nombre nmap_result.txt
#Note that you may need to adjust the list of scripts to include the ones you want to run, and you may also need to modify the commands to suit your needs. Additionally, this code assumes that you have nmap installed on your system.
# path to nmap scripts directory
path = "/usr/share/nmap/scripts"
# target url
target = dominio

# list of scripts to run for web scanning
web_scripts = [
    "http-sql-injection.nse",
    #"http-java-naming-enum.nse",
    #"http-command-injection.nse",
    "http-dombased-xss.nse",
    "http-fileupload-exploiter.nse",
    "http-phpmyadmin-dir-traversal.nse",
    # add more scripts here as needed
]

# run web scanning scripts and save report
web_report = "nmap_web_report.txt"
web_command = f"nmap -sV -sC -p 80,443 --script={','.join(web_scripts)} {target} -oN {web_report}"
os.system(web_command)

# list of scripts to run for domain scanning
domain_scripts = [
    "dns-brute.nse",
    "dns-cache-snoop.nse",
    "dns-ip6-arpa-scan.nse",
    "dns-random-srcport.nse",
    "dns-service-discovery.nse",
    "dns-srv-enum.nse",
    # add more scripts here as needed
]

# run domain scanning scripts and save report
domain_report = "nmap_domain_report.txt"
domain_command = f"nmap -sV -sC -p 53 --script={','.join(domain_scripts)} {dominio} -oN {domain_report}"
os.system(domain_command)

# list of scripts to run for IP scanning
ip_scripts = [
    "http-iis-webdav-vuln.nse",
    "http-vuln-cve2010-2861.nse",
    "http-vuln-cve2010-0738.nse",
    "http-vuln-cve2012-1823.nse",
    "http-vuln-cve2013-0156.nse",
    "http-vuln-cve2013-6786.nse",
    # add more scripts here as needed
]

# run IP scanning scripts and save report
ip_report = "nmap_ip_report.txt"
ip_command = f"nmap -sV -sC -Pn --script={','.join(ip_scripts)} {ip_dominio} -oN {ip_report}"
os.system(ip_command)

#--------------------------- Skipfish --------------------------------------


# Obtener el dominio de la URL
dominio = re.search(r"(?<=://)[\w.-]+", url_completa).group()

# Borrar reportes anteriores si existen
if os.path.exists(dominio):
    os.system(f"rm -r {dominio}")

# Ejecutar skipfish y guardar el reporte en la ruta actual del script con el nombre del dominio
subprocess.run(["skipfish", "-m", "5", "-S", f"{dominio}.skipfish", url_completa])


#--------------------------- Uniscan --------------------------------------
#La función os.system() permite ejecutar comandos de consola desde Python. En este caso, se está ejecutando el comando de uniscan con la opción -u para especificar la URL a escanear y las opciones -qwedsgj para habilitar diferentes tipos de escaneos. Luego, se redirige la salida a un archivo llamado "uniscan_report.txt" con el símbolo >.
#domain = dominio
#uniscan_report = "uniscan_report.txt"

# Borramos los antiguos informes de uniscan
#os.system(f"sudo rm /usr/share/uniscan/{domain}/*")

# Ejecutamos el comando de uniscan y guardamos la salida en el archivo de informe
#with open(uniscan_report, "w") as f:
#    subprocess.call(["sudo", "uniscan", "-u", domain, "-qweds", "-r", f"/usr/share/uniscan/{domain}"], stdout=f)

# Traemos el informe a la carpeta actual del script
#os.system(f"sudo cp /usr/share/uniscan/{domain}/{uniscan_report} ./")


#--------------------------- Nikto --------------------------------------
#os.system(command): Ejecuta el comando especificado en la línea de comandos. En este caso, el comando es nikto -h {dominio} -output nikto_report.txt -Format htm, que ejecuta Nikto en el dominio especificado y guarda los resultados en un archivo llamado nikto_report.txt. El argumento -Format htm indica que el informe de resultados se guardará en formato HTML.
def nikto_scan(domain):
    # Eliminar informes anteriores
    for file in os.listdir():
        if file.startswith('nikto_report_') and domain in file:
            os.remove(file)

    # Realizar el escaneo con Nikto
    os.system(f"nikto -h {domain} -output nikto_report_{domain}.txt -Format htm")





