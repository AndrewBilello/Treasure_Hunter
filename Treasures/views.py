from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from Accounts.models import User
from .models import Treasure, Post, Comment, Hint

def new_treasure(request):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'this_user': User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'new_treasure.html', context)

def create_treasure(request):
    if request.method != "POST":
        return redirect('/dashboard')
    errors = Treasure.objects.treasure_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/treasure/new_treasure')
    user = User.objects.get(id=request.session['user_id'])
    print(request.POST)
    print(request.FILES)
    Treasure.objects.create(
        name = request.POST['name'],
        description = request.POST['description'],
        location = request.POST['location'],
        image = request.FILES['image'],
        map_url = request.POST['map_url'],
        created_by = user
    )
    return redirect('/dashboard')

def delete_treasure(request, treasure_id):
    treasure = Treasure.objects.get(id=treasure_id)
    treasure.delete()
    return redirect('/dashboard')

def treasure_info(request, treasure_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'this_user': User.objects.get(id = request.session['user_id']),
        'this_treasure': Treasure.objects.get(id=treasure_id)
    }
    return render(request, 'treasure_info.html', context)

def edit_treasure(request, treasure_id):
    if 'user_id' not in request.session:
        return redirect('/')

    context = {
        'this_user': User.objects.get(id = request.session['user_id']),
        'this_treasure': Treasure.objects.get(id=treasure_id)
    }
    return render(request, 'edit_treasure.html', context)

def update_treasure(request, treasure_id):
    if request.method != "POST":
        return redirect('/dashboard')
    errors = Treasure.objects.treasure_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/treasure/{treasure_id}/edit_treasure")
    treasure = Treasure.objects.get(id=treasure_id)
    treasure.name = request.POST['name']
    treasure.description = request.POST['description']
    treasure.location = request.POST['location']
    treasure.image = request.FILES['image']
    treasure.map_url = request.POST['map_url']
    treasure.save()
    return redirect('/dashboard')

def create_post(request, treasure_id):
    if request.method =="POST":
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            treasure = Treasure.objects.get(id=treasure_id)
            Post.objects.create(content=request.POST["post_content"], creator=user, treasure=treasure)
    return redirect(f'/treasure/{treasure_id}')

def delete_post(request, treasure_id, post_id):
    if 'user_id' not in request.session:
        return redirect('/')

    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect(f'/treasure/{treasure_id}')

def create_comment(request, treasure_id, post_id):
    if request.method =="POST":
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            wall_post = Post.objects.get(id = post_id)
            Comment.objects.create(content=request.POST["create_comment"], creator=user,
            post=wall_post)
    return redirect(f'/treasure/{treasure_id}')

def delete_comment(request, treasure_id, post_id, comment_id):
    if 'user_id' not in request.session:
        return redirect('/')

    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect(f'/treasure/{treasure_id}')

def create_hint(request, treasure_id):
    if request.method =="POST":
        if 'user_id' in request.session:
            user = User.objects.get(id=request.session['user_id'])
            treasure = Treasure.objects.get(id=treasure_id)
            Hint.objects.create(content=request.POST["hint_content"], creator=user, treasure=treasure)
    return redirect(f'/treasure/{treasure_id}')

def delete_hint(request, treasure_id, hint_id):
    if 'user_id' not in request.session:
        return redirect('/')

    hint = Hint.objects.get(id=hint_id)
    hint.delete()
    return redirect(f'/treasure/{treasure_id}')