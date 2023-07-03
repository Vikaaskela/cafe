from django.shortcuts import render, redirect
from .models import DishCategory, Dish
from .forms import BookingForm
from .forms import ContactForm


def main_page(request):
    if request.method == 'POST':
        booking_form = BookingForm(request.POST)
        if booking_form.is_valid():
            booking_form.save()
            return redirect('/')


    categories = DishCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True, is_special=False)
    special_dishes = Dish.objects.filter(is_visible=True, is_special=True)
    booking_form = BookingForm()
    contact_form = ContactForm()
    return render(request, 
                    'main.html', 
                    context={
                      'categories' : categories,
                      'dishes' : dishes,
                      'special_dishes' : special_dishes,
                      'booking_form' : booking_form,
                      'contact_form' : contact_form,
                    })