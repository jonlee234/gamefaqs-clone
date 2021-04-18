from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class SignupForm(forms.Form):
    PLATFORM_CHOICES = (
        ("PC", "PC"),
        ("PS5", "PS5"),
        ("XSX", "XSX"),
        ("Switch", "Switch"),
        ("iOS", "iOS"),
        ("Android", "Android"),
        ("Arcade", "Arcade"),
        ("PS4", "PS4"),
        ("PS3", "PS3"),
        ("Xbox One", "Xbox One"),
        ("Xbox 360", "Xbox 360"),
        ("Sega", "Sega"),
        ("Wii U", "Wii U"),
        ("Wii", "Wii"),
        ("PSP", "PSP"),
        ("Vita", "Vita"),
        ("3DS", "3DS"),
        ("RetoPy", "RetoPy"),
        ("Other Systems", "Other Systems"),
    )
    avatar = forms.ImageField(required=False)
    email = forms.EmailField()
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())
    bio = forms.CharField(max_length=140)
    platform_choice_field = forms.CharField(
        label="Favorite Platform",
        max_length=2,
        widget=forms.Select(choices=PLATFORM_CHOICES),
    )
