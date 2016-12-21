from django import template #show template library
from tutorial_app.models import Category

register = template.Library()

# ^ creates registry of custom work 

@register.inclusion_tag('cat.html') #create this file and insert to sidebar
def get_category_list(cat=None): #by default it will not highlight any categories
	return {'cats': Category.objects.all(), 'act_cat':cat}

@register.filter(name='addcls')
def addcls(value,cls):
	return value.as_widget(attrs={'class':cls})