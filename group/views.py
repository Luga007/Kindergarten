from django.shortcuts import render
from . models import Group
from django.shortcuts import get_object_or_404, redirect, render
from . forms import GroupForm
from django.contrib.auth.decorators import login_required
from .permissions import can_access_caretaker, can_access_admin, can_access_chief



@login_required(login_url='login')
def group_data_page(request):
    groups = Group.objects.all()
    form = None
    create_form = GroupForm()

    edit_group_id = request.GET.get('edit_group_id')
    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'group.html', )

    if request.method == 'POST':
        if edit_group_id:
            meal_to_edit = get_object_or_404(Group, id=edit_group_id)
            form = GroupForm(request.POST, instance=meal_to_edit)
            if form.is_valid():
                form.save()
                return redirect('group_data_page')
        else:

            create_form = GroupForm(request.POST)
            if create_form.is_valid():
                create_form.save()
                return redirect('group_data_page')
    else:

        if edit_group_id:
            try:
                meal_to_edit = Group.objects.get(id=edit_group_id)
                form = GroupForm(instance=meal_to_edit)
            except Group.DoesNotExist:
                form = None

    context = {
        'groups': groups,
        'form': form,
        'create_form': create_form,
        'edit_group_id': edit_group_id,
        'user_role': request.user.role,
    }
    return render(request, 'group.html', context)


def delete_group(request, group_id):
    groups = get_object_or_404(Group, id=group_id)
    groups.delete()
    return redirect('group_data_page')
