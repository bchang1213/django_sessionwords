# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from datetime import datetime

def index(request):
	if 'words' in request.session:
		print request.session['words']

	return render(request, "session_words/index.html")

def add(request):
	new_words = {} #new_words is an empty dictionary that I will make inherit
	for key,value in request.POST.iteritems():  #the key value pairs of request.POST.
		if key != 'csrfmiddlewaretoken' and key !='bigfont':
			new_words[key] = value
		if key == 'bigfont':
			new_words['bigfont'] = "big"

		new_words['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
	try:
		request.session['words']
	except KeyError:
		request.session['words'] = []

	temp_list = request.session['words']
	temp_list.append(new_words)
	request.session['words'] = temp_list

	for key,val in request.session.__dict__.iteritems():
		print key,val
	return redirect('/')

def clear(request):
	del request.session['words']
	return redirect('/')