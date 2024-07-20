from rest_framework import generics
from knowledge_area.models import Knowledge_Area

from knowledge_area.serializers import KnowledgeAreaSerilizer


"""
trilha do projeto.

area de conhecimento = knowledge_area  #equivalente a {genres}

livros = books #equivalente a {movies}

assuntos = matters #equivalente a {actors}

avaliações = reviews #equivalente a {reviews}
(choices com uma lista com as estrelas possiveis para avaliar.)
 
"""

class KnowledgeAreaCreateListView(generics.ListCreateAPIView):
    queryset = Knowledge_Area.objects.all()
    serializer_class = KnowledgeAreaSerilizer
