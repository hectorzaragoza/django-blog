from datetime import date
from django.shortcuts import render

# Create your views here.

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "glacier.jpeg",
        "author": "Hector",
        "date": date(2021,7,21),
        "title": "Mountain Biking",
        "excerpt": "There's nothing like the rush and peace of a flow trail.",
        "content": """
            This is a multi-Line String
            Easier to write and read
            :)
        """ 
    },
    {
        "slug": "some-picture",
        "image": "2019-02-13.png",
        "author": "Hector",
        "date": date(2021,7,21),
        "title": "Climbing",
        "excerpt": "There's nothing like the rush and peace of a flow trail.",
        "content": """
            This is a multi-Line String
            Easier to write and read
            :)
        """ 
    },
    {
        "slug": "some-picture",
        "image": "propic.jpg",
        "author": "Hector",
        "date": date(2021,7,21),
        "title": "Climbing",
        "excerpt": "There's nothing like the rush and peace of a flow trail.",
        "content": """
            This is a multi-Line String
            Easier to write and read
            :)
        """ 
    }
]

# Helper method
def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts": latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts": all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post": identified_post
    })