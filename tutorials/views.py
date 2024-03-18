from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Tutorials
from .forms import TutorialForm


def view_tutorials(request):
    """ A view that renders the tutorials page  """
    tutorials = Tutorials.objects.all()

    template = 'tutorials/tutorials.html'
    context = {
        'tutorials': tutorials,
    }

    return render(request, template, context)


@login_required
def add_tutorial(request):
    """ Add a new tutorial """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TutorialForm(request.POST)
        if form.is_valid():
            # create instance of form and modify YouTube url for the embed link
            tutorial_form = form.save(commit=False)
            youtube_url = tutorial_form.youtube_url
            tutorial_form.youtube_embed_url = youtube_url.replace(
                "watch?v=", "embed/")
            tutorial_form.save()
            messages.success(request, 'Successfully added tutorial!')
            return redirect(reverse('view_tutorials'))
        else:
            messages.error(
                request, 'Failed to add tutorial. '
                'Please ensure the form is valid.'
            )
    else:
        form = TutorialForm()

    template = 'tutorials/add_tutorial.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_tutorial(request, tutorial_id):
    """ edits a tutorial """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))

    tutorial = get_object_or_404(Tutorials, pk=tutorial_id)
    if request.method == 'POST':
        form = TutorialForm(request.POST, instance=tutorial)
        if form.is_valid():
            # create instance of form and modify YouTube url for the embed link
            tutorial_form = form.save(commit=False)
            youtube_url = tutorial_form.youtube_url
            tutorial_form.youtube_embed_url = youtube_url.replace(
                "watch?v=", "embed/")
            tutorial_form.save()
            messages.success(request, 'Successfully updated tutorial!')
            return redirect(reverse('view_tutorials'))
        else:
            messages.error(
                request, 'Failed to update tutorial. '
                'Please ensure the form is valid.'
            )
    else:
        form = TutorialForm(instance=tutorial)
        messages.info(
            request, f'You are editing the {tutorial.title} tutorial')

    template = 'tutorials/edit_tutorial.html'
    context = {
        'form': form,
        'tutorial': tutorial,
    }

    return render(request, template, context)


@login_required
def delete_tutorial(request, tutorial_id):
    """ Delete a tutorial """
    if not request.user.is_superuser:
        messages.error(request, 'Access denied. Invalid permissions.')
        return redirect(reverse('home'))

    tutorial = get_object_or_404(Tutorials, pk=tutorial_id)
    tutorial.delete()
    messages.success(request, 'Tutorial deleted!')
    return redirect(reverse('view_tutorials'))
