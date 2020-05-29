from django import forms


class AddTweetForm(forms.Form):
    body = forms.CharField(
        widget=forms.Textarea,
        max_length=140
        )
