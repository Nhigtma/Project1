from django.shortcuts import render, redirect, get_object_or_404
from .models import people
from .forms import peopleForm

def peopleList(request):
    peopleL = people.objects.all()
    print(peopleL)
    return render(request, "peopleList.html", {"people": peopleL})
def personDetail(request, cc):
    person = get_object_or_404(people, cc=cc)
    return render(request, 'personDetail.html', {'person': person})
def peopleCreate(request):
    if request.method == 'POST':
        form = peopleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('peopleList')
    else:
        form = peopleForm()
    return render(request, 'peopleForm.html', {'form': form})
def personUpdate(request, cc):
    person = people.objects.get(cc=cc)
    if request.method == 'POST':
        form = peopleForm(request.UPDATE, instance=person)
        if form.is_valid():
            form.save()
            return redirect('personDetail', cc=cc)
    else:
        form = peopleForm(instance=person)
    return render(request, 'peopleForm.html', {'form': form})
def personDelete(request, cc):
    try:
        person = get_object_or_404(people, cc=cc)
        if request.method == 'POST':
            person.delete()
            return redirect('peopleList')
        return render(request, 'personConfirmDelete.html', {'person': person})
    except Exception as e:
        print(f"Error: {e}")
        raise