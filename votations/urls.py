from django.conf.urls import url
from django.contrib import admin

# from django.conf.urls.i18n import i18n_patterns

from .views import VotationDetailView, VotationCategoryListView

urlpatterns = [
	url(r'^(?P<pk>\d)/$', VotationDetailView.as_view(), name='votation_detail'),
	url(r'^(?P<slug>[\w-]+)/all/$', VotationCategoryListView.as_view(), name='votation_list'),
	# url(r'^(?P<pk>\d)/(?P<month>[\w-]+)/(?P<position>[\w-]+)/$', VotationDetailView.as_view(), name='votations_detail'),
]