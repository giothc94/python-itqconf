from django.urls import path
from .views import PageDetailView,PageUpdateView,PageDeleteView

urlpatterns = [
    path('<int:pk>', PageDetailView.as_view(),name="page_footer"),
    path('update/<int:pk>', PageUpdateView.as_view(),name="page_footer_update"),
    path('delete/<int:pk>', PageDeleteView.as_view(),name="page_footer_delete"),
]