from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Course, Event
from .forms import FeedbackForm
class IndexView(View):
    def get(self,request):
        courses = Course.objects.all()
        events = Event.objects.all()[:4]
        form = FeedbackForm()
        data = {
            'courses':courses,
            'form':form,
            'events':events
        }
        return render(request,'index.html',context=data)

    def post(self,request):
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

class EventsView(View):
    def get(self,request):
        events = Event.objects.all()
        return render(request, 'meetings.html',context={'events':events})

class EventDetailView(View):
    def get(self,request,id):
        event = Event.objects.get(id=id)
        return render(request, 'meeting-details.html',context={'event':event})