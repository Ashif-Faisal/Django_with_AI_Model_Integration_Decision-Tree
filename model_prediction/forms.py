from django import forms


class PredictionForm(forms.Form):
    class Meta:
        fields = ['age','income', 'gender', 'm_status']
