from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def aboutPage(request):
	return render(request, 'about.html')

def handCutPage(request):
	return render(request, 'hand_cut.html')

def flowersPage(request):
	return render(request, 'flowers.html')

def motivationLetterPage(request):
	return render(request, 'motivation_letter.html')

def squaKingPage(request):
	return render(request, 'squat_king.html')

def curriculumPage(request):
	return render(request, 'curriculum.html')

def fasterReaderPage(request):
	return render(request, 'faster_reader.html')
