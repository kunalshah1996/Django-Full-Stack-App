from rest_framework import serializers

from .models import Concept

class ConceptSerializer(serializers.ModelSerializer):
    class Meta:
        model=Concept
        fields=['concept_id', 'concept_name','domain_id','vocabulary_id','concept_class_id','concept_code']
