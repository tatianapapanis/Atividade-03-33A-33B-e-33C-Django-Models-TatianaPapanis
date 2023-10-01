from django.shortcuts import render
from .models import Hobbies, Habilidades, Idioma
# Create your views here.
def home (request):
  hobbies = Hobbies.objects.all()
  habilidades = Habilidades.objects.all()
  idiomas = Idioma.objects.all()
  print(hobbies)
  return render (request, "home.html", context={"hobbies": hobbies, "habilidades": habilidades,'idiomas': idiomas })




