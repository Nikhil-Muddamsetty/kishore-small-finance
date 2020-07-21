from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.messages import get_messages
from django.http import JsonResponse

class IndexClassView(TemplateView):
    template_name = 'authentication/index.html'


def send_messages(request):
    if request.GET:
            print("reached into functio1")
    print("reached into functio")

    all_messages = get_messages(request)
    dict_data = {}
    no_of_messages = 0;
    for message in all_messages:
        print(message.tags)
        no_of_messages += 1
        dict_data['tag'+str(no_of_messages)] = message.tags
        dict_data['msg'+str(no_of_messages)] = message.message
    dict_data['total_messages']=str(no_of_messages)
    data = dict_data
    print(data)
    #data = {'hello':'hi'}
    return JsonResponse(data, safe=True)



#----------------------------------------

# storage = get_messages(request)
# for message in storage:
#     do_something_with_the_message(message)
