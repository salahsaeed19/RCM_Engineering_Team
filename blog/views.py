from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Category, Comment
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.contrib import messages
from collections import Counter
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.all().order_by('-publish_date')
    categories = Category.objects.all()
    query = request.GET.get("q")
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)
        ).distinct()

    recent_posts = Post.objects.order_by('-created_at')[:4]
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = [post.category for post in posts]
    category_counts = dict(Counter(categories))
    context = {
        'postss': page_obj,
        'recent_posts': recent_posts,
        # 'posts': posts,
        'categories': categories, 
        'category_counts': category_counts
        }
    return render(request, 'blog/post_list.html', context)


@login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = Comment.objects.filter(post_id=post_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.user_id = request.user
            new_comment.post_id = post
            new_comment.save()
            return redirect('post_detail', post_id=post_id)
    else:
        comment_form = CommentForm()
    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/post_detail.html', context)


@login_required
def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('post_detail', post_id=new_post.pk)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'blog/add_post.html', context)


def search_posts(request):
    # Handle search functionality
    query = request.GET.get('q')
    if query:
        # Use Q objects to perform a case-insensitive search on post titles
        posts = Post.objects.filter(Q(title__icontains=query))
    else:
        posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'postss': posts})


def filter_posts_by_category(request, category_id):
    # Filter posts by category
    category = get_object_or_404(Category, pk=category_id)
    posts = Post.objects.filter(category=category)
    return render(request, 'blog/post_list.html', {'postss': posts})


@login_required
def add_comment(request, post_id):
    # Handle the form submission for adding a comment
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # Create a new comment
            comment = form.save(commit=False)
            comment.user_id = request.user  # Assuming you have user authentication
            comment.post_id_id = post_id
            comment.save()
            messages.success(request, 'Comment added successfully.')
            return redirect('post_detail', post_id=post_id)
        else:
            messages.error(request, 'Error adding comment. Please check the form.')

    # If it's not a POST request or the form is invalid, render the post detail page
    # with the comment form
    return redirect('post_detail', post_id=post_id)