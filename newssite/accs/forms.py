from newsapp.models import * 
from django.forms import ModelForm

class CreateItemForm(ModelForm):
    class Meta:
        model=Item
        fields=['title','memo','image']

class ChangeItemForm(ModelForm):
    class Meta:
        model=Item
        fields=['title','memo']

class Create_SubItem_Form(ModelForm):
    class Meta:
        model=SubItem
        fields=['title','memo','image','video']
        
class Change_SubItem_Form(ModelForm):
    class Meta:
        model=SubItem
        fields=['title','memo']