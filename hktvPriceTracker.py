import requests
from bs4 import BeautifulSoup
import os
from datetime import date

 






def track(url):
	
	headers = {
		"User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
		"referer" : url
	}
	
	page = requests.get(url,headers=headers)


	soup = BeautifulSoup(page.content, 'html.parser')




	title = soup.title.get_text()

	#<span class="discount">$ 270.00</span>				<- price

	#find_all method returns list of obj and cannot use get_text directly


	price = soup.find("span", class_ = "discount")		#<- output:[<span class="discount">$ 270.00</span>]

	extrct_price = price.get_text()				#<-	remove the tag
	
	write_file(title,extrct_price,record_abs_path)
	
	
	
	
	


def load_file(dirname, relative_path):
	abs_path = os.path.join(dirname, relative_path)
	return abs_path


def read_url(abspath):
	with open(abspath, "r") as f:
		url_list = [line.strip() for line in f if line.strip()]
	f.close
	return url_list


def write_file(title, extrct_price,abs_path):
	today = date.today().strftime("%Y/%m/%d")
	price_tracker_file = open(abs_path, "a")
	price_tracker_file.write("\n" + title + "------------" + today + "------------" + extrct_price + "\n")
	price_tracker_file.close()



dirname = os.path.dirname(os.path.realpath('__file__'))
url_rel_path = "data/item_url_list.txt"
record_rel_path = "data/price_tracker_data.txt"


url_abs_path = load_file(dirname, url_rel_path)
record_abs_path = load_file(dirname, record_rel_path)

url_list = read_url(url_abs_path)

for url in url_list:
	track(url)
	
	

