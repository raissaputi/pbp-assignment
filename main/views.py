from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Item x',
        'amount': '999',
        'description': 'XOX'
    }

    return render(request, "main.html", context)
