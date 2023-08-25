from django import forms

class EventsForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')
