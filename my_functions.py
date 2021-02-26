from string import digits
import re

# algunos metodos
def get_all_url_teams_from_page(driver):
    teams = driver.find_elements_by_css_selector("table.table-teams tbody tr td[data-title='Nombre'] a.link-team")
    return [one_team.get_attribute('href') for one_team in teams]

def get_next_button_url(driver):
    return driver.find_element_by_css_selector("nav ul.pagination li.ml-auto a.btn.btn-light").get_attribute('href')

def get_all_url_players_from_page(driver):
    players = driver.find_elements_by_css_selector("table.table-players tbody td[data-title='Nombre'] a.link-player")
    return [one_player.get_attribute('href') for one_player in players]

def get_team_name_from_team_page(driver):
    return driver.find_element_by_css_selector('div.col-lg-8 nav ol.breadcrumb.bg-primary li.breadcrumb-item.active').text

def get_team_id_from_url(team_url):
    url_split = team_url.split('/')
    return url_split[len(url_split)-4]

def get_csv_header():
    return ["Equipo", "Equipo id", "Nombre", "V1", "V2"]

def do_scrap_player(driver, team_name, team_id):
    player_data_array = []

    # equipo
    player_data_array.append(team_name)

    # equipo id
    player_data_array.append(team_id)

    # nombre
    elementHeader = driver.find_elements_by_css_selector("h5.card-header")[0]
    player_data_array.append(
        elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip()
    )
    # valoraciones
    valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)]
    player_data_array.append(str(valoraciones[0]))
    player_data_array.append(str(valoraciones[1]))


    return player_data_array