from django.shortcuts import render, redirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import MyAccount
from .models import MyAccount
from .forms import ProfileImageForm
from django.contrib import messages

@login_required
def profile_view(request, user_id):
#    myaccount, created = MyAccount.objects.get_or_create(user=request.user)
#    return render(request, 'myaccount/profile.html', {'myaccount': myaccount})
    myaccount = get_object_or_404(MyAccount, user_id=user_id)

    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES)
        if form.is_valid():
            myaccount.profile_image = form.cleaned_data['profile_image']  # Save Cloudinary file
            myaccount.save()
            messages.success(request, 'Your profile picture has been updated!')
            return redirect('myaccount:myaccount_home')
    else:
        form = ProfileImageForm()

    return render(request, 'myaccount/profile.html', {'myaccount': myaccount, 'form': form})



@login_required
def user_wishlist_view(request):
    myaccount, created = MyAccount.objects.get_or_create(user=request.user)
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    return render(request, 'wishlist/wishlist.html', {'myaccount': myaccount, 'wishlist_items': wishlist_items})