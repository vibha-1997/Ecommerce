from django.contrib import admin
from .models import Product,ProductCategory,User,UserInterest

class ProductCategoryAdmin(admin.ModelAdmin):
	list_display=['id','category_name','published','timestamp','updated']
	class Meta:
		model=ProductCategory

class ProductAdmin(admin.ModelAdmin):
	list_display=['id','title','price','timestamp','updated','category_id']
	prepopulated_fields={'slug':('title',)}
	class Meta:
		model=Product

class UserAdmin(admin.ModelAdmin):
	list_display=['id','name','email','password','address','published','timestamp','updated']
	class Meta:
		model=User

class UserInterestAdmin(admin.ModelAdmin):
	list_display=['id','user_id','product_id','confirmed','created','modified']
	class Meta:
		model=UserInterest

admin.site.register(Product,ProductAdmin)
admin.site.register(ProductCategory,ProductCategoryAdmin)
admin.site.register(User,UserAdmin)
admin.site.register(UserInterest,UserInterestAdmin)

# Register your models here.
