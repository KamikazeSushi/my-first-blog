from django.shortcuts import render

def post_request(request):
    return render(request, 'blog/post_list.html', {})