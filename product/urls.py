
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .import views
from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',views.home, name='home'),
    path('saree',views.saree,name='saree'),
    path('menbottom',views.menbottomwear,name='menbott'),
    path('mentop',views.mentopwear,name='mentop'),
    path('menfoot',views.menfootwear,name='menfoot'),
    path('womentop',views.womentopwear,name='womentop'),
    path('womenbottom',views.womenbottomwear,name='womenbott'),
    path('womenfoot',views.womenfootear,name='womenfoot'),
    path('softtoys',views.softtoys,name='softtoys'),
    path('kiddress',views.kiddress,name='kiddress'),
    path('kidfoot',views.kidfootware,name='kidfoot'),
    path('stickers',views.stickers,name='stickers'),
    path('clocks',views.clocks,name='clocks'),
    path('showpiece',views.showpiece,name='showpiece'),
    path('kitchenstorage',views.kitchen,name='kitchenstorage'),
    path('makeup',views.makeup,name='makeup'),
    path('skincare',views.skincare,name='skincare'),
    path('haircare',views.haircare,name='haircare'),
    path('fragrance',views.fragrance,name='fragrance'),
    path('mobile',views.mobile,name='mobile'),
    path('smartwatch',views.smartwatch,name='smartwatch'),
    
    
    path('add_to_cart/<int:id>', views.add_to_cart, name='add_to_cart'),
    path('registration',views.Registration.as_view(),name='regi'),
    path('login/',views.CustomLoginView.as_view(), name='login'),
    path('showcart',views.view_cart, name='showcart'),
    path('increase_quantity/<int:cart_item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease_quantity/<int:cart_item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('buynow/<int:id>',views.buynow, name='buynow'),
    path('placeorder',views.placeorder, name='placeorder'),
    path('orderplace',views.orderplace, name='orderplace'),
    path('increases_quantity/<int:order_item_id>/', views.increases_quantity, name='increases_quantity'),
    path('decreases_quantity/<int:order_item_id>/', views.decreases_quantity, name='decreases_quantity'),
    path('remove_from_order/<int:order_item_id>/', views.remove_from_order, name='remove_from_order'),
    path('continuee',views.continuee, name='continuee'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('forgot',views.forgot_password, name='forgot'),
    path('remove_from_cart/<int:cart_item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:id>/', views.product_detail, name='pd'),
    path('detailform',views.detailform,name='detail'),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)