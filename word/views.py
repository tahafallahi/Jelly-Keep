from django.shortcuts import render
from django.urls import reverse_lazy
from word.models import Word
from django.views.generic import ListView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from word import api


class WordListView(LoginRequiredMixin, ListView):
    model = Word
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class WordCreateView(LoginRequiredMixin, CreateView):
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

class WordDeleteListView(LoginRequiredMixin, ListView):
    model = Word

    def get_template_names(self):
        return ['word/delete_word_list.html']

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class WordDeleteView(LoginRequiredMixin, DeleteView):
    model = Word
    success_url = reverse_lazy('word:delete_list')
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)
