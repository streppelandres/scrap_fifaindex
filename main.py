from selenium import webdriver
from string import digits

driver = webdriver.Chrome(executable_path=r"C:\Users\Julian\Downloads\scrap_fifaindex-main\chromedriver.exe")

driver.get("https://www.fifaindex.com/es/teams/fifa17_123")

equipo = driver.find_elements_by_css_selector("td[data-title='Nombre']")[0]

# Revisando equipos
#e = 0
#while e < len(equipos):
print("Entro a revisar el equipo [" + str(0) + "]" + equipo.text + "]")
equipo.click()

cant = len(driver.find_elements_by_css_selector("td[data-title='Nombre']"))

i = 0
while i < cant:
    jugador = driver.find_elements_by_css_selector("td[data-title='Nombre']")[i]
    jugador.click()

    #Containers
    header = driver.find_elements_by_css_selector("h5.card-header")[0]
    box1 = driver.find_elements_by_css_selector(".card-body")[0]
    header2 = driver.find_elements_by_css_selector("h5.card-header")[1]
    stats_box1 = driver.find_elements_by_css_selector(".row.grid .item")[0]
    stats_box2 = driver.find_elements_by_css_selector(".row.grid .item")[1]
    stats_box3 = driver.find_elements_by_css_selector(".row.grid .item")[2]
    stats_box4 = driver.find_elements_by_css_selector(".row.grid .item")[3]
    stats_box5 = driver.find_elements_by_css_selector(".row.grid .item")[4]
    stats_box6 = driver.find_elements_by_css_selector(".row.grid .item")[5]
    stats_box7 = driver.find_elements_by_css_selector(".row.grid .item")[6]
    #stats_box8 = driver.find_elements_by_css_selector(".row.grid .item")[7]
    #stats_box9 = driver.find_elements_by_css_selector(".row.grid .item")[8]

    #Elements
    # TODO: Mejorar estos metodos, hacerlo mas comprensivo
    #*BOX 1*
    nombre = header.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip()
    valoracionA = header.text.split()[len(header.text.split(" "))-1]
    valoracionB = header.text.split()[len(header.text.split(" "))]

    weight = driver.find_elements_by_css_selector(".card-body .float-right .data-units-metric")[0]
    height = driver.find_elements_by_css_selector(".card-body .float-right .data-units-metric")[1]
    foot = driver.find_elements_by_css_selector(".card-body .float-right")[2]
    birth = driver.find_elements_by_css_selector(".card-body .float-right")[3]
    age = driver.find_elements_by_css_selector(".card-body .float-right")[4]
    position = driver.find_elements_by_css_selector(".card-body .float-right")[5]
    rendimiento = driver.find_elements_by_css_selector(".card-body .float-right")[6]
    #stars
        #badfoot = driver.find_elements_by_css_selector(".card-body .float-right")[7]
        #skills = driver.find_elements_by_css_selector(".card-body .float-right")[8]
    value = driver.find_elements_by_css_selector(".card-body .float-right")[9]
    wage = driver.find_elements_by_css_selector(".card-body .float-right")[10]

    #*BOX 2*
    club = driver.find_elements_by_css_selector("h5.card-header .link-team")[1]

    #*STATS*
    control = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(1) p:nth-of-type(1) .badge-dark")[0]
    regates = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(1) p:nth-of-type(2) .badge-dark")[0]

    marcaje = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(2) p:nth-of-type(1) .badge-dark")[0]
    entradas = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(2) p:nth-of-type(2) .badge-dark")[0]
    robos = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(2) p:nth-of-type(3) .badge-dark")[0]

    agresividad = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(1) .badge-dark")[0]
    anticipacion = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(2) .badge-dark")[0]
    pos_ataque = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(3) .badge-dark")[0]
    intercep = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(4) .badge-dark")[0]
    vision = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(5) .badge-dark")[0]
    compostura = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(3) p:nth-of-type(6) .badge-dark")[0]

    centros = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(4) p:nth-of-type(1) .badge-dark")[0]
    pase_corto = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(4) p:nth-of-type(2) .badge-dark")[0]
    pase_largo = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(4) p:nth-of-type(3) .badge-dark")[0]

    aceleracion = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(1) .badge-dark")[0]
    resistencia = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(2) .badge-dark")[0]
    fuerza = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(3) .badge-dark")[0]
    equilibrio = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(4) .badge-dark")[0]
    velocidad = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(5) .badge-dark")[0]
    agilidad = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(6) .badge-dark")[0]
    salto = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(5) p:nth-of-type(7) .badge-dark")[0]

    cabezazos = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(1) .badge-dark")[0]
    pot_de_tiro = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(2) .badge-dark")[0]
    definicion = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(3) .badge-dark")[0]
    tiros_lejanos = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(4) .badge-dark")[0]
    efecto = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(5) .badge-dark")[0]
    prec_falta = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(6) .badge-dark")[0]
    penaltis = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(7) .badge-dark")[0]
    voleas = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(6) p:nth-of-type(8) .badge-dark")[0]

    colocacion = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(1) .badge-dark")[0]
    estirada = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(2) .badge-dark")[0]
    paradas = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(3) .badge-dark")[0]
    saques = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(4) .badge-dark")[0]
    reflejos = driver.find_elements_by_css_selector(".row.grid .item:nth-of-type(7) p:nth-of-type(5) .badge-dark")[0]


    weight = weight.text
    height = height.text
    foot = foot.text
    birth = birth.text
    age = age.text
        #position = position.text
    rendimiento = rendimiento.text
        #badfoot = badfoot.text
        #skills = skills.text
    value = value.text
    wage = wage.text

    club = club.text

    control = control.text
    regates = regates.text

    marcaje = marcaje.text
    entradas = entradas.text
    robos = robos.text

    print("Nombre [" + nombre + "] [" + valoracionA + "] [" + valoracionB + "] [" + control + "] [" + regates + "]")

    driver.back() # Vuelvo atras en el navegador

    i+=1

driver.close()
