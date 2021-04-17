from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse



def landing_page (request): #this is the views for my landing page
    return render (request, 'welcome/index.html')

