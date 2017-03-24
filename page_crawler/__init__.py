from .crawler import getJson
from json import load
from config import base_dir
from os import sep

def get_information():
	return getJson()

def load_information():
	with open(base_dir+sep+'page_crawler/last_crawl.json') as f:
		json_data=load(f)
	return json_data
