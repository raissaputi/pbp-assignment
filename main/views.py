from django.shortcuts import render

def show_main(request):
    context = {
        'nama_aplikasi': "My Bag",
        'nama': "Puti Raissa",
        'kelas': "PBP E"
    }

    return render(request, "main.html", context)
