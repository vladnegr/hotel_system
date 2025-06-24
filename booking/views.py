from django.shortcuts import render
from booking.models import TypeRoom, Booking, Room


def main_page(request):
    rooms = Room.objects.all()

    context ={
        'room_list': rooms
    }
    return render(request, 'booking/room_list.html', context)