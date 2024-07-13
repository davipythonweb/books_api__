from django.shortcuts import render
from django.http import HttpResponse


"""
trilha do projeto.

area de conhecimento = knowledge_area  #equivalente a {genres}

livros = books #equivalente a {movies}

assuntos = matters #equivalente a {actors}

avaliações = reviews #equivalente a {reviews}
(choices com uma lista com as estrelas possiveis para avaliar.)
 
"""

def knowledge_area(request):
    return HttpResponse('Books_API')


