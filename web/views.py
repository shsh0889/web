from django.shortcuts import render

def post_list(request):
    return render(request, 'web/post_list.html', {})
