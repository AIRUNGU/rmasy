from django.shortcuts import render
from django.utils.safestring import mark_safe
import json

def Prohome(request):
    return render(request,'welcome.html',{})


def Proreporter(request, code):
    return render(request, 'room.html', {
        'room_name_json': mark_safe(json.dumps(code))
})
