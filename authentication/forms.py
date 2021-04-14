from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):
    PLATFORM_CHOICES = (
        ("1", "PC"),
        ("2", "PS5"),
        ("3", "XSX"),
        ("4", "Switch"),
        ("5", "iOS"),
        ("6", "Android"),
        ("7", "Arcade"),
        ("8", "PS4"),
        ("9", "PS3"),
        ("10", "Xbox One"),
        ("11", "Xbox 360"),
        ("12", "Sega"),
        ("13", "Wii U"),
        ("14", "Wii"),
        ("15", "PSP"),
        ("16", "Vita"),
        ("17", "3DS"),
        ("18", "RetoPy"),
        ("19", "Other Systems"),
    )
    avatar = forms.ImageField()
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField(max_length=140)
    platform_choice_field = forms.CharField(
        label="Favorite Platform",
        max_length=2,
        widget=forms.Select(choices=PLATFORM_CHOICES),
<<<<<<< HEAD
    )
    avatar = forms.ImageField(required=False)
=======
    )
>>>>>>> d6e1c839c5f3a830124cd30cb60c2adf81869c58
