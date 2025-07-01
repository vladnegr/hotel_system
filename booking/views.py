from django.shortcuts import get_object_or_404, redirect, render
from booking.forms import BookingForm
from booking.models import TypeRoom, Booking, Room
from django.contrib.auth.decorators import login_required



def main_page(request):
    rooms = Room.objects.all()

    context ={
        'room_list': rooms
    }
    return render(request, 'booking/room_list.html', context)


@login_required
def booking_page(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            return redirect('main')

    context = {
        'room': room,
        'form': form
    }

    return render(request, 'booking/booking_page.html', context)