from django import forms


class game_form(forms.Form):
    PLATFORM_CHOICES = (
        ("01", "PC"),
        ("02", "PS5"),
        ("03", "XSX"),
        ("04", "Switch"),
        ("05", "iOS"),
        ("06", "Android"),
        ("07", "Arcade"),
        ("08", "PS4"),
        ("09", "PS3"),
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
    cover_art = forms.ImageField()
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    platform = forms.ChoiceField(choices=PLATFORM_CHOICES)
