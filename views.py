from django.shortcuts import render
from chat.models import ChatModel
# Create your views here.

def homepage(request):
    return render(request,'index.html')

def roomview(request):
    if request.method == 'POST':
        room_no = request.POST['room_no']
        name = request.POST['name']
        messages = []
        for eachObj in ChatModel.objects.filter(room_no=room_no):
            messages.append(eachObj.message)
        context = {
            'room_no': room_no,
            'name': name,
            'messages': messages
        }
    return render(request,'room.html',context)
   