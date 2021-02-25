from selenium import webdriver
from string import digits
import re
from player import *
import time

driver = webdriver.Chrome(executable_path=r"C:\Users\itali\Desktop\scrap_fifaindex\chromedriver_win32\chromedriver.exe")

driver.get("https://www.fifaindex.com/es/teams/fifa17_123")

equipo = driver.find_elements_by_css_selector("td[data-title='Nombre']")[0]

# Revisando equipos
#e = 0
#while e < len(equipos):
print("Entro a revisar el equipo [" + str(0) + "]" + equipo.text + "]")
equipo.click()

cant = len(driver.find_elements_by_css_selector("td[data-title='Nombre']"))-1
print("Cantidad de jugadores [" + str(cant) + "]")

i = 0
while i < cant:
    print("Valor de i al principio [" + str(i) + "]")
    jugador = driver.find_elements_by_css_selector("td[data-title='Nombre']")[i]
    print("Jugador que voy hacer click [" + jugador.text + "]")
    

    state = driver.execute_script('return document.readyState')
    if state == 'complete':
        jugador.click()
        #time.sleep(3)
        # Aca deberia ir un wait

        # Containers
        elementHeader = driver.find_elements_by_css_selector("h5.card-header")[0]
        elementCardBodyFloatRight = driver.find_elements_by_css_selector(".card-body .float-right")

        # Elements
        # TODO: Mejorar estos metodos, hacerlo mas comprensivo
        # *BOX 1 *
        nombre = elementHeader.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip()
        print("Nombre encontrado [" + nombre + "]")


        valoraciones = [int(s) for s in re.findall(r'\b\d+\b', elementHeader.text)]
        print("Valoraciones encontradas [" + ' '.join([str(elem) for elem in valoraciones])  + "]")

        valoracionA = str(valoraciones[0])
        valoracionB = str(valoraciones[1])

        player = Player(nombre, valoracionA, valoracionB)
        player.altura = driver.find_elements_by_css_selector(".card-body .float-right .data-units-metric")[0].text
        player.peso = driver.find_elements_by_css_selector(".card-body .float-right .data-units-metric")[1].text
        player.pie = elementCardBodyFloatRight[2].text
        player.nacimiento = elementCardBodyFloatRight[3].text
        player.edad = elementCardBodyFloatRight[4].text
        player.posicion = elementCardBodyFloatRight[5].text # TODO: Aca pueden haber varias posiciones preferidas
        player.rendimiento = elementCardBodyFloatRight[6].text

        #stars
            #badfoot = driver.find_elements_by_css_selector(".card-body .float-right")[7]
            #skills = driver.find_elements_by_css_selector(".card-body .float-right")[8]
        
        player.valor = elementCardBodyFloatRight[9].text
        player.sueldo = elementCardBodyFloatRight[10].text

        #*BOX 2*
        player.club = driver.find_elements_by_css_selector("h5.card-header .link-team")[1]

        #*STATS*
        player.control = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(1) p:nth-of-type(1) .badge-dark").text
        player.regates = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(1) p:nth-of-type(2) .badge-dark").text

        player.marcaje = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(2) p:nth-of-type(1) .badge-dark").text
        player.entradas = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(2) p:nth-of-type(2) .badge-dark").text
        player.robos = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(2) p:nth-of-type(3) .badge-dark").text

        player.agresividad = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(1) .badge-dark").text
        player.anticipacion = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(2) .badge-dark").text
        player.pos_ataque = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(3) .badge-dark").text
        player.intercep = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(4) .badge-dark").text
        player.vision = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(5) .badge-dark").text
        player.compostura = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(6) .badge-dark").text

        player.centros = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(4) p:nth-of-type(1) .badge-dark").text
        player.pase_corto = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(4) p:nth-of-type(2) .badge-dark").text
        player.pase_largo = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(4) p:nth-of-type(3) .badge-dark").text

        player.aceleracion = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(1) .badge-dark").text
        player.resistencia = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(2) .badge-dark").text
        player.fuerza = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(3) .badge-dark").text
        player.equilibrio = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(4) .badge-dark").text
        player.velocidad = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(5) .badge-dark").text
        player.agilidad = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(6) .badge-dark").text
        player.salto = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(7) .badge-dark").text

        player.cabezazos = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(1) .badge-dark").text
        player.pot_de_tiro = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(2) .badge-dark").text
        player.definicion = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(3) .badge-dark").text
        player.tiros_lejanos = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(4) .badge-dark").text
        player.efecto = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(5) .badge-dark").text
        player.prec_falta = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(6) .badge-dark").text
        player.penaltis = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(7) .badge-dark").text
        player.voleas = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(8) .badge-dark").text

        player.colocacion = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(1) .badge-dark").text
        player.estirada = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(2) .badge-dark").text
        player.paradas = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(3) .badge-dark").text
        player.saques = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(4) .badge-dark").text
        player.reflejos = driver.find_element_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(5) .badge-dark").text

        print("i [" + str(i) + "] Nombre [" + player.nombre + "] [" + player.valoracionA + "] [" + player.valoracionB + "] [" + player.control + "] [" + player.regates + "]")
        i+=1
        driver.back() # Vuelvo atras en el navegador

driver.close()
