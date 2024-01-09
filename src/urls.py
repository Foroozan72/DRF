from django.contrib import admin
from django.urls import path , include
# from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls', namespace='home')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # path("schema/",get_schema_view(title="Your Project", description="API for all things …", version="1.0.0"),
    #       name="openapi-schema",),
        path('schema/', SpectacularAPIView.as_view(), name='schema'),
        # Optional UI:
        path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]