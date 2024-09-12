from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteCreateForm
from .models import Note

# Create your views here.

def note_list(request):
    notes = Note.objects.all()
    return render(request, "note_list.html", {"notes": notes})

@login_required(login_url = "/users/login")
def note_create(request):
    if request.method == "POST":
        form = NoteCreateForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            messages.success(request, "the note create successfully")
            return redirect("/")
    else:
        form = NoteCreateForm()
    return render(request, "note_create", {"form": form})


@login_required(login_url = "/users/login")
def render_html(request, slug):
    note = get_object_or_404(Note, slug=slug)
    if note.owner == request.user:
        return render(request, "note_detail.html", {"note": note})
    messages.error(request, "you have to be the owner of the note")
    return redirect("note_list")
