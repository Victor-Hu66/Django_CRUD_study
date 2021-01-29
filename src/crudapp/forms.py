from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    # first_name = forms.CharField(label="Your name")
    
    class Meta:
        model =Student
        fields = '__all__'  #("first_name", "last_name")
       
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = "My name"
        
            
        