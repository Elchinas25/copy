import json

from django.db import models
from django.db.models.signals import pre_save
from django.contrib.postgres.fields import JSONField
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse




class Votation(models.Model):
	category 	= models.ForeignKey('books.Category', on_delete=models.CASCADE, null=True)

	timestamp 	= models.DateField(auto_now_add=True, editable=False)
	active 		= models.NullBooleanField(default=False, blank=True)
	started 	= models.NullBooleanField(default=False, blank=True)

	start_week = models.DateTimeField(null=True)
	start_vots = models.DateTimeField(null=True)
	end_week 	= models.DateTimeField(null=True)

	MONTHS = (
			('ja', _('January')),
			('fe', _('February')),
			('ma', _('March')),
			('ap', _('April')),
			('may', _('May')),
			('ju', _('June')),
			('jul', _('July')),
			('au', _('August')),
			('se', _('September')),
			('oc', _('October')),
			('no', _('November')),
			('de', _('December')),
		)

	ORDER = (
			('f', _('First')),
			('s', _('Second')),
			('t', _('Third')),
		)

	month  		= models.CharField(max_length=4, choices=MONTHS, null=True)
	position	= models.CharField(max_length=2, choices=ORDER, null=True)


	def __str__(self):
		return "{}. {} {} {}".format(self.category.title, self.get_position_display(), _('votation for'), self.get_month_display())

	def get_absolute_url(self):
		return reverse('votations:votation_detail', kwargs = {'pk': self.pk})


	# NOT TESTED
	# def get_previous_votations(self): # Assumes values for possition and month are numbers in the db AND default order is newest
	# 	if self.position != 1:
	# 		last_votations = Votation.objects.get(category=self.category, position=self.position-1)
	# 	else:
	# 		last_month = self.month - 1
	# 		last_votations = Votation.objects.filter(category=self.category, month=last_month)[0] #Bc or ordering

	# 	return last_votations



class Rating(models.Model):
	ratings		= JSONField(null=True, editable=True)
	average 	= models.FloatField(default=5)

	def rate(self, vote, user):
		numbers = json.loads(self.ratings['numbers'])

		numbers.append(float(vote))
		self.average = sum(numbers)/float(len(numbers))

		self.ratings['numbers'] = json.dumps(numbers)
		self.save()

		user.profile.books_rated.add(self)

	def __str__(self):
		return 'Rating model for: "{}"'.format(self.book.title)




def pre_save_rating_receiver(sender, instance, *args, **kwargs):
	if not instance.ratings:
		instance.ratings = {'numbers': '[5]'}

pre_save.connect(pre_save_rating_receiver, sender=Rating)


