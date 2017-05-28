from .models import HoneyTip, Contents
from django.forms.models import inlineformset_factory

HoneyTipInlineFormSet = inlineformset_factory(HoneyTip, Contents,
    fields = ['honeyimage','honeydescription'],
    extra = 1)

