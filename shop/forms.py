from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required = True, help_text='Required.')
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)

    class Meta:
        model = User #model User comes with username, email, first name, last name , pass1 and pass2 fields
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
        )

    def save(self, commit = True):
        user =  super(RegistrationForm, self).save(commit = False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name =  self.cleaned_data['last_name']
        user.email =  self.cleaned_data['email']

        #note password is saved automatically in User models original save()
        # function, everything else needs to be done manually as done above
        if commit:
            user.is_active = True
            user.save()

            return user
