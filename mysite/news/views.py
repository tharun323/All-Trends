# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
import requests
import json
# Create your views here.
api_key='dfb1b9a0d3b44d319d600424ded6a6c8' #news api api_key

def headlines(request):
	url = ('https://newsapi.org/v2/top-headlines?'
	   'country=us&'
	   'apiKey=dfb1b9a0d3b44d319d600424ded6a6c8')
	response = requests.get(url)
	json_data = (json.loads(response.text))
	result=list(json_data["articles"])
	p=[]
	for i in result:
		p.append(i["title"])

	
	print(json_data)
	# return JsonResponse(json_data["articles"][0]["title"],safe=False)
	#print(json_data[1])

	context = {'data_list': p}
	return render(request, 'news/home.html', context)
	

movie_api_key='a387579f55efe51e4facc2b1aa1d08cb'


#/trending/{media_type}/{time_window}

def newssources(request):
	url=('https://newsapi.org/v2/sources?apiKey=dfb1b9a0d3b44d319d600424ded6a6c8')	
	response = requests.get(url)
	json_data = (json.loads(response.text))
	result=list(json_data["sources"])[:10]
	print(json_data)
	sources=[]
	links=[]
	for i in result:
		sources.append(i["description"])
		links.append(i["url"])

	res=zip(sources,links)
	context = {'data_list': res}
	return render(request, 'news/home.html', context)









