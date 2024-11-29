from django.shortcuts import render

from outreach_app.utils import analyze_sentiment
from .models import Activity, Participation
from django.http import HttpResponse

#landingpage
def landingpage(request):
    return render(request, 'landingpage.html')

#landingpage
def admindashboard(request):
    return render(request, 'admindashboard/dashboard.html')



def home(request):
    return HttpResponse("<h1>Welcome to the Community Outreach System</h1>")

def student_dashboard(request):
    activities = Activity.objects.filter(participation__user=request.user)
    return render(request, 'student_dashboard.html', {'activities': activities})

def feedback_submission(request, activity_id):
    if request.method == "POST":
        feedback = request.POST['feedback']
        # Sentiment analysis logic here
        sentiment_score = analyze_sentiment(feedback)  # Placeholder
        Participation.objects.create(user=request.user, activity_id=activity_id, feedback=feedback, sentiment_score=sentiment_score)
    return redirect('student_dashboard')

# outreach_app/views.py
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Redirect to home page after login
    else:
        form = AuthenticationForm()

    return render(request, 'outreach_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# outreach_app/views.py
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):
    # Assuming you have a model named 'Activity'
    activities = Activity.objects.filter(participation__user=request.user)
    return render(request, 'student_dashboard.html', {'activities': activities})

# outreach_app/views.py
from django.shortcuts import render, redirect
from .models import Feedback

def community_feedback(request):
    if request.method == "POST":
        feedback = request.POST.get('feedback')
        # Save the feedback in the database
        Feedback.objects.create(text=feedback)
        return redirect('home')  # Redirect to home after submission

    return render(request, 'community_feedback.html')
