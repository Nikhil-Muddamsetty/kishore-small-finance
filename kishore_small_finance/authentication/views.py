from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.messages import get_messages
from django.http import JsonResponse

class IndexClassView(TemplateView):
    template_name = 'authentication/index.html'


def send_messages(request):
    print("sending message")
    all_messages = get_messages(request)
    list_data = []
    for message in all_messages:
        dict = {}
        dict["tag"] = message.tags
        dict["msg"] = message.message
        list_data.append(dict)
    print(list_data)
    return JsonResponse(list_data, safe=False)



#----------------------------------------

# storage = get_messages(request)
# for message in storage:
#     do_something_with_the_message(message)
