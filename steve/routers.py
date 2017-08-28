from collections import OrderedDict
from rest_framework.response import Response
from rest_framework.reverse import NoReverseMatch, reverse
from rest_framework.routers import DefaultRouter
from rest_framework.views import APIView
from rest_framework_nested.routers import NestedSimpleRouter


class Router(DefaultRouter):
    include_root_view = True
    include_format_suffixes = False
    root_view_name = 'index'

    def get_api_root_view(self, api_urls=None):
        api_root_dict = {}
        for prefix, viewset, basename in self.registry:
            api_root_dict[prefix] = self.routes[0].name.format(basename=basename)
        api_root_dict = sorted(api_root_dict.items())

        class APIRootView(APIView):
            _ignore_model_permissions = True
            exclude_from_schema = True

            def get(self, request, *args, **kwargs):
                ret = OrderedDict()
                namespace = request.resolver_match.namespace
                for key, url_name in api_root_dict:
                    if namespace:
                        url_name = namespace + ':' + url_name
                    try:
                        ret[key] = reverse(
                            url_name,
                            args=args,
                            kwargs=kwargs,
                            request=request,
                            format=kwargs.get('format', None)
                        )
                    except NoReverseMatch:
                        continue

                return Response(ret)

        return APIRootView.as_view()


class NestedRouter(NestedSimpleRouter):
    pass
