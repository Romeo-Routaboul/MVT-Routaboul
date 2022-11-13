from django.http import HttpResponse
from AppCoder.models import*
from django.template import loader

# Create your views here.


def datos_plantilla(request):
    objetos = Familiar.objects.all()
    diccionario = {"familia": objetos}
    plantilla = loader.get_template("plantillados.html")
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
    
