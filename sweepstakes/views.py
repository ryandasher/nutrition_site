from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

from .models import Drawing, Prize, Points, Winner

from random import randint

@login_required
def user_home(request):
    user = request.user
    context = {}
    if request.method == 'POST':
        if request.META['QUERY_STRING'] == 'points':
            points = randint(1,5)
            # Try to add points first, otherwise add a new points object.
            try:
                points_obj = Points.objects.get(user_id=user.id)
                points_obj.value += points
            except ObjectDoesNotExist:
                # Can we assume the latest drawing is the active one?
                drawing = Drawing.objects.latest('date_created')
                points_obj = Points(value=points, user_id=user.id, drawing_id=drawing.id)
            points_obj.save()
            context['points_msg'] = "You earned %s points!" % points
        elif request.META['QUERY_STRING'] == 'winner':
            # When the prize is claimed, remove from the winner table.
            Winner.objects.filter(winner_id=user.id).delete()
            context['claimed'] = "Congrats! You have claimed your prize!"

    try:
        winner_obj = Winner.objects.get(winner_id=user.id)
        context['winner'] = "You have won $%d!" % winner_obj.value
    except ObjectDoesNotExist:
        pass

    return render(request, 'user_home.html', context)
