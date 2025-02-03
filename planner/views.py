from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Planner
from .forms import PlannerForm
from django.contrib.auth.models import User

@login_required
def planner_home(request, user_id):
    """
    View to display the planner home with the user's events.

    Description:
        This view fetches the events for the logged-in user and displays them in a list format.

    Context:
        - events: A queryset of the user's events.

    Template:
        - planner/home.html: The template for rendering the planner home view with the events.
    """
    user = get_object_or_404(User, id=user_id)
    events = Planner.objects.filter(user=user)
    return render(request, 'planner/home.html', {'events': events, 'user': user})

@login_required
def create_plan(request, user_id):
    """
    View to add a new event.

    Description:
        This view handles the creation of a new event for the logged-in user.

    Context:
        - form: A form instance for creating a new event.
        - user: The user for whom the event is being created.

    Template:
        - planner/create_plan.html: The template for rendering the form to add a new event.
    """
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        form = PlannerForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = user
            event.save()
            return redirect('planner:planner_home', user_id=user.id)
    else:
        form = PlannerForm()
    return render(request, 'planner/create_plan.html', {'form': form, 'user': user})

@login_required
def edit_plan(request, user_id, event_id):
    """
    View to edit an existing event.

    Description:
        This view handles the editing of an existing event for the logged-in user.

    Context:
        - form: A form instance for editing the event.
        - user: The user who owns the event.
        - event: The event instance being edited.

    Template:
        - planner/edit_plan.html: The template for rendering the form to edit the event.
    """
    user = get_object_or_404(User, id=user_id)
    event = get_object_or_404(Planner, id=event_id, user=user)
    if request.method == 'POST':
        form = PlannerForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('planner:planner_home', user_id=user.id)
    else:
        form = PlannerForm(instance=event)
    return render(request, 'planner/edit_plan.html', {'form': form, 'user': user})

@login_required
def delete_plan(request, user_id, event_id):
    """
    View to delete an existing event.

    Description:
        This view handles the deletion of an existing event for the logged-in user.

    Context:
        - event: The event instance to be deleted.
        - user: The user who owns the event.

    Template:
        - planner/delete_plan.html: The template for rendering the confirmation for deleting the event.
    """
    user = get_object_or_404(User, id=user_id)
    event = get_object_or_404(Planner, id=event_id, user=user)
    if request.method == 'POST':
        event.delete()
        return redirect('planner:planner_home', user_id=user.id)
    return render(request, 'planner/delete_plan.html', {'event': event, 'user': user})