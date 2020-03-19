from ..repository.models_repository import ModelsRepository
from collections.abc import Iterable


def no_parametr_view():
    return None


def iter_single_blog_post():
    posts = get_iterable_or_none(ModelsRepository().get_all_blog_posts())
    if posts:
        for post in posts:
            yield {'slug': post.slug}
    else:
        return None


def iter_single_subpage():
    subpages = get_iterable_or_none(ModelsRepository().get_all_subpages())
    if subpages:
        for subpage in subpages:
            yield {'slug': subpage.slug}
    else:
        return None


def get_iterable_or_none(model_instances):
    if model_instances:
        if isinstance(model_instances, Iterable):
            return model_instances
        else:
            return [model_instances]
    else:
        return None
