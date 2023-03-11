from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def print_hello(request):

    return HttpResponse('Hello to print parameter')


#example localhost:port/print/query/?name=ahmad&id=2/
def print_querystring(request):
    name = request.GET['name']
    id = request.GET['id']
    query = name+id
    return HttpResponse(query)



#example localhost:port/print/order/burger
def print_parameter(request, dish):

    menu = {
        'burger' : 'patty and bun',
        'juice' : 'orange juics',
        'pasta' : 'pasta and sauce'
    }

    descirption = menu[dish]

    #return HttpResponse(descirption)
    return HttpResponse('You ordered'+ ' '+str(dish) + ' ' + 'which consists of ' +' ' + descirption)

