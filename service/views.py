from django.shortcuts import render
from datetime import date, timedelta
from .models import Appointment, Master
from collections import OrderedDict


def get_available_slots():
    existing_appointments = Appointment.objects.all()
    available_slots = OrderedDict()
    current_date = date.today()
    while True:
        appointments_on_date = existing_appointments.filter(appointment_date=current_date)
        if not appointments_on_date:
            available_slots[current_date] = []

        all_time_slots = [choice[0] for choice in Appointment.TIME_CHOICES]

        available_slots[current_date] = [
            f"{time_slot}, {current_date}, {', '.join(Master.objects.exclude(appointments__appointment_date=current_date, appointments__appointment_time=time_slot).values_list('name', flat=True))}"
            for time_slot in all_time_slots
        ]
        available_slots[current_date].sort()
        current_date = current_date + timedelta(days=1)
        if len(available_slots) == 7:
            break
    return available_slots


def available_dates(request):
    available_slots = get_available_slots()
    return render(request, 'available_dates.html', {'available_slots': available_slots})
