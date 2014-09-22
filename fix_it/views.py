from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import render, redirect
from fix_it.forms import NewPost, NewComment
from fix_it.models import Post, Annotate
import folium
from geopy.geocoders import Nominatim


def front(request):
    posts = Post.objects.all()
    certain_post = Post.objects.get(id=1)
    comments = Annotate.objects.all()
    data = {
        'posts': posts,
        'comments': comments,
    }
    # Trying out folium
    geolocator = Nominatim()
    # for post in posts:
    #     location = geolocator.geocode(post.location)
    #     map_osm = folium.Map(location=[45.5236, -122.6750])
    #     map_osm.simple_marker([location.latitude], [location.longitude], popup=post.title)
    #     map_osm.create_map(path='testmap.html')

    location = geolocator.geocode(certain_post.location)
    map_osm = folium.Map(location=[45.5236, -122.6750])
    map_osm.simple_marker([location.latitude, location.longitude], popup='Test time!')
    map_osm.create_map(path='testmap.html')

    return render(request, 'home.html', data)


# @login_required
def new_post(request):
    data = {'new_post': NewPost()}
    if request.method == "POST":
        form = NewPost(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            Post.objects.create(author=user, body=form.cleaned_data['body'], image=form.cleaned_data['image'])
    else:
        return render(request, 'new_post.html', data)

    # Change this to a 'Thanks for posting' screen
    return render(request, 'home.html', data)


def profile(request):
    data = {
        'posts': Post.objects.filter(author=request.user)
    }
    return render(request, 'profile.html', data)


def new_comment(request, post_id):
    # Attach the comment to the clicked post
    post = Post.objects.get(id=post_id)
    data = {
        'new_comment': NewComment(),
        'post': post
    }

    if request.method == "POST":
        form = NewComment(request.POST)
        if form.is_valid():
            Annotate.objects.create(post=post, comment=form.cleaned_data['comment'],
                                    author=request.user)
            return redirect('/')

    else:
        return render(request, 'new_comment.html', data)
    return redirect(request, 'new_comment.html', data)


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {
        'form': form
    })


def view_posts(request):
    data = {
        'posts': Post.objects.all()
    }

    return render(request, 'view_posts.html', data)


def down_vote(request, comment_id):
    comment = Annotate.objects.get(id=comment_id)
    comment.thumb_up = False
    comment.thumb_down = True
    comment.down_votes += 1
    comment.voted = True
    comment.save()
    # data = {
    #     'comments': comments
    # }
    return redirect('/')


def up_vote(request, comment_id):
    comment = Annotate.objects.get(id=comment_id)
    comment.thumb_down = False
    comment.thumb_up = True
    comment.up_votes += 1
    comment.voted = True
    comment.save()
    # data = {
    #     'comments': comments
    # }
    return redirect('/')


def leaderboard(request):
    # Users with the most posts (i.e. the most helped)
    users_with_most_posts = User.objects.annotate(num_posts=Count('posts')).order_by('-num_posts')[:5]
    users_with_most_comments = Post.objects.annotate(most_comms=Count('author')).order_by('-most_comms')[:5]
    most_comments = Annotate.objects.annotate(most_comms=Count('author')).order_by('-most_comms')[:5]

    data = {
        'users_with_most_posts': users_with_most_posts,
        'users_with_most_comments': users_with_most_comments,
        'most_comments': most_comments,


    }
    return render(request, 'leaderboard.html', data)



