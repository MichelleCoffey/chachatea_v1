from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def posts(request):
    """
    A view for the blog page
        Args:
            request
        Returns:
            renders blog page template
    """

    posts = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(posts, 4)  # Maximum 4 posts on each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'blog_page': 'active',
        'page': page,
        'posts': posts,
    }
    return render(request, 'blog/blogs.html', context)
