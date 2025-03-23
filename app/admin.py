from django.contrib import admin 
from django.apps import apps 

app = apps.get_app_config( 'app' ) 
models = app.get_models() 

for m in models :
    admin.site.register( m ) 
