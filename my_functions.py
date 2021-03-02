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

def get_csv_header():
    return ["date_version", "equipo", "equipo_id", "jugador_nombre", "jugador_id", "val_1", "val_2"]

def do_scrap_player(driver, team_name, team_id, player_id, fecha_de_la_data):
    player_data_array = []

    # agrego la fecha de la version de los datos
    player_data_array.append(fecha_de_la_data)

    # equipo
    player_data_array.append(team_name)

    # equipo id
    player_data_array.append(FAKE_ID_PLUS + team_id)

    # jugador nombre
    elementHeader = driver.find_elements_by_css_selector("h5.card-header")[0]
    player_data_array.append(
        elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip() # agarro nada mas las letras del string
    )

    # jugador id
    player_data_array.append(player_id)

    # valoraciones
    valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)] # agarro nada mas los enteros del string
    player_data_array.append(str(valoraciones[0])) # val_1
    player_data_array.append(str(valoraciones[1])) # val_2

    # descargo la img
    get_and_download_player_img(driver)

    return player_data_array

FAKE_ID_PLUS = "1000" # id que se le agrega adelante para adaptarlo al wordpress deficiente de J