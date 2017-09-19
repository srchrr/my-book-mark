from django.shortcuts import render
from django.views.generic import ListView, DateDetailView
# Create your views here.
from .models import Bookmark

class BookmarkListV(ListView):
    model = Bookmark

class BookmarkDetailV(DateDetailView):
    model = Bookmark


