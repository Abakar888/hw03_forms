from django.core.paginator import Paginator


def paginator(queryset, elems, request):
    paginator = Paginator(queryset, elems)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
