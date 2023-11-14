import csv
import json
import random
import openpyxl
from scipy.stats import skewnorm
import unicodecsv as csv
from unidecode import unidecode

def obtener_valores_medios(barrio):
    valores_medios = {
        "Zona Centro": {
            "precio_medio_m2": (0.80 * 1933),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 110, "scale": 30}
        },
        "Sta. Marina - San Andrés - San Pablo - San Lorenzo": {
            "precio_medio_m2": (0.80 * 1620),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 60, "scale": 30}
        },
        "Casco Histórico - Ribera - San Basilio": {
            "precio_medio_m2": (0.80 * 1618),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 117, "scale": 30}
        },
        "Ollerías - San Cayetano": {
            "precio_medio_m2": (0.80 * 1766),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 82, "scale": 30}
        },
        "Fátima - Levante": {
            "precio_medio_m2": (0.80 * 1381),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 80, "scale": 30}
        },
        "Viñuela - Rescatado": {
            "precio_medio_m2": (0.80 * 1359),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 75, "scale": 30}
        },
        "Sagunto - Edisol": {
            "precio_medio_m2": (0.80 * 1405),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 82, "scale": 30}
        },
        "Ciudad Jardín - Zoco": {
            "precio_medio_m2": (0.80 * 1620),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 80, "scale": 30}
        },
        "Vista Alegre - Parque Cruz Conde": {
            "precio_medio_m2": (0.80 * 1641),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 85, "scale": 30}
        },
        "Santa Rosa - Valdeolleros": {
            "precio_medio_m2": (0.80 * 1637),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 85, "scale": 30}
        },
        "El Brillante -El Naranjo - El Tablero": {
            "precio_medio_m2": (0.80 * 1622),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 80, "scale": 30}
        },
        "Huerta de la Reina - Trassierra": {
            "precio_medio_m2": (0.80 * 1434),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 96, "scale": 30}
        },
        "Tablero Bajo - Arruzafilla": {
            "precio_medio_m2": (0.80 * 2373),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 78, "scale": 30}
        },
        "Arroyo del Moro - Noreña": {
            "precio_medio_m2": (0.80 * 2161),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 121, "scale": 30}
        },
        "Parque Figueroa": {
            "precio_medio_m2": (0.80 * 1614),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 60, "scale": 30}
        },
        "Sector Sur": {
            "precio_medio_m2": (0.80 * 1077),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 85, "scale": 30}
        },
        "Campo de la Verdad - Miraflores": {
            "precio_medio_m2": (0.80 * 1353),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 100, "scale": 30}
        },
        "Fuensanta - Arcángel": {
            "precio_medio_m2": (0.80 * 1272),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 90, "scale": 30}
        },
        "Cañero": {
            "precio_medio_m2": (0.80 * 1365),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 132, "scale": 30}
        },
        "Poniente Norte - Miralbaida - Parque Azahara": {
            "precio_medio_m2": (0.80 * 1434),
            "probabilidades_caracteristicas": [0.7, 0.31, 0.254, 0.5],
            "distribucion": {"a": 1.5, "loc": 90, "scale": 30}
        }
    }

    return valores_medios[barrio]
