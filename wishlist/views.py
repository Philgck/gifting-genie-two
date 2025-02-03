from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import WishlistItemForm
from .models import WishlistItem
from myaccount.models import MyAccount


@login_required
def add_wishlist_item(request):
    if request.method == 'POST':
        form = WishlistItemForm(request.POST)
        if form.is_valid():
            wishlist_item = form.save(commit=False)
            wishlist_item.user = request.user
            wishlist_item.save()
            messages.success(request, 'Wishlist item added successfully!')
            return redirect('wishlist', user_id=request.user.id)
    else:
        form = WishlistItemForm()
        myaccount = MyAccount.objects.get(user=request.user)
    return render(request, 'wishlist/add_wishlist_item.html', {'form': form, 'myaccount': myaccount})


@login_required
def wishlist_view(request, user_id):
    wishlist_items = WishlistItem.objects.filter(user_id=user_id)
    myaccount = MyAccount.objects.get(user_id=user_id)
    return render(request, 'wishlist/wishlist.html', {'myaccount': myaccount, 'wishlist_items': wishlist_items})


@login_required
def edit_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    if request.method == 'POST':
        form = WishlistItemForm(request.POST, instance=wishlist_item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Wishlist item updated successfully!')
            return redirect('wishlist', user_id=request.user.id)
    else:
        form = WishlistItemForm(instance=wishlist_item)
        myaccount = MyAccount.objects.get(user=request.user)
    return render(request, 'wishlist/edit_wishlist_item.html', {'myaccount': myaccount, 'form': form})


@login_required
def delete_wishlist_item(request, item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=item_id, user=request.user)
    if request.method == 'POST':
        wishlist_item.delete()
        return redirect('wishlist', user_id=request.user.id)
    myaccount = MyAccount.objects.get(user=request.user)
    return render(request, 'wishlist/delete_wishlist_item.html', {'wishlist_item': wishlist_item, 'myaccount': myaccount})