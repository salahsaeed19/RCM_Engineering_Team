from django.shortcuts import render, get_object_or_404, redirect
from .models import EngineeringSummary
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


@login_required
def summary_list(request):
    summary = EngineeringSummary.objects.all()

    paginator = Paginator(summary, 12)
    page_number = request.GET.get('page')
    summaries = paginator.get_page(page_number)

    return render(request, 'engineering_summaries/summary_list.html', {'summaries': summaries})


@login_required
def search_summaries(request):
    query = request.GET.get('q', '')
    summaries = EngineeringSummary.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    ).distinct()
    
    paginator = Paginator(summaries, 12)
    page_number = request.GET.get('page')
    summaries = paginator.get_page(page_number)
    
    return render(request, 'engineering_summaries/summary_list.html', {
        'summaries': summaries,
        'query': query
    })


@login_required
def filter_summaries_by_category(request, category):

    summaries = EngineeringSummary.objects.filter(categories__name=category)
    
    paginator = Paginator(summaries, 12)
    page_number = request.GET.get('page')
    summaries = paginator.get_page(page_number)
    
    return render(request, 'engineering_summaries/summary_list.html', {'summaries': summaries})


@login_required
def increment_views_and_redirect(request, summary_id):
    summary = get_object_or_404(EngineeringSummary, id=summary_id)
    summary.views += 1
    summary.save()
    return HttpResponseRedirect(summary.source_link)


# @login_required
# def summary_detail(request, summary_id):
#     summary = get_object_or_404(EngineeringSummary, pk=summary_id)

#     session_key = 'view_summary_{}'.format(summary.pk)
#     if not request.session.get(session_key, False):
#         summary.views += 1
#         summary.save()
#         request.session[session_key] = True

#     return render(request, 'engineering_summaries/summary_detail.html', {'summary': summary})


# @login_required
# def add_summary(request):
#     if request.method == 'POST':
#         form = EngineeringSummaryForm(request.POST, request.FILES)
#         if form.is_valid():
#             summary = form.save(commit=False)
#             summary.author = request.user
#             summary.save()
#             return redirect('summary_detail', summary_id=summary.id)
#     else:
#         form = EngineeringSummaryForm()
#     return render(request, 'engineering_summaries/add_summary.html', {'form': form})


# @login_required
# def edit_summary(request, summary_id):
#     summary = get_object_or_404(EngineeringSummary, pk=summary_id)
#     if request.method == 'POST':
#         form = EngineeringSummaryForm(request.POST, request.FILES, instance=summary)
#         if form.is_valid():
#             form.save()
#             return redirect('summary_detail', summary_id=summary.id)
#     else:
#         form = EngineeringSummaryForm(instance=summary)
#     return render(request, 'engineering_summaries/edit_summary.html', {'form': form, 'summary': summary})