from selenium import webdriver
import logging
from datetime import datetime
import urllib.request
from src import generic_functions as g_functions
from src import team_functions as functions
import csv
import os

# creo las carpetas necesarias donde se van almacenar los archivos
g_functions.create_directories(os.getcwd())

DATA_VERSION_URL = "fifa17_123"
DATA_VERSION_DATE = "27-03-2017"
DATE_TODAY = datetime.today().strftime('%Y%m%d')

flagFirstTime = True # flag para saber si es la primer iteraccion

# log config
logging.basicConfig(filename= "logs/" + DATE_TODAY + '_team_logging.log', encoding='utf-8', format='%(asctime)s %(message)s', level=logging.INFO)

# driver config TODO: Hacer el path relativo
driver = webdriver.Chrome(executable_path=r"C:\chromedriver_win32\chromedriver.exe")
driver.get("https://www.fifaindex.com/es/teams/" + DATA_VERSION_URL) # Navigate to the frist team's page

# config de urlib
opener=urllib.request.build_opener()
opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

# TODO:
# Hacer algo que busque si ya existe el header-row, porque cuando retomas va agregar de nuevo el header row

for i in range(1, g_functions.get_cant_pages(driver) + 1):
    next_page = "https://www.fifaindex.com/es/teams/"+ DATA_VERSION_URL +"/?page=" + str(i)
    logging.info("Redireccionando a la pagina [" + next_page + "]")
    driver.get(next_page) # Al finalizar esta pagina de equipos, voy a la siguiente

    # por cada equipo de esa pagina
    for team_url in g_functions.get_all_url_teams_from_page(driver):
        logging.info("Redireccionando al equipo [" + team_url + "]")
        driver.get(team_url) # Navigate to team page

        team_name = g_functions.get_team_name_from_team_page(driver)
        team_id = g_functions.get_team_id_from_url(team_url)

        # abro el csv
        with open('data/' + DATE_TODAY + '_team_list.csv', 'a', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, quotechar='&') # el quotechar tiene que ser algo que no se use para nada

            if(flagFirstTime):
                logging.info("Primer ingreso, se va agregar el header al csv")
                writer.writerow(functions.get_csv_header())
                flagFirstTime = False

            # scrap team
            logging.info("Se va scrapear el equipo [" + team_name + "] con la id [" + team_id + "]")
            writer.writerow(functions.do_scrap_team(driver, team_name, team_id, DATA_VERSION_DATE))

else:
    logging.info("Se termino de scrapear los equipos, se va cerrar el driver")
    driver.quit()