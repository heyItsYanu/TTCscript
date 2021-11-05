import requests
import os
import sys
from zipfile import ZipFile

url = 'https://' + sys.argv[1] + '.tamrieltradecentre.com/download/PriceTable'
addon_dir = 'C:\\Users\\' + os.getlogin() + '\\Documents\\Elder Scrolls Online\\live\\AddOns\\TamrielTradeCentre\\'
table_zip = addon_dir + 'PriceTable.zip'

if os.path.exists(table_zip):
	os.remove(table_zip)
	print("deleted")
else:
	print("The file does not exist")

download = requests.get(url, allow_redirects=True)

with open(table_zip, 'wb') as downloaded:
	downloaded.write(download.content)

zf = ZipFile(table_zip, 'r')
zf.extractall(addon_dir)
zf.close()
