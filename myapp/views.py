from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.core.mail import EmailMessage,send_mail,EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from .forms import EmailForm

class EmailAttachementView(View):
    form_class = EmailForm
    template_name = 'myapp/sendmail.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'email_form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)

        if form.is_valid():
            
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            attach = request.FILES['attach']

            ctx = {
                'name' : name,
                'email' : email,
                'mobileno' : mobile,
                'subject' : subject,
                'message' : message
            }

            message = render_to_string('myapp/mail.html', ctx)

           # send_mail('Contact Form Enquiry', message, settings.EMAIL_HOST_USER, ['gopalsrinivas.b@gmail.com'], fail_silently=False, html_message=message) 2nd method
            mail = EmailMultiAlternatives(subject, message, settings.EMAIL_HOST_USER, ['gopalsrinivas.b@gmail.com'],[email])
            mail.attach(attach.name, attach.read(), attach.content_type)
            mail.attach_alternative(message, "text/html")
            try:
                mail.send()
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Sent email to %s'%email})
            except:
                return render(request, self.template_name, {'email_form': form, 'error_message': 'Either the attachment is too big or corrupt'})

        return render(request, self.template_name, {'email_form': form, 'error_message': 'Unable to send email. Please try again later'})