import django_filters as filters

from posts.models import Post


class PostFilter(filters.FilterSet):
    publisher = filters.CharFilter(method='filter_publisher')

    class Meta:
        model = Post
        fields = ('publisher',)

    def filter_publisher(self, queryset, _, value):
        return queryset.filter(publisher__user__first_name=value)
