from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .permissions import can_access_caretaker, can_access_admin, can_access_chief
from inventory.models import Inventory
from django.db.models import Sum
from datetime import timedelta, date
import json
from group.models import Group
from kids.models import Kids


@login_required(login_url='login')
def main(request):
    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'kids.html', )

    inventory_labels = list(Inventory.objects.filter(is_active=True).values_list('ingredients__name', flat=True))
    inventory_values = list(Inventory.objects.filter(is_active=True).values_list('overall_kg', flat=True))
    ctx = {
        'user_role': request.user.role,
        'inventory_labels': inventory_labels,
        'inventory_values': inventory_values,

    }

    return render(request, 'base.html', ctx)