from selenium import webdriver
import logging
from datetime import datetime
import urllib.request
import my_functions as functions
import csv

DATA_VERSION_URL = "fifa17_123" # url version de la data
DATA_VERSION_DATE = "27-03-2017" # fecha de la data (hardcodeado a pedido de j)
LIMITE_CANTIDAD_PAGINAS = 0 # indicar la cantidad de paginas a scrapear, si es [0] va ser "infinito"

flagFirstTime = True # flag para saber si es la primer iteraccion

# log config TODO: Meterlos en una carpeta
logging.basicConfig(filename=datetime.today().strftime('%Y%m%d') + '_logging.log', encoding='utf-8', format='%(asctime)s %(message)s', level=logging.INFO)

# driver config TODO: Hacer el path relativo
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.fifaindex.com/es/teams/" + DATA_VERSION_URL) # Navigate to the frist team's page

# config de urlib
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

i = 0
while True:
    next_page_url = functions.get_next_button_url(driver)

    # por cada equipo de esa pagina
    for team_url in functions.get_all_url_teams_from_page(driver):
        logging.info("Redireccionando al equipo [" + team_url + "]")
        driver.get(team_url) # Navigate to team page

        team_name = functions.get_team_name_from_team_page(driver)
        team_id = functions.get_team_id_from_url(team_url)

        # abro el csv TODO: Meterlo en una carpeta
        with open('player_list.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)

            if(flagFirstTime):
                writer.writerow(functions.get_csv_header())
                flagFirstTime = False

            # por cada jugador de ese equipo
            for player_url in functions.get_all_url_players_from_page(driver):
                logging.info("Redireccionando al jugador [" + player_url + "]")
                driver.get(player_url) # navigate to player page

                # scrapeo el player y lo guardo en el csv
                writer.writerow(functions.do_scrap_player(driver, team_name, team_id, functions.get_player_id_from_url(player_url)))

    if((LIMITE_CANTIDAD_PAGINAS-1) == i):
        logging.info("Cantidad limite de paginas alcanzado [" + LIMITE_CANTIDAD_PAGINAS + "]")
        break
    
    logging.info("Redireccionando a la pagina [" + next_page_url + "]")
    driver.get(next_page_url) # al finalizar esta pagina de equipos, voy a la siguiente

    i+=1