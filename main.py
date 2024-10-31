#%%
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#%%
port=8282
chrome_path=r"D:\program data\chrome-testing-win64"
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", f"127.0.0.1:{port}")
# chrome_options.add_experimental_option("detach", True)


br = webdriver.Chrome(service=ChromeService(executable_path=chrome_path+'\chromedriver.exe'), options=chrome_options)
br.get("https://codebeautify.org/code-to-image-converter")



#%%
# download_xpath = "/html/body/div[@id='app']/section[@class='container section pt-5 is-fluid']/div[@class='columns']/div[@class='column is-8']/div[@class='columns has-text-centered']/div[@class='column is-4 pl-0']/div[@class='field has-addons']/div[@class='control'][1]/button[@id='download']/span[2]"
languale_xpath = "/html/body/div[@id='app']/section[@class='container section pt-5 is-fluid']/div[@class='columns']/div[@class='column is-4']/div[@class='columns'][1]/div[@class='column'][2]/div[@class='field']/div[@class='select is-fullwidth']/select[@id='selectLanguage']"
theme_xpath = "/html/body/div[@id='app']/section[@class='container section pt-5 is-fluid']/div[@class='columns']/div[@class='column is-4']/div[@class='columns'][1]/div[@class='column'][1]/div[@class='field']/div[@class='select is-fullwidth']/select[@id='selectThemes']"
file_name_xpath = "/html/body/div[@id='app']/section[@class='container section pt-5 is-fluid']/div[@class='columns']/div[@class='column is-4']/div[@class='field'][2]/div[@class='control']/input[@id='inputFileName']"
code_area_xpath = "/html/body/div[1]/section[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div[1]/textarea"
# clear_code_xpath = "/html/body/div[1]/section[2]/div[2]/div[2]/div[2]/div[2]/button"
pading_xpath = "/html/body/div[@id='app']/section[@class='container section pt-5 is-fluid']/div[@class='columns']/div[@class='column is-4']/div[@class='columns'][2]/div[@class='column'][1]/div[@class='field']/p[@class='control has-icons-right']/input[@id='inputPadding']"
Width_xpath = "/html/body/div[@id='app']/section[@class='container section pt-5 is-fluid']/div[@class='columns']/div[@class='column is-4']/div[@class='columns'][2]/div[@class='column is-4']/div[@class='field']/p[@class='control has-icons-right']/input[@id='inputWidth']"


## hidden element
code_div_xpath = "/html/body/div[1]/section[2]/div[2]/div[2]/div[1]/div/div/div[1]/div[2]/div/div"

# %%
def _change_value(xpath, value):
    br.execute_script(f"arguments[0].value = '{value}';", br.find_element(By.XPATH, xpath))

def _drop_down(xpath, value):
    Select(br.find_element(By.XPATH, xpath)).select_by_value(value)

def set_code(code):
    clear_code()

    a=br.find_element(By.XPATH, code_div_xpath)
    br.execute_script("arguments[0].style.overflow = 'visible';", a)
    br.find_element(By.XPATH, code_area_xpath).send_keys(s)
    br.execute_script("arguments[0].style.overflow = 'hidden';", a)
    
    a.send_keys(code)

def clear_code():
    br.execute_script("clearCodeArea()")

def startup_setting():
    br.execute_script("showHideBranding('hide')")
    
    _change_value(pading_xpath, 0)
    _change_value(Width_xpath, 0)

    _drop_down(languale_xpath, "python")
    _drop_down(theme_xpath, "base16-dark")
    
    clear_code()

#%%
chrome_default_download = r"C:\Users\Lenovo ideaPad 3\Downloads"
def download_image():
    pre = set(os.listdir(chrome_default_download))
    br.execute_script("downloadImage()")
    while 1:
        sleep(2.5)
        now = set(os.listdir(chrome_default_download))
        for i in now.difference(pre):
            if "beautify-picture" in i:
                return Path(chrome_default_download).joinpath(i)

download_image()


