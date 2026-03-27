from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NoteForm
from .models import Note


def home(request):
    # Agar user logged-in hai to seedha uske notes page par bhej dein,
    # warna login page par redirect kar dein.
    if request.user.is_authenticated:
        return redirect("note_list")
    return redirect("login")


@login_required
def note_list(request):
    # Sirf current logged-in user ke notes ko list karna.
    notes = Note.objects.filter(owner=request.user).order_by("-updated_at", "-created_at")
    return render(request, "note_list.html", {"notes": notes})


@login_required
def note_create(request):
    # User ka naya note create karna aur usi user ko owner set karna.
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.owner = request.user
            note.save()
            return redirect("note_list")
    else:
        form = NoteForm()

    return render(request, "note_form.html", {"form": form, "mode": "create"})


@login_required
def note_edit(request, note_id: int):
    # Existing note ko edit karna, lekin sirf tab jab note current user ka ho.
    note = get_object_or_404(Note, pk=note_id, owner=request.user)

    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("note_list")
    else:
        form = NoteForm(instance=note)

    return render(request, "note_form.html", {"form": form, "note": note, "mode": "edit"})


@login_required
def note_delete(request, note_id: int):
    # Note delete karne se pehle confirmation dikhana, aur owner-only deletion ensure karna.
    note = get_object_or_404(Note, pk=note_id, owner=request.user)

    if request.method == "POST":
        note.delete()
        return redirect("note_list")

    return render(request, "note_confirm_delete.html", {"note": note})


def register_view(request):
    # Naye user ka registration handle karna (username/password create).
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "register.html", {"form": form})
