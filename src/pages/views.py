from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print(request.user)
    return render(request, "home.html", {})

def contact_view(req, *args, **kwargs):
    # print("ARGS ===", args)
    # print("KWARGS ===", kwargs)
    # return HttpResponse("<h1>Contact page</h1>")
    return render(req, 'contact.html', {})

def about_view(req, *args, **kwargs):
    my_context = {
        "my_title" : "<h1>This is a title !</h1>",
        "my_text" : "This is about us",
        "my_number" : 12345,
        "my_list" : ["patate", "pain", "20 kg de riz", 67, 890],
        "my_true_bool" : True
    }
    return render(req,'about.html', my_context)