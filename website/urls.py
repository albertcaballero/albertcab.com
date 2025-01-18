from django.urls import path, include

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
	path('main/', views.mainPage),
	path('math/', views.matematicsPage),
	path('pong/', views.pongPage),
	path('minirt/', views.miniRTPage),
	# path('faster_reader/', views.fasterReaderPage),
	# path('accounts/', include('django.contrib.auth.urls')),
]