def generar_datos_inmueble(precio_medio_m2, probabilidades_caracteristicas, distribucion):
    datos = []

    a = distribucion["a"]
    loc = distribucion["loc"]
    scale = distribucion["scale"]
    metros_cuadrados = round(float(skewnorm.rvs(a, loc=loc, scale=scale, size=1)), 2)

    if metros_cuadrados < 40:
        num_habitaciones = 1
    elif 40 <= metros_cuadrados <= 60:
        num_habitaciones = random.choices([2, 3], weights=[0.75, 0.25])[0]
    elif 60 <= metros_cuadrados <= 80:
        num_habitaciones = random.choices([2, 3], weights=[0.15, 0.85])[0]
    elif 80 < metros_cuadrados <= 140:
        num_habitaciones = random.choices([3, 4], weights=[0.75, 0.25])[0]
    else:
        num_habitaciones = random.choices([4, 5], weights=[0.75, 0.25])[0]

    if metros_cuadrados < 60:
        num_banos = 1
    elif 60 <= metros_cuadrados <= 75:
        num_banos = random.choice([1, 2])
    elif 75 < metros_cuadrados <= 150:
        num_banos = 2
    elif 150 < metros_cuadrados <= 160:
        num_banos = random.choice([2, 3])
    else:
        num_banos = 3

    tiene_terraza = random.random() < probabilidades_caracteristicas[0]
    tiene_ascensor = random.random() < probabilidades_caracteristicas[1]
    tiene_parking = random.random() < probabilidades_caracteristicas[2]
    esta_amueblado = random.random() < probabilidades_caracteristicas[3]

    valor_inmueble = round(metros_cuadrados * precio_medio_m2, 2)

    if tiene_terraza:
        incremento_terraza = random.uniform(0.03, 0.06)
        valor_inmueble *= (1 + incremento_terraza)
    if tiene_ascensor:
        incremento_ascensor = random.uniform(0.1, 0.2)
        valor_inmueble *= (1 + incremento_ascensor)
    if tiene_parking:
        incremento_parking = random.uniform(0.08, 0.12)
        valor_inmueble *= (1 + incremento_parking)
    if esta_amueblado:
        incremento_amueblado = random.uniform(-0.1, 0.1)
        valor_inmueble *= (1 + incremento_amueblado)

    datos.append(metros_cuadrados)
    datos.append(num_habitaciones)
    datos.append(num_banos)
    datos.append(tiene_terraza)
    datos.append(tiene_ascensor)
    datos.append(tiene_parking)
    datos.append(esta_amueblado)
    datos.append(valor_inmueble)

    return datos

num_viviendas = 1000
viviendas = []

libro_excel = openpyxl.Workbook()
hoja_calculo = libro_excel.active

hoja_calculo.append(
    ["Barrio", "Metros cuadrados", "Habitaciones", "Baños",  "Terraza", "Ascensor", "Parking", "Amueblado", "Valor"])

valores_medios_centro = obtener_valores_medios("Zona Centro")
precio_medio_m2_centro = valores_medios_centro["precio_medio_m2"]
probabilidades_caracteristicas_centro = valores_medios_centro["probabilidades_caracteristicas"]
distribucion_centro = valores_medios_centro["distribucion"]

valores_medios_san_andres = obtener_valores_medios("Sta. Marina - San Andrés - San Pablo - San Lorenzo")
precio_medio_m2_san_andres = valores_medios_san_andres["precio_medio_m2"]
probabilidades_caracteristicas_san_andres = valores_medios_san_andres["probabilidades_caracteristicas"]
distribucion_san_andres = valores_medios_san_andres["distribucion"]

valores_medios_casco_historico = obtener_valores_medios("Casco Histórico - Ribera - San Basilio")
precio_medio_m2_casco_historico = valores_medios_casco_historico["precio_medio_m2"]
probabilidades_caracteristicas_casco_historico = valores_medios_casco_historico["probabilidades_caracteristicas"]
distribucion_casco_historico = valores_medios_casco_historico["distribucion"]

valores_medios_ollerias = obtener_valores_medios("Ollerías - San Cayetano")
precio_medio_m2_ollerias = valores_medios_ollerias["precio_medio_m2"]
probabilidades_caracteristicas_ollerias = valores_medios_ollerias["probabilidades_caracteristicas"]
distribucion_ollerias = valores_medios_ollerias["distribucion"]

valores_medios_fatima = obtener_valores_medios("Fátima - Levante")
precio_medio_m2_fatima = valores_medios_fatima["precio_medio_m2"]
probabilidades_caracteristicas_fatima = valores_medios_fatima["probabilidades_caracteristicas"]
distribucion_fatima = valores_medios_fatima["distribucion"]

valores_medios_vinuela = obtener_valores_medios("Viñuela - Rescatado")
precio_medio_m2_vinuela = valores_medios_vinuela["precio_medio_m2"]
probabilidades_caracteristicas_vinuela = valores_medios_vinuela["probabilidades_caracteristicas"]
distribucion_vinuela = valores_medios_vinuela["distribucion"]

