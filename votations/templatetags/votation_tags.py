import datetime, pytz

from django import template

from django.db.models import Count
from django.db.models import Q

from books.models import Book, Category
from votations.models import Votation

register = template.Library()


# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)

@register.inclusion_tag('votations/time_left.html')
def get_time_left(user, category):
	user_tz = user.profile.timezone

	user_now_aware = datetime.datetime.now(pytz.timezone(user_tz))
	user_now_naive = user_now_aware.replace(tzinfo=None)

	current_votations = Votation.objects.get(
											Q(category=category) &
											Q(start_week__lt=user_now_naive) &
											Q(end_week__gt=user_now_naive)
											)

	print('Found: ', current_votations)


	if current_votations.start_vots<user_now_aware:
		started = True



	diff = current_votations.start_vots - user_now_aware

	d 	 = diff.days
	m, s = divmod(diff.seconds, 60)
	h, m = divmod(m, 60)

	started = False


	return {'d': d, 'h': h, 'm': m, 's': s, 'started': started}