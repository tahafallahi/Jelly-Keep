from django.shortcuts import render
from django.urls import reverse_lazy
from word.models import Word
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from word import api


class WordListView(ListView):
    model = Word
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class WordCreateView(CreateView):
    model = Word
    fields = ['title']
    success_url = reverse_lazy('word:list')
    def form_valid(self, form):
        object = form.save(commit=False)
        object.title = object.title.capitalize()
        object.user = self.request.user
        object.dict_url = api.get_page_url(object.title)
        object.audio_url = api.get_mp3(object.dict_url)
        return super().form_valid(form)


class WordDeleteView(DeleteView):
    model = Word
    success_url = reverse_lazy('word:list')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
