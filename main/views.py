from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from django.utils.decorators import method_decorator
from django.template.loader import render_to_string
from django.http import  HttpResponse, JsonResponse
from django.views.generic import TemplateView
from rest_framework.response import Response
# from .serializers import EmailSerializer
from rest_framework.views import APIView
from django.db.models import Max, Count
from django.http import HttpResponse
from django.contrib import messages
from rest_framework import status
from django.conf import settings
# from .utils import search_title
from django.views import View
from .models import *
# Create your views here.
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class Home(TemplateView):
    template_name = "home.html"
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
       
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        
        if 'name' in request.POST and 'apo_email' in request.POST:
            name = request.POST.get('name')
            apo_email = request.POST.get('apo_email')
            try:
                validate_email(apo_email)
                service = request.POST.get('service', None)
                comment = request.POST.get('comment', None)
                Appointment.objects.create(fullname=name, email=apo_email, services=service, comments=comment)
                messages.success(request, "Appointment booked successfully.")
            except ValidationError:
                messages.error(request, "Invalid email address for appointment.")
        
        return redirect('home')
    
    
class ContactView(TemplateView):
    template_name = "contact.html"

    def get(self, request):
        context = {"title":"Contact Us"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        
        if 'fullname' in request.POST and 'email' in request.POST and 'phone_number' in request.POST:
            name = request.POST.get('fullname')
            email = request.POST.get('email')
            phone_number = request.POST.get('phone_number')
            try:
                  
                validate_email(email)
                # service = request.POST.get('service', None)
                # comment = request.POST.get('comment', None)
                # company_name = request.POST.get('company_name', None)
                existing_customer = request.POST.get('existingCustomer', None)
                enquiry_type = request.POST.get('enquiryType', None)
                callback_team = request.POST.get('callbackFrom', None)
                contactusnew.objects.create(fullname=name, email=email, phonenumber = phone_number ,existing_customer=existing_customer, enquiry_type=enquiry_type,callback_team=callback_team)
                messages.success(request, "Appointment booked successfully.")
            except ValidationError:
                messages.error(request, "Invalid email address for appointment.")

        return redirect('contact')


class AboutUS(TemplateView):
    template_name = "about.html"

    def get(self, request):
        context = {"title":"About Us"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('about')


class ProductAndService(TemplateView):
    template_name = "product_and_service.html"

    def get(self, request):
        context = {"title":"Products & Service Details"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('productandservices')
    

class SolarPowerSystem(TemplateView):
    template_name = "solar_power_system.html"

    def get(self, request):
        context = {"title":"Solar Power System"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('solarpowersystem')
    

class VectoriaRebate(TemplateView):
    template_name = "victoria_rebate.html"

    def get(self, request):
        context = {"title":"Victoria Rebate"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('vectoriarebate')
    

class Blog(TemplateView):
    template_name = "blog.html"

    def get(self, request):
        context = {"title":"Victoria Rebate"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('blog')

class KnowledgeCenter(TemplateView):
    template_name = "knowledge_center.html"

    def get(self, request):
        context = {"title":"Knowledge Center"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('knowledgecenter')

class LatestNews(TemplateView):
    template_name = "latest_news.html"

    def get(self, request):
        context = {"title":"Latest News"}
        return render(request, self.template_name,context)

    def post(self, request):
        if 'sub_email' in request.POST:
            sub_email = request.POST.get('sub_email')
            try:
                validate_email(sub_email)
                UserMail.objects.create(email=sub_email)
                messages.success(request, "Subscription successful.")
            except ValidationError:
                messages.error(request, "Invalid email address.")
        return redirect('latestnews')