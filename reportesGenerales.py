import mysql.connector
import csv
from os import scandir, getcwd
from datetime import date

# Declaración de variables
route = "/home/administrador/Escritorio/Consultas SQL/RGSeparados"
var_script = ""
columns = 40

# Definición de funciones
# La función ls toma como parámetro una ruta. Lee los archivos que tiene el directorio y devuelte una lista con los nombres de los archivos
def ls(ruta = getcwd()):
    return [route + "/" + arch.name for arch in scandir(ruta) if arch.is_file()]


# Main
# Creo una lista con los archivos que tiene el directorio (Podría ir iterando abriendo el script y ejecutándolo)
print ("leyendo scripts...")
lista_scripts = ls(route)
print ("creada la lista de scripts")

# Me conecto al MySQL
#print ("connecting to MySQL")
cnx = mysql.connector.connect(user='tecnico', password='####', host='####', charset='utf8')
cursor = cnx.cursor()
print ("connected...")

print("Generando reportes...")
for ruta in lista_scripts:
    print ("executing: " + ruta)

    # Leo el script y lo guardo como string en var_script
    with open(ruta) as f:
        for line in f.readlines():
            var_script += line

    # Ejecuta el query

    cursor.execute(var_script)

    ### Armado de nombre del lote
    # Chequeo qué campaña es
    lote = ""
    campania = ruta[-5:]

    hoy = "{0:%Y%m%d}".format(date.today())

    if campania == "segur":
        campania = "Prosegur"
        lote = "PROSEGUR - Rendimiento WkHs " + hoy + ".csv"
    elif campania == "iones":
        campania = "Donaciones"
        lote = "DONACIONES - Rendimiento WkHs " + hoy
    elif campania == "ntial":
        campania = "Prudential"
        lote = "SEGUROS PRUDENTIAL - Rendimiento WkHs " + hoy + ".csv"
    elif campania == "ancor":
        campania = "Sancor-Ribeiro"
        lote = "SANCOR-RIBEIRO - Rendimiento WkHs " + hoy


    csv.register_dialect('myDialect',quoting=csv.QUOTE_ALL,skipinitialspace=True)

    # Guardo los datos en el archivo salida.csv
    with open(lote,'wt') as f:
        writer = csv.writer(f,dialect='myDialect')

        if campania == "Donaciones":
            writer.writerow(["Fecha", "Campaña", "Año", "Mes","Dia", "Semana", "Nombre Día", "Día Semana", "Lunes", "Día Lunes", "Mes Lunes", "Semana Solicitación", "Equipo", "Operador", "Atendimos", "Vacías", "Hablamos", "Argumentamos", "Solicitaron", "Solicitaron", "AtenVsSol", "ArgVsSol", "Hora Logueo", "Tiempo Logueado", "Tiempo Administrativo", "Tiempo Descanso", "Tiempo Llamadas", "Tiempo Hablado", "Tiempo Venta", "Tiempo No Ventas", "THablVsWHs", "VtasVsWHs","ANULADA INTERNA", "PENDIENTE INTERNA", "PASADA A CLIENTE","Cliente PENDIENTE", "Cliente INSTALADA", "Cliente NEGATIVA", "Logueado Normalizado", "ThablVsWHs Normalizado", "VtasVsWHs Normalizado"])
            cantidad = 41
        elif campania == "Sancor-Ribeiro":
            writer.writerow(["Fecha","Campaña",	"Año",	"Mes",	"Dia",	"Semana",	"NombreDia",	"Dia Semana",	"Lunes",	"Dia Lunes",	"Mes Lunes",	"Semana Solicitacion",	"Equipo",	"Operador",	"Atendimos",	"Vacias",	"Hablamos",	"Argumentamos",	"Polizas Solicitadas",	"Clientes Solicitadores",	"Solicitaron",	"AtenVsSol",	"ArgVsSol",	"Hora Logueo",	"Tiempo Logueado",	"Tiempo Administrativo",	"Tiempo Descanso",	"Tiempo Llamadas",	"Tiempo Hablado",	"Tiempo Ventas",	"Tiempo No Ventas",	"THablVsWHs",	"VtasVsWHs",	"Logueado Normalizado",	"ThablVsWHs Normalizado",	"VtasVsWHs Normalizado"])
            cantidad = 36

        for row in cursor.fetchall():
            lista = list(row)
            for i in range(cantidad):
                if(type(lista[i]) == type(int())):
                    lista[i] = int(lista[i])
                if(type(lista[i]) == type(float())):
                    lista[i] = float(lista[i])
                if (lista[i] == None):
                     lista[i] = "NULL"

            rowmodified = tuple(lista)
            writer.writerow(rowmodified)



    print ("query executed...")
    var_script = ""



# Cierro conexión al MySQL
cnx.close()
