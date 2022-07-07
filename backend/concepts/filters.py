import django_filters


class NumberInFilter(django_filters.BaseInFilter, django_filters.NumberFilter):
    pass


class ConceptFilter(django_filters.FilterSet):
    concept_id__in = NumberInFilter(field_name="concept_id", lookup_expr="in")



