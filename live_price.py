import sys
import time
import argparse

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

parser = argparse.ArgumentParser(
    prog="setup-tracker",
    description="Price tracking software for shopping lists")

parser.add_argument('-r', '--refresh', help='number of seconds to wait after every scan')
parser.add_argument('-b', '--browser', choices=['firefox', 'chrome'], default='firefox')
parser.add_argument('-l', '--headless', action='store_true')

args = parser.parse_args()

listing = [
	# { 
	# 	"store": "store_name",
	# 	"selector": "//*[@id='valParc']", # custom selector for the price
	# 	"links": [
	# 		https://www.storename.com/product/348688,
	#		https://www.storename.com/product/908475
	# 	]
	# },
	{
		"store": "kabum",
		"selector": "//*[@class='regularPrice']",
		"links": [
			"https://www.kabum.com.br/produto/479539/placa-de-video-rx-6650-xt-mech-2x-8g-oc-msi-radeon-8gb-gddr6-free-sync",
			"https://www.kabum.com.br/produto/320797/processador-amd-ryzen-7-5700x-3-4ghz-4-6ghz-max-turbo-cache-36mb-am4-sem-video-100-100000926wof",
			"https://www.kabum.com.br/produto/113891/ssd-256-gb-husky-gaming-m-2-nvme-leitura-1800mb-s-e-gravacao-1300mb-s-hgml003",
			"https://www.kabum.com.br/produto/472349/memoria-lexar-16gb-3200mhz-ddr4-cl22-ld4au016g-b3200gsst",
			"https://www.kabum.com.br/produto/369658/fonte-msi-mag-a650bn-atx-650w-80-plus-bronze-pfc-ativo-entrada-bivolt-preto-306-7zp2b22-ce0",
			"https://www.kabum.com.br/produto/118916/placa-mae-gigabyte-a520m-s2h-amd-am4-ddr4",
			"https://www.kabum.com.br/produto/204497/gabinete-gamer-rise-mode-z1-glass-rgb-lateral-em-vidro-fume-preto-rm-z01-01-fb"
		]
	}
]

while True:
	if args.browser == "firefox":
		options = FirefoxOptions()
		if args.headless:
			options.add_argument("--headless")
		options.binary_location = "./firefox/firefox"
		driver = webdriver.Firefox(options=options)
	else:
		options = ChromeOptions()
		options.binary_location = "./chrome-linux64/chrome"
		if args.headless:
			options.add_argument('--headless=new')
		driver = webdriver.Chrome(options=options)

	for shop_list in listing:
		total = 0
		for link in shop_list["links"]:
			driver.get(link)
			time.sleep(2)
			value_str = ""
			try:
				value_str = driver.find_element(By.XPATH, shop_list["selector"]).text
			except:
				pass
			value_str = "".join(filter(str.isdigit, value_str))
			value = 0
			if len(value_str) > 0:
				value = float(value_str)/100
				print(value)
			else:
				print("not found")
			total += value
		print("listing "+shop_list["store"]+": "+str(total)+"\n##")
	
	driver.quit()
	if args.refresh:
		time.sleep(int(args.refresh))
	else:
		break