valores_medios_sagunto = obtener_valores_medios("Sagunto - Edisol")
precio_medio_m2_sagunto = valores_medios_sagunto["precio_medio_m2"]
probabilidades_caracteristicas_sagunto = valores_medios_sagunto["probabilidades_caracteristicas"]
distribucion_sagunto = valores_medios_sagunto["distribucion"]

valores_medios_ciudad_jardin = obtener_valores_medios("Ciudad Jardín - Zoco")
precio_medio_m2_ciudad_jardin = valores_medios_ciudad_jardin["precio_medio_m2"]
probabilidades_caracteristicas_ciudad_jardin = valores_medios_ciudad_jardin["probabilidades_caracteristicas"]
distribucion_ciudad_jardin = valores_medios_ciudad_jardin["distribucion"]

valores_medios_vista_alegre = obtener_valores_medios("Vista Alegre - Parque Cruz Conde")
precio_medio_m2_vista_alegre = valores_medios_vista_alegre["precio_medio_m2"]
probabilidades_caracteristicas_vista_alegre = valores_medios_vista_alegre["probabilidades_caracteristicas"]
distribucion_vista_alegre = valores_medios_vista_alegre["distribucion"]

valores_medios_santa_rosa = obtener_valores_medios("Santa Rosa - Valdeolleros")
precio_medio_m2_santa_rosa = valores_medios_santa_rosa["precio_medio_m2"]
probabilidades_caracteristicas_santa_rosa = valores_medios_santa_rosa["probabilidades_caracteristicas"]
distribucion_santa_rosa = valores_medios_santa_rosa["distribucion"]

valores_medios_brillante = obtener_valores_medios("El Brillante -El Naranjo - El Tablero")
precio_medio_m2_brillante = valores_medios_brillante["precio_medio_m2"]
probabilidades_caracteristicas_brillante = valores_medios_brillante["probabilidades_caracteristicas"]
distribucion_brillante = valores_medios_brillante["distribucion"]

valores_medios_huerta = obtener_valores_medios("Huerta de la Reina - Trassierra")
precio_medio_m2_huerta = valores_medios_huerta["precio_medio_m2"]
probabilidades_caracteristicas_huerta = valores_medios_huerta["probabilidades_caracteristicas"]
distribucion_huerta = valores_medios_huerta["distribucion"]

valores_medios_tablero_bajo = obtener_valores_medios("Tablero Bajo - Arruzafilla")
precio_medio_m2_tablero_bajo = valores_medios_tablero_bajo["precio_medio_m2"]
probabilidades_caracteristicas_tablero_bajo = valores_medios_tablero_bajo["probabilidades_caracteristicas"]
distribucion_tablero_bajo = valores_medios_tablero_bajo["distribucion"]

valores_medios_arroyo = obtener_valores_medios("Arroyo del Moro - Noreña")
precio_medio_m2_arroyo = valores_medios_arroyo["precio_medio_m2"]
probabilidades_caracteristicas_arroyo = valores_medios_arroyo["probabilidades_caracteristicas"]
distribucion_arroyo = valores_medios_arroyo["distribucion"]

valores_medios_figueroa = obtener_valores_medios("Parque Figueroa")
precio_medio_m2_figueroa = valores_medios_figueroa["precio_medio_m2"]
probabilidades_caracteristicas_figueroa = valores_medios_figueroa["probabilidades_caracteristicas"]
distribucion_figueroa = valores_medios_figueroa["distribucion"]

valores_medios_sector_sur = obtener_valores_medios("Sector Sur")
precio_medio_m2_sector_sur = valores_medios_sector_sur["precio_medio_m2"]
probabilidades_caracteristicas_sector_sur = valores_medios_sector_sur["probabilidades_caracteristicas"]
distribucion_sector_sur = valores_medios_sector_sur["distribucion"]

valores_medios_campo_verdad = obtener_valores_medios("Campo de la Verdad - Miraflores")
precio_medio_m2_campo_verdad = valores_medios_campo_verdad["precio_medio_m2"]
probabilidades_caracteristicas_campo_verdad = valores_medios_campo_verdad["probabilidades_caracteristicas"]
distribucion_campo_verdad = valores_medios_campo_verdad["distribucion"]

