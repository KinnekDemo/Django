from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from fix_it.forms import NewPost
from fix_it.models import Post, Annotate


def front(request):
    posts = Post.objects.all()
    comments = Annotate.objects.all()
    data = {
        'posts': posts,
        'comments': comments,
    }

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
    return render(request, 'profile.html')


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
    posts = Post.objects.all()

    data = {
        'posts': posts
    }

    return render(request, 'view_posts.html', data)


def up_vote(request, comment_id):
    # comments = Post.objects.filter(comments__id=comment_id)
    comment = Annotate.objects.get(id=comment_id)
    comment.vote_count += 1
    comment.voted = True
    comment.save()
    # data = {
    #     'comments': comments
    # }
    return render(request, 'home.html')


