from django import forms

class MedicalForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    age = forms.IntegerField(label='Age')
    ##sex = forms.ChoiceField(choices=[('question', 'Question'), ('other', 'Other')])
    height = forms.IntegerField(label='Height')
    weight = forms.IntegerField(label='Weight')
    sbp = forms.IntegerField(label='Systolic Blood Pressure')
    dbp = forms.IntegerField(label='Diastolic Blood Pressure')