valores_medios_fuensanta = obtener_valores_medios("Fuensanta - Arcángel")
precio_medio_m2_fuensanta = valores_medios_fuensanta["precio_medio_m2"]
probabilidades_caracteristicas_fuensanta = valores_medios_fuensanta["probabilidades_caracteristicas"]
distribucion_fuensanta = valores_medios_fuensanta["distribucion"]

valores_medios_canero = obtener_valores_medios("Cañero")
precio_medio_m2_canero = valores_medios_canero["precio_medio_m2"]
probabilidades_caracteristicas_canero = valores_medios_canero["probabilidades_caracteristicas"]
distribucion_canero = valores_medios_canero["distribucion"]

valores_medios_poniente = obtener_valores_medios("Poniente Norte - Miralbaida - Parque Azahara")
precio_medio_m2_poniente = valores_medios_poniente["precio_medio_m2"]
probabilidades_caracteristicas_poniente = valores_medios_poniente["probabilidades_caracteristicas"]
distribucion_poniente = valores_medios_poniente["distribucion"]

for _ in range(num_viviendas):
    barrio = random.choice([
        "Zona Centro",
        "Sta. Marina - San Andrés - San Pablo - San Lorenzo",
        "Casco Histórico - Ribera - San Basilio",
        "Ollerías - San Cayetano",
        "Fátima - Levante",
        "Viñuela - Rescatado",
        "Sagunto - Edisol",
        "Ciudad Jardín - Zoco",
        "Vista Alegre - Parque Cruz Conde",
        "Santa Rosa - Valdeolleros",
        "El Brillante - El Naranjo - El Tablero",
        "Huerta de la Reina - Trassierra",
        "Tablero Bajo - Arruzafilla",
        "Arroyo del Moro - Noreña",
        "Parque Figueroa",
        "Sector Sur",
        "Campo de la Verdad - Miraflores",
        "Fuensanta - Arcángel",
        "Cañero",
        "Poniente Norte - Miralbaida - Parque Azahara"
    ])

    if barrio == "Zona Centro":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_centro, probabilidades_caracteristicas_centro, distribucion_centro)
    elif barrio == "Sta. Marina - San Andrés - San Pablo - San Lorenzo":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_san_andres, probabilidades_caracteristicas_san_andres, distribucion_san_andres)
    elif barrio == "Casco Histórico - Ribera - San Basilio":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_casco_historico, probabilidades_caracteristicas_casco_historico, distribucion_casco_historico)
    elif barrio == "Ollerías - San Cayetano":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_ollerias, probabilidades_caracteristicas_ollerias, distribucion_ollerias)
    elif barrio == "Fátima - Levante":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_fatima, probabilidades_caracteristicas_fatima, distribucion_fatima)
    elif barrio == "Viñuela - Rescatado":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_vinuela, probabilidades_caracteristicas_vinuela, distribucion_vinuela)
    elif barrio == "Sagunto - Edisol":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_sagunto, probabilidades_caracteristicas_sagunto, distribucion_sagunto)
    elif barrio == "Ciudad Jardín - Zoco":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_ciudad_jardin, probabilidades_caracteristicas_ciudad_jardin, distribucion_ciudad_jardin)
    elif barrio == "Vista Alegre - Parque Cruz Conde":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_vista_alegre, probabilidades_caracteristicas_vista_alegre, distribucion_vista_alegre)
    elif barrio == "Santa Rosa - Valdeolleros":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_santa_rosa, probabilidades_caracteristicas_santa_rosa, distribucion_santa_rosa)
    elif barrio == "El Brillante - El Naranjo - El Tablero":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_brillante, probabilidades_caracteristicas_brillante, distribucion_brillante)
    elif barrio == "Huerta de la Reina - Trassierra":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_huerta, probabilidades_caracteristicas_huerta, distribucion_huerta)
    elif barrio == "Tablero Bajo - Arruzafilla":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_tablero_bajo, probabilidades_caracteristicas_tablero_bajo, distribucion_tablero_bajo)
    elif barrio == "Arroyo del Moro - Noreña":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_arroyo, probabilidades_caracteristicas_arroyo, distribucion_arroyo)
    elif barrio == "Parque Figueroa":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_figueroa, probabilidades_caracteristicas_figueroa, distribucion_figueroa)
    elif barrio == "Sector Sur":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_sector_sur, probabilidades_caracteristicas_sector_sur, distribucion_sector_sur)
    elif barrio == "Campo de la Verdad - Miraflores":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_campo_verdad, probabilidades_caracteristicas_campo_verdad, distribucion_campo_verdad)
    elif barrio == "Fuensanta - Arcángel":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_fuensanta, probabilidades_caracteristicas_fuensanta, distribucion_fuensanta)
    elif barrio == "Cañero":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_canero, probabilidades_caracteristicas_canero, distribucion_canero)
    elif barrio == "Poniente Norte - Miralbaida - Parque Azahara":
        datos_vivienda = generar_datos_inmueble(precio_medio_m2_poniente, probabilidades_caracteristicas_poniente, distribucion_poniente)

    hoja_calculo.append([barrio] + datos_vivienda)
    vivienda = {
        "Barrio": barrio,
        "Metros cuadrados": datos_vivienda[0],
        "Habitaciones": datos_vivienda[1],
        "Baños": datos_vivienda[2],
        "Terraza": datos_vivienda[3],
        "Ascensor": datos_vivienda[4],
        "Parking": datos_vivienda[5],
        "Amueblado": datos_vivienda[6],
        "Valor": datos_vivienda[7]
    }
    viviendas.append(vivienda)

