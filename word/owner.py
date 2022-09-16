from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin


class OwnerDetailView(LoginRequiredMixin, DetailView):
    pass

class OwnerListView(LoginRequiredMixin, ListView):
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)

class OwnerCreateView(LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        object = form.save(commit=False)
        object.user = self.request.user
        return super().form_valid(form)

class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    pass

class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    pass
