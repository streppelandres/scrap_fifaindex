from string import digits
import urllib.request
import re

# algunos metodos
def get_all_url_players_from_page(driver):
    players = driver.find_elements_by_css_selector("table.table-players")[0].find_elements_by_css_selector("tbody td[data-title='Nombre'] a.link-player")
    return [one_player.get_attribute('href') for one_player in players]

def get_player_id_from_url(player_url):
    url_split = player_url.split('/')
    return url_split[len(url_split)-4]

def get_and_download_player_img(driver):
    img_src = driver.find_element_by_css_selector("div.row.pt-3 div.col-sm-6 div.d-flex.mb-3.align-items-center div.align-self-center img.player").get_attribute("src")
    img_src = img_src[0:len(img_src)-4] + "png" # Cambio el formato a png
    urllib.request.urlretrieve(img_src, "img/player/" + img_src.split("/")[8])

def scrap_player_first_card(driver, p_row):
    first_card_selector = "div.col-lg-8 div.row.pt-3 div.col-sm-6 div.card.mb-5 div.card-body "

    # altura
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(1) span.float-right span.data-units.data-units-metric").text)

    # peso
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(2) span.float-right span.data-units.data-units-metric").text)

    # pie
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(3) span.float-right").text)

    # nacimiento
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(4) span.float-right").text)

    # edad
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(5) span.float-right").text)

    # posiciones preferidas
    p_row.append(adapter_posiciones_db_deficiente_j(driver.find_elements_by_css_selector(first_card_selector + "p:nth-of-type(6) span.float-right a")))

    # rendimiento
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(7) span.float-right").text)

    # pie_malo
    p_row.append(str(len(driver.find_elements_by_css_selector(first_card_selector + "p:nth-of-type(8) span.float-right span.star i.fas"))))

    # filigranas
    p_row.append(str(len(driver.find_elements_by_css_selector(first_card_selector + "p:nth-of-type(9) span.float-right span.star i.fas"))))

    # valor
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(10) span.float-right").text)

    # sueldo
    p_row.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(13) span.float-right").text)

def adapter_posiciones_db_deficiente_j(webelement_posiciones):
    # paso los web element a array
    pList = []
    for wep in webelement_posiciones:
        pList.append(wep.text)

    # formateo los elementos acorde a la bd de j
    posiciones = []
    i = 0
    celda = "a:" + str(len(pList)) + ":{"
    for p in pList:
        celda += "i:" + str(i) + ";s:" + str(len(p)) + ":\"" + p.lower() + "\";"
        i+=1
    celda += "}"

    return celda

def get_csv_header():
    return [
            "date_version", "equipo_nombre", "equipo_id", "jugador_nombre", "jugador_id", "val_1", "val_2",
            "altura", "peso", "pie", "nacimiento", "edad", "posiciones", "rendimiento",
            "pie_malo", "filigranas", "valor", "sueldo" # first box
            ]

def do_scrap_player(driver, team_name, team_id, player_id, fecha_de_la_data):
    p_row = []

    # descargo la img
    get_and_download_player_img(driver)

    # agrego la fecha de la version de los datos
    p_row.append(fecha_de_la_data)

    # equipo_nombre
    p_row.append(team_name)

    # equipo_id
    p_row.append(FAKE_ID_PLUS + team_id)

    # jugador_nombre
    elementHeader = driver.find_elements_by_css_selector("h5.card-header")[0]
    p_row.append(
        elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip() # agarro nada mas las letras del string
    )

    # jugador_id
    p_row.append(player_id)

    # valoraciones
    valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)] # agarro nada mas los enteros del string
    p_row.append(str(valoraciones[0])) # val_1
    p_row.append(str(valoraciones[1])) # val_2

    # scrapeo la primer caja, donde esta la altura, peso, pie, posiciones, etc
    scrap_player_first_card(driver, p_row)

    return p_row

FAKE_ID_PLUS = "5000" # id que se le agrega adelante para adaptarlo al wordpress deficiente de J