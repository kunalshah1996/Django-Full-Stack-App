from rest_framework import generics
from django_filters import rest_framework as filters
from .filters import ConceptFilter


from .models import Concept
from .serializers import ConceptSerializer

class ConceptDetailAPIView(generics.RetrieveAPIView):
    queryset=Concept.objects.all()
    serializer_class=ConceptSerializer

concept_detail_view = ConceptDetailAPIView.as_view()

class ConceptListView(generics.ListAPIView):
    queryset=Concept.objects.all()
    serializer_class=ConceptSerializer


concept_list_view=ConceptListView.as_view()

class ConceptFilterListView(generics.ListAPIView):

    queryset=Concept.objects.all()
    serializer_class=ConceptSerializer
    filter_backends = [filters.DjangoFilterBackend, ]
    filterset_class = ConceptFilter

concept_filter_list_view=ConceptFilterListView.as_view()


class ConceptSearchView(generics.ListAPIView):

    serializer_class = ConceptSerializer
    

    def get_queryset(self):
        concept_name = self.request.query_params.get('concept_name',None)
        return Concept.objects.filter(concept_name__icontains=concept_name)

concept_search_view=ConceptSearchView.as_view()
