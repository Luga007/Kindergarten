from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import CareTakerManger, Caretaker
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm, UserCreationForm, UserUpdateForm
from .permissions import can_access_caretaker, can_access_admin, can_access_chief

def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form.is_valid())
        print(form)
        print(form.errors)
        if form.is_valid():
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    form = LoginForm()
    ctx = {'form': form}
    return render(request, 'login-v2.html', ctx)



def caretakerpage(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if not can_access_caretaker(request.user):
        return render(request, 'caretakerdata.html')
    caretaker = Caretaker.objects.all()
    form = None
    create_form = UserCreationForm()

    edit_caretaker_id = request.GET.get('edit_caretaker_id')

    if request.method == 'POST':
        if edit_caretaker_id:
            caretaker_to_edit = get_object_or_404(Caretaker, id=edit_caretaker_id)
            form = UserUpdateForm(request.POST, instance=caretaker_to_edit)
            if form.is_valid():
                form.save()
                return redirect('caretakerpage')
        else:

            create_form = UserCreationForm(request.POST)
            print(create_form)
            print(create_form.is_valid())
            print(create_form.errors)
            if create_form.is_valid():
                create_form.save()
                return redirect('caretakerpage')
    else:

        if edit_caretaker_id:
            try:
                meal_to_edit = Caretaker.objects.get(id=edit_caretaker_id)
                form = UserUpdateForm(instance=meal_to_edit)
            except Caretaker.DoesNotExist:
                form = None

    context = {
        'caretakers': caretaker,
        'form': form,
        'create_form': create_form,
        'edit_caretaker_id': edit_caretaker_id,
        'user_role': request.user.role,
    }
    return render(request, 'caretakerdata.html', context)


def delete_user(request, caretaker_id):
    user = get_object_or_404(Caretaker, id=caretaker_id)
    user.delete()
    return redirect('caretakerpage')


