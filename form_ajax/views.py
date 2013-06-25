import django.utils.simplejson as json

from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django import forms
from django.template.context import RequestContext

from django.forms.widgets import Input
class Html5EmailInput(Input):
    input_type = 'email'

class ContactForm(forms.Form):
    name = forms.CharField(max_length=30)
    firstname = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=50, widget=Html5EmailInput())
    message = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=50, widget=forms.PasswordInput())

    def clean_password(self):
        password = self.cleaned_data['password']
        length = len(password)
        if length < 8:
            raise forms.ValidationError("Password has to be at least 8 characters long.")
        return password

def contact(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            name = form.cleaned_data['name']
            firstname = form.cleaned_data['firstname']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            password = form.cleaned_data['password']
            # do_something

            # then return
            if  request.is_ajax():
            	return HttpResponse(content=json.dumps({'success' : '/success'}), mimetype='application/json')
            return redirect('success') # Redirect after POST
    else:
        form = ContactForm() # An unbound form
    return render_to_response('form_ajax/form.html', {'form' : form}, context_instance=RequestContext(request))


def success(request):
    return HttpResponse('success')