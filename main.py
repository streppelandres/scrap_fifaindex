from selenium import webdriver
from string import digits

driver = webdriver.Chrome(executable_path=r"C:\Users\itali\Desktop\Scrap test\chromedriver_win32\chromedriver.exe")

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

    header = driver.find_elements_by_css_selector("h5.card-header")[0]

    # TODO: Mejorar estos metodos, hacerlo mas comprensivo
    nombre = header.text.translate(str.maketrans('', '', digits)).replace('\n', ' ').replace('\r', '').strip()
    valoracionA = header.text.split()[len(header.text.split(" "))-1]
    valoracionB = header.text.split()[len(header.text.split(" "))]
    
    print("Nombre [" + nombre + "] [" + valoracionA + "] [" + valoracionB + "]")

    driver.back() # Vuelvo atras en el navegador

    i+=1

driver.close()
