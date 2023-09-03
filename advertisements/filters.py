from django_filters import rest_framework as filters, DateFromToRangeFilter, ChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""
    created_at = DateFromToRangeFilter()
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)
    # TODO: задайте требуемые фильтры

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']

