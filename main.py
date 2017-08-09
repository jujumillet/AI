from get_api_json import *
import requests
import json
import argparse
import pprint

def split_order(string):
	decompose_sentences = string.split(sep=" ", maxsplit=-1)
	for i in decompose_sentences:
		print(i)


def main ():
    print ("hello world")
    #first_order = input("Enter the order : ")
    #split_order(first_order)

    ville = input("Enter a city : ")
    get_json_town(ville)


if __name__ == '__main__':
	main()