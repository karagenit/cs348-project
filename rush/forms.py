from django import forms

class StudentLoginForm(forms.Form):
    puid = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class":"form-control",
    }))
class StudentRegistration(forms.Form):
    Name = forms.CharField(max_length=200)
    Email = forms.CharField(
        required=False,
    )
    Phone = forms.CharField(
        required=False,
    )
    Major = forms.CharField(
        max_length=200, 
        required=False,
    )
    GPA = forms.DecimalField(max_digits=3, decimal_places=2, required=False)
    Hometown = forms.CharField(max_length=200, required=False)
    CHOICES = (('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'),('SR', 'Senior & Above'),)
    Grade = forms.ChoiceField(choices=CHOICES, required=False)