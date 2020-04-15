from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_extensions.etag.mixins import ETAGMixin


class CacheResponseAndETAGMixin(ETAGMixin, CacheResponseMixin):
    pass
