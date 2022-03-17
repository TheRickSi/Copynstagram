from users.models import Profile
from django import forms
from django.contrib.auth.hashers import make_password
from users.models import User


class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=True)
    phone_number = forms.CharField(max_length=20, required=True)
    picture = forms.ImageField(required=False)


class SignupForm(forms.Form):
    username = forms.CharField(
        min_length=4,
        max_length=50,
        widget=forms.TextInput(
            attrs={'placeholder':'Username','class': 'form-control','required': True}
        )
    )

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password','class': 'form-control','required': True}
        )
    )

    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput(
            attrs={'placeholder':'Password Confirmation ','class': 'form-control','required': True}
        )
    )

    first_name = forms.CharField(
        max_length=50,
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder':'First Name','class': 'form-control','required': True}
        )
    )

    last_name = forms.CharField(
        max_length=50,
        min_length=2,
        widget=forms.TextInput(
            attrs={'placeholder':'Last Name','class': 'form-control  ','required': True}
        )
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={'placeholder':'Email','class': 'form-control','required': True}
        ),
        min_length=6,
        max_length=70
    )

    def clean_username(self):
        username = self.cleaned_data["username"]
        template_conf=self.fields.get("username").widget.attrs
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            template_conf['class']='form-control is-invalid'
            self.fields.get("username").widget.attrs = template_conf
            raise forms.ValidationError('Username is already in Use.')
        return username

    def clean(self):
        """Verify Password confirmation match."""
        data = super().clean()
        password = data['password']
        password_confirmation = data['password_confirmation']
        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data
    
    def save(self):
        data=self.cleaned_data 
        data.pop('password_confirmation')
        data['password']=make_password(data['password'])
        user= User.objects.create(**data)
        profile= Profile.objects.create(user=user)
        profile.save()