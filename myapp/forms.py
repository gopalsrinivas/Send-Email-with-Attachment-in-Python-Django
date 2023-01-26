from django import forms

class EmailForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"name"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","id":"email"}))
    mobile = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"mobile"}))
    subject = forms.CharField(max_length=200,widget=forms.TextInput(attrs={"class":"form-control","id":"subject"}))
    message = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","id":"message",'rows':3}))
    attach = forms.FileField()
