from selenium import webdriver
import logging
from datetime import datetime
import urllib.request
from src import generic_functions as g_functions
from src import player_functions as functions
import csv
import os

# creo las carpetas necesarias donde se van almacenar los archivos
g_functions.create_directories(os.getcwd())

DATA_VERSION_URL = "fifa17_123" # url version de la data
DATA_VERSION_DATE = "27-03-2017" # fecha de la data (hardcodeado a pedido de J)
DATE_TODAY = datetime.today().strftime('%Y%m%d')

# Si se queda colgado en algun player, cambias estos datos y ya, si no hay una forma de hacer que no se pijee, fijate que cuand ose pijea complete esto automatico:
START_PAGE = 16
hardCodeUrl = True
hardCodeUrlTeam = "https://www.fifaindex.com/es/team/1794/sheffield-united/fifa17_123/"
hardCodeUrlPlayer = "https://www.fifaindex.com/es/player/212300/jack-oconnell/fifa17_123/"

# log config
logging.basicConfig(filename= "logs/" + DATE_TODAY + '_player_logging.log', encoding='utf-8', format='%(asctime)s %(message)s', level=logging.INFO)

# driver config TODO: Hacer el path relativo
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.fifaindex.com/es/teams/" + DATA_VERSION_URL) # Navigate to the frist team's page

# config de urlib
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

for i in range(START_PAGE, g_functions.get_cant_pages(driver) + 1):
    next_page = "https://www.fifaindex.com/es/teams/"+ DATA_VERSION_URL +"/?page=" + str(i)
    logging.info("Redireccionando a la pagina [" + next_page + "]")
    driver.get(next_page) # Al finalizar esta pagina de equipos, voy a la siguiente
    while True: # TODO: Extraer esto en una funcion
        try:
            # Si encuentra el elemento significa que hay error, sigo dentro del while
            error_type = driver.find_elements_by_css_selector('div#cf-wrapper div#cf-error-details header h1 span.cf-error-type').text
            error_code = driver.find_elements_by_css_selector('div#cf-wrapper div#cf-error-details header h1 span.cf-error-code').text
            logging.error(error_type + " " + error_code + ", se va volver a intentar ingresar a [" + next_page + "]")
            driver.get(next_page)
        except:
            # Si no encuentra el elemento significa que todo esta bien, salgo del while
            break

    # por cada equipo de esa pagina
    urls_team_list = g_functions.get_all_url_teams_from_page(driver)

    if (hardCodeUrl):
        # me agarro apartir del equipo hardcodeado
        urls_team_list = urls_team_list[urls_team_list.index(hardCodeUrlTeam):len(urls_team_list)]

    for team_url in urls_team_list:

        logging.info("Redireccionando al equipo [" + team_url + "]")
        driver.get(team_url) # Navigate to team page

        team_name = g_functions.get_team_name_from_team_page(driver)
        team_id = g_functions.get_team_id_from_url(team_url)

        # abro el csv
        with open('data/' + DATE_TODAY + '_player_list.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, quotechar='&') # el quotechar tiene que ser algo que no se use para nada

            #if(i == 1):
                # si es la primera vez agrego el header de las columnas
                #writer.writerow(functions.get_csv_header())

            # por cada jugador de ese equipo
            urls_player_list = functions.get_all_url_players_from_page(driver)

            if (hardCodeUrl):
                urls_player_list = urls_player_list[urls_player_list.index(hardCodeUrlPlayer):len(urls_player_list)]
                hardCodeUrl = False

            for player_url in urls_player_list:
                
                logging.info("Redireccionando al jugador [" + player_url + "]")
                driver.get(player_url) # navigate to player page
                    
                while True: # TODO: Extraer esto en una funcion
                    try:
                        # Si encuentra el elemento significa que hay error, sigo dentro del while
                        error_type = driver.find_elements_by_css_selector('div#cf-wrapper div#cf-error-details header h1 span.cf-error-type').text
                        error_code = driver.find_elements_by_css_selector('div#cf-wrapper div#cf-error-details header h1 span.cf-error-code').text
                        logging.error(error_type + " " + error_code + ", se va volver a intentar ingresar a [" + player_url + "]")
                        driver.get(player_url)
                    except:
                        # Si no encuentra el elemento significa que todo esta bien, salgo del while
                        break

                # scrapeo el player y lo guardo en el csv
                writer.writerow(functions.do_scrap_player(driver, team_name, team_id, functions.get_player_id_from_url(player_url), DATA_VERSION_DATE))
    
else:
    logging.info("Se termino de scrapear los equipos, se va cerrar el driver")
    driver.quit()