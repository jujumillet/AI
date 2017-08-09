import requests
import json
import argparse
from pprint import pprint
import numpy as np
import pandas as pd
from analyse_json import *

def get_json_town(ville, api_key):


	url = "http://api.openweathermap.org/data/2.5/weather?q={},fr&appid={}".format(ville, api_key)
	
	r = requests.get(url)

	data = r.json() #charge le fichier json de type dict
	#print(type(data))
	#pprint(data)

	#print(data['sys']['country']) #Lire valeurs fichier json
	#for cle in data:
	#	print(cle)

	temp = convKelvinCelsius(data['main']['temp'])
	sentence = "Il fait {} degré à {}".format(temp, data['name'])

	print (sentence)

if __name__ == '__main__':
	town_test = input("Enter a test value : ")
	get_json_town(town_test)
