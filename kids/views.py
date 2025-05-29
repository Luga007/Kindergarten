from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden

from .models import Kids, Parent
from django.shortcuts import get_object_or_404, redirect, render
from .forms import KidsForm, ParentForm
from .permissions import can_access_chief, can_access_caretaker, can_access_admin


@login_required(login_url='login')
def kid_data_page(request):
    kids = Kids.objects.all()
    form = None
    create_form = KidsForm()


    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    edit_kid_id = request.POST.get('edit_kid_id') or request.GET.get('edit_kid_id')


    if request.method == 'POST':
        if edit_kid_id:
            kid_to_edit = get_object_or_404(Kids, id=edit_kid_id)
            form = KidsForm(request.POST, instance=kid_to_edit)
            print(form.is_valid())
            print(form.errors)
            print(form)
            if form.is_valid():
                form.save()
                return redirect('kids_page')
        else:

            create_form = KidsForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('kids_page')
    else:

        if edit_kid_id:
            try:
                meal_to_edit = Kids.objects.get(id=edit_kid_id)
                form = KidsForm(instance=meal_to_edit)
            except Kids.DoesNotExist:
                form = None

    context = {
        'kids': kids,
        'form': form,
        'create_form': create_form,
        'edit_kid_id': edit_kid_id,
        'user_role': request.user.role,
    }
    return render(request, 'kids.html', context)


def kid_delete(request, kid_id):
    kid = get_object_or_404(Kids, id=kid_id)
    kid.delete()
    return redirect('kids_page')




@login_required(login_url='login')
def parent_page(request):
    parent = Parent.objects.all()
    form = None
    create_form = ParentForm()

    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'parent.html', )

    edit_ingredient_id = request.GET.get('edit_meal_id')

    if request.method == 'POST':
        if edit_ingredient_id:
            ingredient_to_edit = get_object_or_404(Parent, id=edit_ingredient_id)
            form = ParentForm(request.POST, instance=ingredient_to_edit)
            if form.is_valid():
                form.save()
                return redirect('parent_page')
        else:
            create_form = ParentForm(request.POST)
            print(create_form)
            print(create_form.is_valid())
            print(create_form.errors)
            if create_form.is_valid():
                create_form.save()
                return redirect('parent_page')
    else:
        if edit_ingredient_id:
            try:
                ingredient_to_edit = Parent.objects.get(id=edit_ingredient_id)
                form = ParentForm(instance=ingredient_to_edit)
            except Parent.DoesNotExist:
                form = None
        else:
            form = None

    context = {
        'parents': parent,
        'form': form,
        'create_form': create_form,
        'edit_ingredient_id': edit_ingredient_id,
        'user_role': request.user.role,
    }
    return render(request, 'parent.html', context)


def parent_delete(request, parent_id):
    parent = get_object_or_404(Parent, id=parent_id)
    parent.delete()
    return redirect('parent_page')
