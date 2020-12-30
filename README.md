# reporting-automatizacion

En pos de disminuir los tiempos que insumía la conexión a la BBDD y el posterior envío de un reporte a nuestros clientes, generé estos tres scripts:

1. Se ejecuta reportesGenerales.py , extrayendo de nuestra BBDD los rendimientos de los usuarios.
2. Luego, csvtoxls.py transforma el csv a un xls.
3. Se hacen unas modificaciones manualmente al reporte descargado.
4. Por último, sendmail.py envía el reporte modificado a los clientes que correspondan.

