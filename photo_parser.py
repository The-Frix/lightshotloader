import requests
from bs4 import BeautifulSoup
import random
import os

print("GitHub: https://github.com/The-Frix \n")
nums = int(input("Number of images: "))
inums = 0

if os.path.exists("images/") == False:
	os.mkdir("images/")

while inums < nums:
	def randch(lensym):
		i = 0
		txt = ""
		while i < lensym :
			i += 1;
			list1=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
			b=random.randint(0,25)
			txt = txt + list1[b]
		
		return txt

	start_profile = "https://prnt.sc/" + randch(6)

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

	req = requests.get(start_profile, headers=headers)
	soup = BeautifulSoup(req.text)
	imgs = soup.find('img').get("src")

	try:
		img = requests.get(imgs)

		name = str(imgs.split("/")[4])
		print(imgs.split("/"))
		file = open("images/" + name, 'wb')

		file.write(img.content)
		inums += 1
	except requests.exceptions.MissingSchema:
		print("err")
	except IndexError:
		print("not found")
