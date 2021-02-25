from selenium import webdriver
from string import digits
import re

def get_all_url_teams_from_page():
    teams = DRIVER.find_elements_by_css_selector("table.table-teams tbody tr td[data-title='Nombre'] a.link-team")
    return [one_team.get_attribute('href') for one_team in teams]

def get_next_button_url():
    return DRIVER.find_element_by_css_selector("nav ul.pagination li.ml-auto a.btn.btn-light").get_attribute('href')

def get_all_url_players_from_page():
    players = DRIVER.find_elements_by_css_selector("table.table-players tbody td[data-title='Nombre'] a.link-player")
    return [one_player.get_attribute('href') for one_player in players]

DRIVER = webdriver.Chrome(executable_path=r"C:\Users\itali\Desktop\scrap_fifaindex\chromedriver_win32\chromedriver.exe")
DRIVER.get("https://www.fifaindex.com/es/teams/fifa17_123/")

print("Next page URL [" + get_next_button_url() + "]")
for team_url in get_all_url_teams_from_page():
    # Navigate to team page
    print("Redirect to team [" + team_url + "]")
    DRIVER.get(team_url)

    for player_url in get_all_url_players_from_page():
        print("Redirect to player [" + player_url + "]")
        DRIVER.get(player_url)

        elementHeader = DRIVER.find_elements_by_css_selector("h5.card-header")[0]
        nombre = elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip()
        print("Player name [" + nombre + "]")

        valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)]
        print("Player rate [" + ' '.join([str(elem) for elem in valoraciones])  + "]")

# TODO: cuando termina el for de los teams, tiene que redireccionar a donde se haya guardado el ultimo boton
# y repetir recursivamente todo de nuevo
# fijate de hacer algun metodo recursivo