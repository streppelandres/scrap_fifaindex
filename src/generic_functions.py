from selenium import webdriver

def get_next_button_url(driver):
    return driver.find_element_by_css_selector("nav ul.pagination li.ml-auto a.btn.btn-light").get_attribute('href')

def get_all_url_teams_from_page(driver):
    teams = driver.find_elements_by_css_selector("table.table-teams tbody tr td[data-title='Nombre'] a.link-team")
    return [one_team.get_attribute('href') for one_team in teams]

def get_team_name_from_team_page(driver):
    return driver.find_element_by_css_selector('div.col-lg-8 nav ol.breadcrumb.bg-primary li.breadcrumb-item.active').text

def get_team_id_from_url(team_url):
    url_split = team_url.split('/')
    return url_split[len(url_split)-4]