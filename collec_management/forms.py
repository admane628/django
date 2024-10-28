from django.forms import ModelForm
from .models import Collec

class CollectionForm(ModelForm):
	class Meta:
		model = Collec
		fields = ["title", "description"]