for cell in hoja_calculo["B"][1:]:
    cell.number_format = "0"

for cell in hoja_calculo["I"][1:]:
    cell.number_format = "0"

for cell in hoja_calculo["I"][1:]:
    cell.value = round(cell.value)
    cell.number_format = u'#,##0"€"'

for columna in hoja_calculo.columns:
    max_length = 0
    for cell in columna:
        try:
            if len(str(cell.value)) > max_length:
                max_length = len(str(cell.value))
        except:
            pass
    adjusted_width = (max_length + 3)
    hoja_calculo.column_dimensions[cell.column_letter].width = adjusted_width

for fila in hoja_calculo.iter_rows(min_row=2):
    for celda in fila:
        if isinstance(celda.value, bool):
            celda.value = "Sí" if celda.value else "No"

libro_excel.save("datos_viviendas_xlsx.xlsx")

def exportar_csv(viviendas, archivo_csv):
    with open(archivo_csv, 'wb') as csvfile:
        csvfile.write(u'\ufeff'.encode('utf-8'))
        fieldnames = ["Barrio", "Metros cuadrados", "Habitaciones", "Banos", "Terraza", "Ascensor", "Parking", "Amueblado", "Valor"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, encoding='utf-8')
        writer.writeheader()
        for vivienda in viviendas:
            vivienda_rounded = {k: round(float(v), 2) if isinstance(v, float) else v for k, v in vivienda.items()}
            vivienda_rounded = {k: int(v) if isinstance(v, bool) else v for k, v in vivienda_rounded.items()}
            vivienda_rounded["Metros cuadrados"] = round(vivienda_rounded["Metros cuadrados"])
            vivienda_rounded["Valor"] = round(vivienda_rounded["Valor"])
            vivienda_rounded["Banos"] = vivienda_rounded.pop("Baños")
            vivienda_rounded = {k: unidecode(str(v)) for k, v in vivienda_rounded.items()}
            writer.writerow(vivienda_rounded)

exportar_csv(viviendas, 'datos_viviendas_csv.csv')

def exportar_json(viviendas, archivo_json):
    with open(archivo_json, 'w', encoding='utf-8') as jsonfile:
        viviendas_formatted = [{k: round(v, 2) if isinstance(v, float) else v for k, v in vivienda.items()} for vivienda in viviendas]
        viviendas_formatted = [{k: round(v) if k in ["Metros cuadrados", "Valor"] else v for k, v in vivienda.items()} for vivienda in viviendas_formatted]
        json.dump(viviendas_formatted, jsonfile, ensure_ascii=False, indent=4)

exportar_json(viviendas, 'datos_viviendas_json.json')