import requests
import json
import argparse
from pprint import pprint

def get_json_town(ville):


	url = "http://api.openweathermap.org/data/2.5/weather?q={},fr&appid={}".format(ville, api_key)
	
	r = requests.get(url)
	data=r.json()
	pprint(data)
	

if __name__ == '__main__':
	town_test = input("Enter a test value : ")
	get_json_town(town_test)
