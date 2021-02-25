import pandas as pd
import io
import requests
import urllib
import mimetypes

url = 'https://www.datosabiertos.gob.pe/sites/default/files/_Muestra.xlsx'
urllib.request.urlretrieve(url, 'vac_data.xlsx')

vac_data = pd.read_excel('vac_data.xlsx')
print(vac_data.head(5))
