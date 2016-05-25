from rest_framework import viewsets
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Statement
from .serializers import StatementSerializer


class ChatterboxViewSet(viewsets.ModelViewSet):

    queryset = Statement.objects.all().order_by('created')
    serializer_class = StatementSerializer

class ChatterboxView(TemplateView):

    template_name = "chatterbox/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['text'] = Statement.objects.all()
        return context

    def get(self, request):
        context = self.get_context_data()
        return render(request, "chatterbox/home.html", context)
