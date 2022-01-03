# from datetime import date
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView, DetailView

# Create your views here.

# all_posts = [
#  Dummy Data   
# ]

# # Helper method
# def get_date(post):
#     return post['date']

class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"
    
    # Need to modify slice and order
    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data
    

# Converting to Class-based View
# def starting_page(request):
    # using dummy data
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:]
    # return render(request, "blog/index.html", {
    #     "posts": latest_posts
    # })

    # using db data
    # latest_posts = Post.objects.all().order_by("-date")[:3] # this line creates a sql query, doesnt use python to do this...no performance hit of loading all records then slicing 3
    # return render(request, "blog/index.html", {
    #     "posts": latest_posts
    # })

class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "all_posts"

# def posts(request):
#     all_posts = Post.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#         "all_posts": all_posts
#     })

class SinglePostView(DetailView):
    template_name = "blog/post-detail.html"
    model = Post
    # Detail View by defaul looks for slug (from urls page)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_tags"] = self.object.tags.all()
        return context

# def post_detail(request, slug):
#     # identified_post = next(post for post in all_posts if post['slug'] == slug)
#     identified_post = get_object_or_404(Post, slug=slug)
#     return render(request, "blog/post-detail.html", {
#         "post": identified_post,
#         "post_tags": identified_post.tags.all()
#     })