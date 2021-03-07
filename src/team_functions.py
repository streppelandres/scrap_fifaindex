import urllib.request

def get_and_download_player_img(driver):
    img_src = driver.find_element_by_css_selector("div.row.pt-3 div.col-sm-6 div.d-flex.mb-3.align-items-center div.align-self-center img.player").get_attribute("src")
    img_src = img_src[0:len(img_src)-4] + "png" # Cambio el formato a png
    urllib.request.urlretrieve(img_src, "img/team/" + img_src.split("/")[8])

def get_csv_header():
    return [] # TODO: Add header

def do_scrap_team(driver, team_name, team_id, data_version_date):

    return [] # TODO: Scrap team