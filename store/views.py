from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages

from .models import Medicine
from .forms import MedicineForm, SignUpForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Signup successful. Please log in.")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'store/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pwd = request.POST.get('password')

        if not uname or not pwd:
            messages.error(request, "Both username and password are required.")
            return render(request, 'store/login.html')

        user = authenticate(request, username=uname, password=pwd)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome, {user.username}!")
            return redirect('medicine_list')
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'store/login.html')

    return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return redirect('login')

@login_required(login_url='/login/')
def medicine_list(request):
    search_query = request.GET.get('q', '')
    medicines = Medicine.objects.filter(user=request.user)
    if search_query:
        medicines = medicines.filter(name__icontains=search_query)
    paginator = Paginator(medicines.order_by('-added_at'), 5)
    page = request.GET.get('page')
    medicines = paginator.get_page(page)
    return render(request, 'store/medicine_list.html', {
        'medicines': medicines,
        'query': search_query
    })

@login_required(login_url='/login/')
def add_medicine(request):
    if Medicine.objects.filter(user=request.user).count() >= 5:
        return render(request, 'store/error.html', {
            'message': 'You can only add up to 5 medicines.'
        })
    if request.method == 'POST':
        form = MedicineForm(request.POST)
        if form.is_valid():
            medicine = form.save(commit=False)
            medicine.user = request.user
            medicine.save()
            messages.success(request, "Medicine added successfully.")
            return redirect('medicine_list')
    else:
        form = MedicineForm()
    return render(request, 'store/add_medicine.html', {'form': form})

@login_required(login_url='/login/')
def edit_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk, user=request.user)
    if request.method == 'POST':
        form = MedicineForm(request.POST, instance=medicine)
        if form.is_valid():
            form.save()
            messages.success(request, "Medicine updated successfully.")
            return redirect('medicine_list')
    else:
        form = MedicineForm(instance=medicine)
    return render(request, 'store/edit_medicine.html', {'form': form})

@login_required(login_url='/login/')
def delete_medicine(request, pk):
    medicine = get_object_or_404(Medicine, pk=pk, user=request.user)
    medicine.delete()
    messages.success(request, "Medicine deleted successfully.")
    return redirect('medicine_list')
