from django.contrib import admin

from .models import Drawing, Prize, Points, Winner

from random import randint

class DrawingAdmin(admin.ModelAdmin):
    actions = ['run_drawing']

    def run_drawing(self, request, queryset):
        # TODO: Hack, but running out of time. Only will work on first item
        # of queryset. In reality we want this button elsewhere in the admin.
        chance_list = []
        for p in Points.objects.all():
            chance_list.extend([p.user_id] * p.value)

        prize_values = []
        # We want to dole out the highest value prizes first.
        for prize in Prize.objects.filter(drawing_id=queryset[0].id).order_by('-value'):
            prize_values.extend([prize.value] * prize.count)

        # Users with the most points have the highest chance of attaining higher
        # value prizes.
        for prize_value in prize_values:
            if len(chance_list) == 0:
                break
            choice = randint(0, len(chance_list) - 1)
            user_id = chance_list[choice]
            winner = Winner(winner_id=user_id, value=prize_value)
            winner.save()
            chance_list = [x for x in chance_list if x != user_id]

        Drawing.objects.filter(id=queryset[0].id).delete()
    run_drawing.short_description = "Run the latest drawing"


admin.site.register(Drawing, DrawingAdmin)
admin.site.register(Prize)
