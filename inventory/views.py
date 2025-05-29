from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import InventoryForm
from django.shortcuts import render, get_object_or_404, redirect
from .permissions import can_access_caretaker, can_access_admin, can_access_chief
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync


@login_required(login_url='login')
def inventory_page(request):
    inventory = Inventory.objects.all()
    form = None
    create_form = InventoryForm()
    if not can_access_caretaker and can_access_chief(request.user):
        return render(request, 'inventory.html', )

    edit_inventory_id = request.GET.get('edit_meal_id')

    if request.method == 'POST':
        if edit_inventory_id:
            inventory_to_edit = get_object_or_404(Inventory, id=edit_inventory_id)
            form = InventoryForm(request.POST, instance=inventory_to_edit)
            if form.is_valid():
                form.save()
                return redirect('inventory_page')
        else:
            create_form = InventoryForm(request.POST)
            print(create_form)
            print(create_form.is_valid())
            print(create_form.errors)
            if create_form.is_valid():
                create_form.save()
                return redirect('inventory_page')
    else:
        if edit_inventory_id:
            try:
                ingredient_to_edit = Inventory.objects.get(id=edit_inventory_id)
                form = InventoryForm(instance=ingredient_to_edit)
            except Inventory.DoesNotExist:
                form = None
        else:
            form = None

    context = {
        'inventories': inventory,
        'form': form,
        'create_form': create_form,
        'edit_inventory_id': edit_inventory_id,
        'user_role': request.user.role,
    }
    return render(request, 'inventory.html', context)


def delete_inventory(request, inventory_id):
    inventory = get_object_or_404(Inventory, id=inventory_id)
    inventory.delete()
    return redirect('inventory_page')


def low_stock_alerts(request):
    low_items = Inventory.objects.filter(overall_kg__lt=10)
    return render(request, 'alert.html', {'low_items': low_items})
