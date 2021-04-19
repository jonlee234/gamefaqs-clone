from django import forms


class game_form(forms.Form):
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
    cover_art = forms.ImageField(required=False)
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)


class SearchBar(forms.Form):
    search = forms.CharField()
