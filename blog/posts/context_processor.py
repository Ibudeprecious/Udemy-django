def categories (request):
    categories = [
        'Read a Book',
        'Learn a skill',
        'Track your time',
        'Track your money'
    ]
    return {'categories': categories}
