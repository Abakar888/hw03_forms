import datetime as dt

def year(request):
    year = dt.datetime.today().year
    """Добавляет переменную с текущим годом."""
    return {
        'year': year
    }