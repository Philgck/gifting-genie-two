from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Friendship
from .forms import AddFriendForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required


def search_usernames(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        query = request.GET.get('term', '')
        users = User.objects.filter(username__icontains=query)
        results = [user.username for user in users]
        return JsonResponse(results, safe=False)
    return JsonResponse([], safe=False)


@login_required
def friendship_list(request, user_id):
    user = get_object_or_404(User, id=user_id)
    friendships = Friendship.objects.filter(user=user, confirmed=True)
    return render(request, 'friendslist/friendslist.html', {'friendships': friendships, 'user': user})

@login_required
def confirm_friendship(request, user_id, friendship_id):
    user = get_object_or_404(User, id=user_id)
    friendship = get_object_or_404(Friendship, id=friendship_id, friend=user)
    if request.method == 'POST':
        friendship.confirmed = True
        friendship.save()
        return redirect('friendslist:friendslist', user_id=user.id)
    return render(request, 'friendslist/confirm_friendship.html', {'friendship': friendship, 'user': user})
# @login_required
# def friendship_list(request):
#     if request.user.is_authenticated:
#         friendships = Friendship.objects.filter(
#             user=request.user, confirmed=True
#             )
#         return render(
#             request,
#             'friendslist/friendslist.html',
#             {'friendships': friendships}
#             )
#     else:
#         return redirect('account_login')


# class FriendshipListView(ListView):
#     model = Friendship
#     template_name = 'friendslist/friendslist.html'
#     context_object_name = 'friendships'

#     def get_queryset(self):
#         return Friendship.objects.filter(
#             user=self.request.user, confirmed=True
#             )


# def confirm_friendship(request, friendship_id):
#     friendship = get_object_or_404(
#         Friendship, id=friendship_id, friend=request.user
#         )
#     if request.method == 'POST':
#         friendship.confirmed = True
#         friendship.save()
#         return HttpResponseRedirect(reverse('friendslist'))
