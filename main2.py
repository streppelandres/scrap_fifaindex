from selenium import webdriver
from string import digits
import re
import logging
from datetime import datetime

def get_all_url_teams_from_page():
    teams = driver.find_elements_by_css_selector("table.table-teams tbody tr td[data-title='Nombre'] a.link-team")
    return [one_team.get_attribute('href') for one_team in teams]

def get_next_button_url():
    return driver.find_element_by_css_selector("nav ul.pagination li.ml-auto a.btn.btn-light").get_attribute('href')

def get_all_url_players_from_page():
    players = driver.find_elements_by_css_selector("table.table-players tbody td[data-title='Nombre'] a.link-player")
    return [one_player.get_attribute('href') for one_player in players]

def get_team_name_from_team_page():
    return driver.find_element_by_css_selector('div.col-lg-8 nav ol.breadcrumb.bg-primary li.breadcrumb-item.active').text

# log config TODO: Meterlos en una carpeta
logging.basicConfig(filename=datetime.today().strftime('%Y%m%d') + '_logging.log', encoding='utf-8', format='%(asctime)s %(message)s', level=logging.INFO)

# driver config TODO: Hacer el path relativo
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.fifaindex.com/es/teams/fifa17_123/") # Navigate to the frist team's page

# TODO: cambiar el while-true por el max numero de paginas, lo tenias anotado por ahi
while True:
    next_page_url = get_next_button_url()

    # por cada equipo de esa pagina
    for team_url in get_all_url_teams_from_page():
        logging.info("Redireccionando al equipo [" + team_url + "]")
        driver.get(team_url) # Navigate to team page
        team_name = get_team_name_from_team_page()

        # por cada jugador de ese equipo
        for player_url in get_all_url_players_from_page():
            driver.get(player_url) # Navigate to player page
            logging.info("Redireccionando al jugador [" + player_url + "]")

            elementHeader = driver.find_elements_by_css_selector("h5.card-header")[0]
            nombre = elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip()
            valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)]

            print("| " + ' '.join([str(elem) for elem in valoraciones]) + "\t| " + team_name + "\t| " + nombre)

    driver.get(next_page_url) # al finalizar esta pagina de equipos, voy a la siguiente