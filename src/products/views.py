from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Product
from .forms import ProductForm  # , RawProductForm


# FUNCTION BASED VIEWS != class based views (cf. blog.views)

def product_list_view(req):
    my_queryset = Product.objects.all()  # list of objects
    my_context = {"objects_list": my_queryset}
    return render(req, "products/product_list.html", my_context)


def product_delete_view(req, id):
    obj = get_object_or_404(Product, id=id)
    # this view is first rendered with a GET

    # when the form is submitted, it's with a POST :
    if req.method == "POST":
        obj.delete()
        return redirect("../")
    my_context = {"object": obj}
    return render(req, "products/product_delete.html", my_context)


def dynamic_lookup_view(request, id):
    # obj = Product.objects.get(id=id)

    # If the obj cannot be found => display an error 404 :
    # obj = get_object_or_404(Product, id=id)

    # Other method => raise an exception with the error 404 :
    try:
        obj = Product.objects.get(id=id)
    except Product.DoesNotExist:
        raise Http404

    context = {"object": obj}

    return render(request, "products/product_detail.html", context)


def product_create_view(request, *args, **kwargs):
    initial_data = {
        "title": "My valid title yo !"
    }  # this is not a placeholder but a value
    form = ProductForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        form = (
            ProductForm()
        )  # render an empty form after saving (to clean the fields)

    context = {
        "form": form,
    }
    return render(request, "products/product_create.html", context)


# def product_create_view(request, *args, **kwargs):
#     my_form = RawProductForm()  # if method = "GET" (=> default behavior)
#     if request.method == "POST":
#         my_form = RawProductForm(request.POST)
#         print(dir(my_form))
#         if my_form.is_valid():
#             print(my_form.cleaned_data)
#             Product.objects.create(**my_form.cleaned_data)
#         else:
#             print(my_form.errors)
#     context = {"form": my_form}
#     return render(request, "products/product_create.html", context)


# def product_create_view(request, *args, **kwargs):
#     # this is a bad method to save data !
#     if request.method == 'POST' :
#         my_new_title = request.POST.get('title')
#         print('my_new_title =====' , my_new_title)
#     context = {}
#     return render(request, "products/product_create.html", context)


def product_detail_view(request, *args, **kwargs):
    obj = Product.objects.get(id=1)
    # context = {
    #     'title': obj.title,
    #     'description': obj.description'
    # }
    print(obj)
    context = {
        "object": obj,
    }
    return render(request, "products/product_detail.html", context)
