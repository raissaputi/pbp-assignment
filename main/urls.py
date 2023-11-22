from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
from main.views import register, login_user, logout_user
from main.views import get_product_json, create_ajax, delete_ajax
from main.views import create_item_flutter, show_json_user

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', create_ajax, name='create_ajax'),
    path('delete-ajax/<int:id>/', delete_ajax, name='delete_ajax'),
    path('create-flutter/', create_item_flutter, name='create_item_flutter'),
    path('json-user/', show_json_user, name='show_json_user'),
]