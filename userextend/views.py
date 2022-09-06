from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView

from boardgame_library.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm
from userextend.models import UserExtend


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save()

            subject = 'Create a new account'
            message = None
            html_message1 = render_to_string('email.html', {'current_user': new_user})
            send_mail(subject, message, EMAIL_HOST_USER, [new_user.email], html_message=html_message1)

            return redirect('login')
