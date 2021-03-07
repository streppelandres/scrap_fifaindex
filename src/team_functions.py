import urllib.request
import os

def get_and_download_team_img(driver, team_id):
    img_src = driver.find_element_by_css_selector("div.row.pt-3 div.col-sm-6.col-md-7 div.d-flex.mb-3.align-items-center div.align-self-center img.team.size-10").get_attribute("src")
    
    path = os.getcwd() + "/img/team/" + team_id
    os.makedirs(path, exist_ok=True)

    urllib.request.urlretrieve(img_src, path + "/" + team_id + ".png")

def get_and_download_team_kits(driver, team_id):
    kit_web_element_list = driver.find_elements_by_css_selector("div.col-12.col-lg-7 div.card.mb-5 div.card-body div.row div.col-6.text-center")

    # por cada camiseta encontrada
    for we_kit in kit_web_element_list:
        we_img_src = we_kit.find_element_by_css_selector("img.kit.img-fluid").get_attribute("src")
        we_p = we_kit.find_element_by_css_selector("p").text

        urllib.request.urlretrieve(we_img_src, "img/team/" + team_id + "/" + team_id + "_" + we_p + ".png")

def get_csv_header():
    h_row = []

    h_row.append("date_version")
    h_row.append("equipo_nombre")
    h_row.append("equipo_id")

    return h_row

def do_scrap_team(driver, team_name, team_id, data_version_date):
    t_row = []

    get_and_download_team_img(driver, team_id)
    get_and_download_team_kits(driver, team_id)
    t_row.append(data_version_date)
    t_row.append(team_name)
    t_row.append(team_id)

    

    return t_row # TODO: Scrap team