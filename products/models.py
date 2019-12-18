from django.db import models

# Create your models here.
class ProductCategory(models.Model):
	category_name=models.CharField(max_length=200,null=False,blank=False)
	published=models.IntegerField(default=1,null=False,blank=False)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return str(self.id)

class Product(models.Model):
	title=models.CharField(max_length=200,null=False,blank=False)
	description=models.TextField(null=True,blank=True)
	price=models.DecimalField(decimal_places=2,max_digits=100)
	slug=models.SlugField()
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)
	active=models.BooleanField(default=True)
	category_id=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

	def __str__(self):
		return self.title

class User(models.Model):
	name=models.CharField(max_length=200,null=False,blank=False)
	email=models.CharField(max_length=200,null=False,blank=False)
	password=models.CharField(max_length=200,null=False,blank=False)
	address=models.CharField(max_length=200,null=False,blank=False)
	published=models.IntegerField(default=1,null=False,blank=False)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	updated=models.DateTimeField(auto_now_add=False,auto_now=True)

	def __str__(self):
		return str(self.id)

class UserInterest(models.Model):
	user_id=models.ForeignKey(User,on_delete=models.CASCADE,related_name='interest_user')
	product_id=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='interest_product')
	created=models.DateTimeField(auto_now_add=True,auto_now=False)
	modified=models.DateTimeField(auto_now_add=False,auto_now=True)
	confirmed=models.IntegerField(default=1,null=False,blank=False)

	def __str__(self):
		return str(self.id)
