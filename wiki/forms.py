from django import forms
from wiki.models import Page
# from django import render_to_respose



class FriendlyForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)

class PageForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Page
        exclude = (model.slug, model.created, model.modified)
    
    # return render_to_respose('newpage.html', args)
       


