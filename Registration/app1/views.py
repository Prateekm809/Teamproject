from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import AdminsignupForm
from django.http import JsonResponse
from .models import VideoCompletion
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserProfileForm
from .models import UserImage
from .models import UserVideos
from django.core.mail import send_mail
from .models import Visit
from django.views import View
from .forms import UserDataForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import UserData
# Create your views here.

def my_view(request):
    # Get the user's IP address (you may need to handle proxy servers)
    ip_address = request.META.get('REMOTE_ADDR')

    # Create a new Visit object
    visit = Visit(ip_address=ip_address)
    visit.save()

    # Your view logic here

    return render(request, 'home.html')


def visit_count(request):
    # Count the total number of visits
    total_visits = Visit.objects.count()

    return render(request, 'home.html', {'total_visits': total_visits})


@login_required
def mark_video_as_done(request):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        user = request.user
        video_id = request.POST.get('video_id')

        # Get or create the UserVideos instance for the user
        user_videos, created = UserVideos.objects.get_or_create(user=user)

        # Update the corresponding video field to True
        video_field_name = f'video_{video_id}'
        setattr(user_videos, video_field_name, True)
        user_videos.save()

        return JsonResponse({'message': 'Video marked as done.'})

    return JsonResponse({'message': 'Invalid request.'}, status=400)


def upload_image(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if the user already has a UserImage instance
            user_image, created = UserImage.objects.get_or_create(user=request.user)
            user_image.profile_image = form.cleaned_data['profile_image']
            user_image.save()
            return redirect('dashboard')  # Redirect to the user's profile page
    else:
        form = UserProfileForm()

    return render(request, 'upload_image.html', {'form': form})


def HomePage(request):
    return render(request, 'home.html')


@login_required
def WelcomePage(request):
    return render(request, 'welcome.html')

def check_username(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        user_exists = User.objects.filter(username=username).exists()
        return JsonResponse({'exists': user_exists})


def check_email(request):
    if request.method == 'GET':
        email = request.GET.get('email')
        email_exists = User.objects.filter(email=email).exists()
        return JsonResponse({'exists': email_exists})


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        try:
            # Check if passwords match
            if pass1 != pass2:
                raise ValueError("Passwords do not match!")

            # Create user
            my_user = User.objects.create_user(username=uname, email=email, password=pass1)

            # Send email
            message = (
                f"Hii, {uname} Registration Successfully!\nYour details are:\nUsername: {uname}\nEmail: {email}"
                f"\nPassword: {pass1}\nThank you!"
            )
            send_mail(
                "Confirmation Mail",
                message,
                "elevatex08@gmail.com",
                [email],
                fail_silently=False,
            )

            return HttpResponseRedirect("login")

        except Exception as e:
            # Handle exceptions
            error_message = str(e)
            return HttpResponse(f"Registration failed: {error_message}")

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        print(username, pass1)
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('user-data')
        else:
            return HttpResponse('username and password is incorrect!!')
    return render(request, 'login.html')


@login_required
def dashboard(request):
    try:
        # Attempt to retrieve the UserVideos record for the current user
        user_videos = UserVideos.objects.get(user=request.user)
    except UserVideos.DoesNotExist:
        # If the record doesn't exist, create a new one for the user
        user_videos = UserVideos(user=request.user)
        user_videos.save()

    try:
        # Attempt to retrieve the UserData record for the current user
        user_data = UserData.objects.get(user=request.user)
    except UserData.DoesNotExist:
        # If the record doesn't exist, set user_data to None
        user_data = None

    return render(request, 'dashboard.html', {'user_videos': user_videos, 'user_data': user_data})

def mark_video_completed(request):
    if request.method == "POST":
        video_name = request.POST.get("video_name")
        user = request.user

        # Check if the completion record exists and update it
        completion, created = VideoCompletion.objects.get_or_create(
            user=user,
            video_name=video_name,
        )

        if not created:
            completion.completed = True
            completion.save()

        response_data = {'message': 'Video marked as completed'}
        return JsonResponse(response_data)


def logout_view(request):
    logout(request)
    return redirect('home')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            # This is important to keep the user logged in after password change.
            update_session_auth_hash(request, user)
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})


class UserDataView(LoginRequiredMixin, View):
    template_name = 'user_data.html'

    def get(self, request):
        try:
            user_data = UserData.objects.get(user=request.user)
        except UserData.DoesNotExist:
            user_data = UserData(user=request.user)

        # Check if the user has already filled out their data
        if user_data.height is not None and user_data.weight is not None:
            # Determine the redirect URL based on the sport choice
            sport_choice = user_data.sport_choice
            if sport_choice == 'basketball':
                return redirect('basketball')
            elif sport_choice == 'swimming':
                return redirect('swimming')
            elif sport_choice == 'Taekwondo':
                return redirect('Taekwondo')

        form = UserDataForm(instance=user_data)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        try:
            user_data = UserData.objects.get(user=request.user)
        except UserData.DoesNotExist:
            user_data = UserData(user=request.user)

        form = UserDataForm(request.POST, request.FILES, instance=user_data)
        if form.is_valid():
            form.save()
            # Determine the redirect URL based on the sport choice
            sport_choice = form.cleaned_data['sport_choice']
            if sport_choice == 'basketball':
                return redirect('basketball')
            elif sport_choice == 'swimming':
                return redirect('swimming')
            elif sport_choice == 'Taekwondo':
                return redirect('Taekwondo')
            # Redirect the user to their chosen sport's page

        # Handle form validation errors
        return render(request, self.template_name, {'form': form})


def Taekwondo(request):
    return render(request, 'form/welcomepages/Taekwondo.html')


def basketball(request):
    return render(request, 'form/welcomepages/basketball.html')


def swimming(request):
    return render(request, 'form/welcomepages/swimming.html')


@login_required
def user_data_view(request):
    try:
        user_data = UserData.objects.get(user=request.user)
    except UserData.DoesNotExist:
        user_data = None

    return render(request, 'admin_login.html', {'user_data': user_data})
