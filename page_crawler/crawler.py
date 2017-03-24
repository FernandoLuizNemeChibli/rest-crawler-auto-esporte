#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree
from os import sep
from requests import get
from StringIO import StringIO
from urllib2 import urlopen
from json import dump
from os import path
from os import sep

base_dir=path.abspath(path.dirname(__file__))

def getJson():
	webpage=urlopen('http://revistaautoesporte.globo.com/rss/ultimas/feed.xml').read()
	xml_parser=etree.XMLParser()
	html_parser=etree.HTMLParser()
	tree=etree.parse(StringIO(webpage),xml_parser)
	feed_array=[]
	for element in tree.findall('//item'):
		description_parsed=etree.parse(StringIO(element.find("description").text),html_parser)
		description_array=[
			{
			"type":"text",
			"content": "".join(iter_text for text in description_parsed.xpath("//p") for iter_text in text.itertext())
			},
			{
			"type":"links",
			"content":[link.get('href') for link in description_parsed.findall("//div//ul//li//a")]
			}
		]
		for image in description_parsed.findall("//div//img"):
			description_array.append(
				{
					"type":"image",
					"content": image.get('src')
				}
			)

		feed_array.append(
			{
			"title":element.find("title").text,
			"link":element.find("link").text,
			"description":description_array
			}
		)
	return {'feed':feed_array}
	
def saveJson():
	with open(base_dir+sep+'last_crawl.json','wb') as f:
		dump(getJson(),f)
