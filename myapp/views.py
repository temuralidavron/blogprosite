from django.shortcuts import render

from myapp.forms import BlogForm


def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'blog/create_blog.html',{'form':form})
    else:
        form=BlogForm()

        return render(request, 'blog/create_blog.html',{'form':form})