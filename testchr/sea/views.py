from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from bs4 import BeautifulSoup
from .models import Proyecto
import requests
import json 

# Create your views here.
def get_data_from_sea(request):
    path_actual = settings.BASE_DIR

    url = "https://seia.sea.gob.cl/busqueda/buscarProyectoAction.php"

    # Realizar petición HTTP a la página
    response = requests.get(url)

    # Crear objeto BeautifulSoup con la respuesta obtenida
    soup = BeautifulSoup(response.content, "html.parser")

    # Obtener todas las páginas de resultados
    options = soup.find("select", {"name": "pagina_offset"}).find_all("option")
    pages = []
    for option in options:
        option_value = option.get('value')
        pages.append(option_value)
        #Obtener las primeras 10 paginas
        if(len(pages) == 10):
            break

    #Se puede agregar la ultima página para probar el resultado 
    #pages.append(2844)

    # Crear lista para almacenar los resultados
    results = []

    # Recorrer todas las páginas y obtener la información de las tablas
    for page in pages:
        page_url = url + "?_paginador_fila_actual=" + str(page)
        page_response = requests.get(page_url)
        page_soup = BeautifulSoup(page_response.content, "html.parser", from_encoding='windows-1250')
        table = page_soup.find("table", {"class": "tabla_datos"})
        rows = table.find_all("tr")
        
        cont=0;
        for row in rows:
            if(cont<2):
                cont += 1
                continue
            cols = row.find_all("td")
            cols = [col.text.strip() for col in cols]
            result = {
                "nombre": cols[1],
                "tipo": cols[2],
                "region": cols[3],
                "topologia": cols[4],
                "titular": cols[5],
                "inversion": float(cols[6].replace('.','').replace(',','.')),
                "fecha_presentacion_ingreso": cols[7],
                "estado": cols[8],
                "mapa": cols[9]
            }

            results.append({"id": cols[0], **result})

            Proyecto.objects.update_or_create(
                id=cols[0],
                defaults={**result}
            )

    # Crear archivo JSON con la información obtenida
    with open(f"{path_actual}\\sea\\docs\\resultados.json", "w", encoding='utf-8') as file:
        json.dump(results, file, indent=4, ensure_ascii=False)

    return HttpResponse('Proyectos sea obtenidos correctamente')

def show_sea_projects(request):
    sea_proyects = Proyecto.objects.all()
    return render(request, 'sea/show_sea_projects.html', {'sea_proyects': sea_proyects})
