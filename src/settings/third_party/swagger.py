from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

SWAGGER_SETTINGS = {
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header',
            'description': 'JWT Authorization header using the Bearer scheme. Example: "Bearer {token}"',
        }
    },
    'USE_SESSION_AUTH': False,
}

schema_view = get_schema_view(
    openapi.Info(
        title="Comments API",
        default_version='v1',
        description="API documentation for the Comments project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@comments.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
