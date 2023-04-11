from django.core.paginator import Paginator


def paginator(queryset, elems, request):
    paginator = Paginator(queryset, elems)
    page_number = request.GET.get('page')
    return paginator.get_page(page_number)
