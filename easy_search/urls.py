from django.conf.urls import url

from .views import EasySearchResultsView


urlpatterns = [
    url(r'^$', EasySearchResultsView.as_view(), name='search-results')
]
