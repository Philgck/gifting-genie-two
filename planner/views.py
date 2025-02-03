from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Planner
from .forms import PlannerForm
from django.contrib.auth.models import User
from django.contrib import messages


# @login_required
# def calendar_view(request, user_id):
#     """
#     View to display the calendar with the user's events and their friends' events.

#     Description:
#         This view fetches the events for the logged-in user and their friends and displays them in a calendar format.

#     Context:
#         - events: A queryset of the user's events.
#         - friends_events: A queryset of the user's friends' events.
#         - user: The user whose calendar is being viewed.

#     Template:
#         - planner/calendar.html: The template for rendering the calendar view with the events.
#     """
    # user = get_object_or_404(User, id=user_id)
    # events = Planner.objects.filter(user=user)
    # friends = Friendship.objects.filter(user=user, confirmed=True)
    # friends_events = Planner.objects.filter(user__in=[friend.friend for friend in friends])
    # return render(request, 'planner/calendar.html', {'events': events, 'friends_events': friends_events, 'user': user})

@login_required
def planner_view(request):
    events = Planner.objects.filter(user=request.user)
    return render(request, 'planner/planner.html', {'events': events})

@login_required
def get_events(request):
    events = Planner.objects.filter(user=request.user)
    events_list = []
    for event in events:
        events_list.append({
            'title': event.event_name,
            'start': event.event_date.isoformat(),  # Start date
            'end': (event.event_date + timedelta(days=1)).isoformat(),  # End date (next day)
            'description': event.description,
        })
    return JsonResponse(events_list, safe=False)

# @login_required
# def add_event(request, user_id):
#     """
#     View to add a new event.

#     Description:
#         This view handles the creation of a new event for the logged-in user.

#     Context:
#         - form: A form instance for creating a new event.
#         - user: The user for whom the event is being created.

#     Template:
#         - planner/add_event.html: The template for rendering the form to add a new event.
#     """
#     user = get_object_or_404(User, id=user_id)
#     if request.method == 'POST':
#         form = PlannerForm(request.POST)
#         if form.is_valid():
#             event = form.save(commit=False)
#             event.user = user
#             event.save()
#             return redirect('planner:user_calendar', user_id=user.id)
#     else:
#         form = PlannerForm()
#     return render(request, 'planner/add_event.html', {'form': form, 'user': user})

@login_required
def add_event(request):
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            messages.success(request, 'Event added successfully!')
            return redirect('planner:planner_view')
    else:
        form = PlannerForm()
    return render(request, 'planner/add_plan.html', {'form': form})

# @login_required
# def edit_event(request, user_id, event_id):
#     """
#     View to edit an existing event.

#     Description:
#         This view handles the editing of an existing event for the logged-in user.

#     Context:
#         - form: A form instance for editing the event.
#         - user: The user who owns the event.
#         - event: The event instance being edited.

#     Template:
#         - planner/edit_event.html: The template for rendering the form to edit the event.
#     """
#     user = get_object_or_404(User, id=user_id)
#     event = get_object_or_404(Planner, id=event_id, user=user)
#     if request.method == 'POST':
#         form = PlannerForm(request.POST, instance=event)
#         if form.is_valid():
#             form.save()
#             return redirect('planner:user_calendar', user_id=user.id)
#     else:
#         form = PlannerForm(instance=event)
#     return render(request, 'planner/edit_event.html', {'form': form, 'user': user})

@login_required
def edit_event(request, event_id):
    event = get_object_or_404(Planner, id=event_id, user=request.user)
    if request.method == 'POST':
        form = PlannerForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully!')
            return redirect('planner:planner_view')
    else:
        form = PlannerForm(instance=event)
    return render(request, 'planner/edit_plan.html', {'form': form})

# @login_required
# def delete_event(request, user_id, event_id):
#     """
#     View to delete an existing event.

#     Description:
#         This view handles the deletion of an existing event for the logged-in user.

#     Context:
#         - event: The event instance to be deleted.
#         - user: The user who owns the event.

#     Template:
#         - planner/delete_event.html: The template for rendering the confirmation for deleting the event.
#     """
#     user = get_object_or_404(User, id=user_id)
#     event = get_object_or_404(Planner, id=event_id, user=user)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('planner:user_calendar', user_id=user.id)
#     return render(request, 'planner/delete_event.html', {'event': event, 'user': user})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Planner, id=event_id, user=request.user)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('planner:planner_view')
    return render(request, 'planner/delete_plan.html', {'event': event})