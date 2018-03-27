from django.shortcuts import render

from django.views.generic import DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse

from books.models import Review, Category
from .models import Votation


class VotationDetailView(DetailView):
	def get_queryset(self):
		return Votation.objects.all()

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)

		vot = kwargs.get('object')
		vot_books = vot.book_set.all() # vot.get_ordered()

		almost_hard_coded_url = reverse('votations:votation_list', kwargs={'slug':vot.category.slug})

		context['books'] = vot_books
		context['url'] = almost_hard_coded_url

		return context

	# def get_object(self):
	# 	cat_slug = self.kwargs.get('category')
	# 	cat = get_object_or_404(Category, slug__iexact = cat_slug)
	# 	obj = get_object_or_404()
	# 	return Votation.objects.all()

class VotationCategoryListView(DetailView):
	template_name = 'votations/votation_list.html'
	def get_object(self):
		cat_slug = self.kwargs.get('slug')
		cat = get_object_or_404(Category, slug__iexact=cat_slug)
		return cat

	def get_context_data(self, *args, **kwargs):
		print('ja', self.object)
		ctx = super().get_context_data(**kwargs)

		vots = Votation.objects.filter(category=self.object)
		ctx['votations'] = vots

		return ctx


