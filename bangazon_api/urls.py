
from django.conf.urls import url, include
from bangazon_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'products', views.ListProductsView)
router.register(r'customers', views.ListCustomersView)
router.register(r'product_type', views.ListProductTypeView)
router.register(r'payment_type', views.ListPaymentTypeView)
router.register(r'order', views.ListOrderView)


urlpatterns = [
    url(r'^', include(router.urls))
    # path('products/', ListProductsView.as_view(), name="products-all")
]
