from string import digits
import urllib.request
import re
# from main2 import DATA_VERSION_DATE

# algunos metodos
def get_all_url_teams_from_page(driver):
    teams = driver.find_elements_by_css_selector("table.table-teams tbody tr td[data-title='Nombre'] a.link-team")
    return [one_team.get_attribute('href') for one_team in teams]

def get_next_button_url(driver):
    return driver.find_element_by_css_selector("nav ul.pagination li.ml-auto a.btn.btn-light").get_attribute('href')

def get_all_url_players_from_page(driver):
    players = driver.find_elements_by_css_selector("table.table-players")[0].find_elements_by_css_selector("tbody td[data-title='Nombre'] a.link-player")
    return [one_player.get_attribute('href') for one_player in players]

def get_team_name_from_team_page(driver):
    return driver.find_element_by_css_selector('div.col-lg-8 nav ol.breadcrumb.bg-primary li.breadcrumb-item.active').text

# TODO: Estos dos metodos hacen lo mismo, fijate capaz de hacer uno solo
def get_team_id_from_url(team_url):
    url_split = team_url.split('/')
    return url_split[len(url_split)-4]

def get_player_id_from_url(player_url):
    url_split = player_url.split('/')
    return url_split[len(url_split)-4]

def get_and_download_player_img(driver):
    img_src = driver.find_element_by_css_selector("div.row.pt-3 div.col-sm-6 div.d-flex.mb-3.align-items-center div.align-self-center img.player").get_attribute("src")
    img_src = img_src[0:len(img_src)-4] + "png" # Cambio el formato a png
    urllib.request.urlretrieve(img_src, "img/" + img_src.split("/")[8])

def scrap_player_first_card(driver, player_data_array):
    first_card_selector = "div.col-lg-8 div.row.pt-3 div.col-sm-6 div.card.mb-5 div.card-body "

    # altura
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(1) span.float-right span.data-units.data-units-metric").text)

    # peso
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(2) span.float-right span.data-units.data-units-metric").text)

    # pie
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(3) span.float-right").text)

    # nacimiento
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(4) span.float-right").text)

    # edad
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(5) span.float-right").text)

    # posiciones preferidas
    player_data_array.append(adapter_posiciones_db_deficiente_j(driver.find_elements_by_css_selector(first_card_selector + "p:nth-of-type(6) span.float-right a")))

    # rendimiento
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(7) span.float-right").text)

    # pie_malo
    player_data_array.append(str(len(driver.find_elements_by_css_selector(first_card_selector + "p:nth-of-type(8) span.float-right span.star i.fas"))))

    # filigranas
    player_data_array.append(str(len(driver.find_elements_by_css_selector(first_card_selector + "p:nth-of-type(9) span.float-right span.star i.fas"))))

    # valor
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(10) span.float-right").text)

    # sueldo
    player_data_array.append(driver.find_element_by_css_selector(first_card_selector + "p:nth-of-type(13) span.float-right").text)

def adapter_posiciones_db_deficiente_j(webelement_posiciones):
    # paso los web element a array
    pList = []
    for wep in webelement_posiciones:
        pList.append(wep.text)

    # formateo los elementos acorde a la bd de j
    posiciones = []
    i = 0
    celda = "a:" + str(len(pList)) + ": {"
    for p in pList:
        celda += "i:" + str(i) + ";s:" + str(len(p)) + "\"" + p + "\";"
        i+=1
    celda += "}"

    return celda

def get_csv_header():
    return [
            "date_version", "equipo_nombre", "equipo_id", "jugador_nombre", "jugador_id", "val_1", "val_2",
            "altura", "peso", "pie", "nacimiento", "edad", "posiciones", "rendimiento", "pie_malo", "filigranas", "valor", "sueldo" # first box
            ]

def do_scrap_player(driver, team_name, team_id, player_id, fecha_de_la_data):
    player_data_array = []

    # descargo la img
    get_and_download_player_img(driver)

    # agrego la fecha de la version de los datos
    player_data_array.append(fecha_de_la_data)

    # equipo_nombre
    player_data_array.append(team_name)

    # equipo_id
    player_data_array.append(FAKE_ID_PLUS + team_id)

    # jugador_nombre
    elementHeader = driver.find_elements_by_css_selector("h5.card-header")[0]
    player_data_array.append(
        elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip() # agarro nada mas las letras del string
    )

    # jugador_id
    player_data_array.append(player_id)

    # valoraciones
    valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)] # agarro nada mas los enteros del string
    player_data_array.append(str(valoraciones[0])) # val_1
    player_data_array.append(str(valoraciones[1])) # val_2

    # scrapeo la primer caja, donde esta la altura, peso, pie, posiciones, etc
    scrap_player_first_card(driver, player_data_array)

    return player_data_array

FAKE_ID_PLUS = "1000" # id que se le agrega adelante para adaptarlo al wordpress deficiente de J