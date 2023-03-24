from apps.products.models import Category


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    @classmethod
    def get_instance(cls):
        if isinstance(cls._instance, cls):
            return cls._instance


class CachedCategories(Singleton):
    def __init__(self, queryset=None):
        self.queryset = queryset

    def get_children(self, parent: Category):
        children = list(obj for obj in self.queryset if obj.path.startswith(parent.path)
                        and obj.depth == parent.depth + 1)
        return children

    def get_cached_root_nodes(self):
        return list(obj for obj in self.queryset if obj.depth == 1)
