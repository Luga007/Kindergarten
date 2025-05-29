from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Attendance
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AttendanceForm
from .permissions import can_access_chief,can_access_admin,can_access_caretaker

@login_required(login_url='login')
def attendance_page(request):
    attendance = Attendance.objects.all()
    form = None
    create_form = AttendanceForm()

    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    edit_ingredient_id = request.GET.get('edit_meal_id')

    if request.method == 'POST':
        if edit_ingredient_id:
            ingredient_to_edit = get_object_or_404(Attendance, id=edit_ingredient_id)
            form = AttendanceForm(request.POST, instance=ingredient_to_edit)
            if form.is_valid():
                form.save()
                return redirect('attendance_page')
        else:
            create_form = AttendanceForm(request.POST)
            print(create_form)
            print(create_form.is_valid())
            print(create_form.errors)
            if create_form.is_valid():
                create_form.save()
                return redirect('attendance_page')
    else:
        if edit_ingredient_id:
            try:
                ingredient_to_edit = Attendance.objects.get(id=edit_ingredient_id)
                form = AttendanceForm(instance=ingredient_to_edit)
            except Attendance.DoesNotExist:
                form = None
        else:
            form = None

    context = {
        'attendances': attendance,
        'form': form,
        'create_form': create_form,
        'edit_ingredient_id': edit_ingredient_id,
        'user_role': request.user.role,
    }
    return render(request, 'attendance.html', context)


def delete_attendance(request, attendance_id):
    attendance = get_object_or_404(Attendance, id=attendance_id)
    attendance.delete()
    return redirect('attendance_page')