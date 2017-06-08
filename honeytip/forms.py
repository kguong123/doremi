from .models import HoneyTip, Contents
from django.forms import ModelForm, inlineformset_factory


class HoneyTipForm(ModelForm):
    class Meta:
        model = HoneyTip
        exclude = ('slug', 'create_date', 'hit_count_generic', 'app_name')

class ContentsForm(ModelForm):
    class Meta:
        model = Contents
        exclude = ()   




HoneyTipInlineFormSet = inlineformset_factory(HoneyTip, Contents, form=ContentsForm, extra=2, can_delete=True)



