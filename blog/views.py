# from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

# all_posts = [
#  Dummy Data   
# ]

# # Helper method
# def get_date(post):
#     return post['date']

def starting_page(request):
    # using dummy data
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    # return render(request, "blog/index.html", {
    #     "posts": latest_posts
    # })

    # using db data
    latest_posts = Post.objects.all().order_by("-date")[:3] # this line creates a sql query, doesnt use python to do this...no performance hit of loading all records then slicing 3
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post,
        "post_tags": identified_post.tags.all()
    })