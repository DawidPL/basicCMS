from .repository.models_repository import ModelsRepository

def common_context(request):
    main_info = {
        'page_url': 'http://127.0.0.1:8000',
        'page_name': 'Twoja strona',
    }
    return main_info

def nav_tree_generator(request):
    models_repository = ModelsRepository()
    subpages = models_repository.get_active_subpages()
    parents = {}

    for subpage in subpages:
        if subpage.parent:
            if subpage.parent not in parents:
                parents[subpage.parent] = []
            parents[subpage.parent].append(subpage)
        else:
            parents.setdefault(subpage,[])
    return {'parents':parents,}
