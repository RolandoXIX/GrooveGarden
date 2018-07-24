from django.shortcuts import render_to_response

# Create your views here.


def inicio(request):
    return render_to_response('inicio.html', context={"active":"inicio"})


def promociones(request):
    return render_to_response('promociones.html', context={"active":"promociones"})