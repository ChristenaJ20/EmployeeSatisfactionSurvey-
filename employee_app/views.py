from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import SurveySubmission

def index(request):
    if request.user.is_authenticated:
        # Redirect to a success page or dashboard page
        full_uri = request.session.get('full_uri', None)
        if full_uri is None:
            return redirect('success')
        else:
            del request.session['full_uri']  # Clear the session variable after using it
            return redirect(full_uri)
    else:
        return redirect('login')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid credentials')
            return render(request, 'login.html')
    else:
        print("Hello")
        request.session['full_uri'] = request.build_absolute_uri("/surveys/")
        print(request.session['full_uri'])
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def success(request):
    return render(request, 'success.html')

@login_required
def survey_form(request):
    """Display and handle employee survey form submission."""
    if request.method == 'POST':
        department = request.POST.get('department', '').strip()
        rating = request.POST.get('rating', '').strip()
        comment = request.POST.get('comment', '').strip()
        anonymous_input = request.POST.get('anonymous', '').strip().lower()
        anonymous = anonymous_input == 'y' or anonymous_input == 'on'
        
        # Validation
        errors = []
        if not department:
            errors.append("Department is required.")
        if not rating:
            errors.append("Rating is required.")
        else:
            try:
                rating = int(rating)
                if rating < 1 or rating > 5:
                    errors.append("Rating must be between 1 and 5.")
            except ValueError:
                errors.append("Rating must be a number between 1 and 5.")
        if not comment:
            errors.append("Comment is required.")
        
        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'survey_form.html', {
                'department': department,
                'rating': rating if isinstance(rating, int) else request.POST.get('rating', ''),
                'comment': comment,
                'anonymous': anonymous
            })
        
        # Save submission
        username = None if anonymous else request.user.username
        submission = SurveySubmission.objects.create(
            department=department,
            rating=rating,
            comment=comment,
            anonymous=anonymous,
            username=username
        )
        messages.success(request, 'Thank you! Survey submitted successfully.')
        return redirect('survey_form')
    
    return render(request, 'survey_form.html')

@login_required
def survey_results(request):
    """Display all survey submissions (sorted by department)."""
    submissions = SurveySubmission.objects.all().order_by('department', '-submitted_at')
    return render(request, 'survey_results.html', {'submissions': submissions})