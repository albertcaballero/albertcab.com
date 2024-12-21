from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
	path('home/', views.home),
	path('hand_cut/', views.handCutPage),
	path('flowers/', views.flowersPage),
	path('motivation_letter/', views.motivationLetterPage),
	path('curriculum_vitae/', views.curriculumPage),
	path('squat_king/', views.squaKingPage),
	path('about/', views.aboutPage),
	# path('faster_reader/', views.fasterReaderPage),
]