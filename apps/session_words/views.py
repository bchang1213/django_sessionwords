from django.shortcuts import render, redirect

def index(request):
	return render(request, "session_words/index.html")

def add(request):
	request.session['word'] = request.POST['word']
	request.session['color'] = request.POST['color']
	request.session['bigfont'] = request.POST['bigfont']
	print request.POST['word']
	print request.POST['color']
	print request.POST['bigfont']
	if request.session['bigfont'] == 'on':
		print 'true'
	return redirect('/')
