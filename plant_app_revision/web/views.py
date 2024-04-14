from django.shortcuts import render, redirect
from plant_app_revision.web.forms import ProfileCreateForm, PlantCreateForm, PlantEditForm, PlantDeleteForm, \
    ProfileEditForm, ProfileDeleteForm
from plant_app_revision.web.models import Profile, Plant


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    context = {
        'has_profile': has_profile,
    }
    return render(request, 'home-page.html', context)


def profile_create(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True

    if get_profile() is not None:
        return redirect('index')
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'create-profile.html', context)


def catalogue(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    if profile is None:
        return profile_create(request)

    context = {
        'plants': Plant.objects.all(),
        'has_profile': has_profile,
    }
    return render(request, 'catalogue.html', context)


def plant_create(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    if request.method == 'POST':
        form = PlantCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantCreateForm()

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    plant = Plant.objects.filter(pk=pk).get()
    context = {
        'plant': plant,
        'has_profile': has_profile,
    }
    return render(request, 'plant-details.html', context)


def plant_edit(request, pk):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlantEditForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantEditForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'has_profile': has_profile,
    }
    return render(request, 'edit-plant.html', context)


def plant_delete(request, pk):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    plant = Plant.objects.get(pk=pk)
    if request.method == 'POST':
        form = PlantDeleteForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = PlantDeleteForm(instance=plant)

    context = {
        'form': form,
        'plant': plant,
        'has_profile': has_profile,
    }
    return render(request, 'delete-plant.html', context)


def profile_details(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True
    plants_count = Plant.objects.count()
    context = {
        'profile': profile,
        'plants_count': plants_count,
        'has_profile': has_profile,
    }
    return render(request, 'profile-details.html', context)


def profile_edit(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True

    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if profile is None:
        has_profile = False
    else:
        has_profile = True

    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form': form,
        'has_profile': has_profile,
    }
    return render(request, 'delete-profile.html', context)