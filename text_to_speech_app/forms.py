from django import forms

class TextForm(forms.Form):
    accent = forms.ChoiceField()
    text= forms.CharField(widget=forms.Textarea(attrs={'rows':6,'cols':60}))