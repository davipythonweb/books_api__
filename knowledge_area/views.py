from rest_framework import generics
from knowledge_area.models import Knowledge_Area

from knowledge_area.serializers import KnowledgeAreaSerilizer



# fluxo de criação dos apps:
"""
models
views
serializers
urls
tests
admin
"""



"""
trilha do projeto.

area de conhecimento = knowledge_area  #equivalente a {genres}

assuntos = matters #equivalente a {actors}

escritores = writers #equivalente tambem a {actors} 

livros = books #equivalente a {movies}


avaliações = reviews #equivalente a {reviews}
(choices com uma lista com as estrelas possiveis para avaliar.)
 
"""



class KnowledgeAreaCreateListView(generics.ListCreateAPIView):
    queryset = Knowledge_Area.objects.all()
    serializer_class = KnowledgeAreaSerilizer

class KnowledgeAreaRetrieveUpdateDestoyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Knowledge_Area.objects.all()
    serializer_class = KnowledgeAreaSerilizer