from django import forms
TLD_CHOICES=(
    ('com.au','Australian'),
    ('co.za','South Africa',),
    ('co.uk','British'),
    ('co.in','Indian'),
    ('ca','Canadian'),
    ('ie','Irish'),
    ('es','Spanish')
)
class TextForm(forms.Form):
    tld = forms.ChoiceField(choices=TLD_CHOICES,label="Enter your accent",widget=forms.Select(attrs={'class':'form-control'}))
    text= forms.CharField(label="Enter your text",widget=forms.Textarea(attrs={'rows':6,'cols':65,'class':'p-2 mt-0 mb-1'}))