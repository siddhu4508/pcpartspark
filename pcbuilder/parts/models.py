from django.db import models

class Component(models.Model):
    CATEGORIES = [
        ('CPU', 'Processor'),
        ('GPU', 'Graphics Card'),
        ('RAM', 'Memory'),
        ('MOBO', 'Motherboard'),
        ('PSU', 'Power Supply Unit'),
        ('SSD', 'Solid-State Drive'),
        ('HDD', 'Hard Drive'),
        ('Case', 'Case'),
        ('Monitor', 'Monitor'),
        ('Keyboard', 'Keyboard'),
        ('Mouse', 'Mouse'),
        ('Headset', 'Headset'),
        ('Software', 'Software'),
        ('Other', 'Other'),
        ('Unknown', 'Unknown'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORIES)
    price_inr = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    url = models.URLField()
    description = models.TextField()
    rating = models.IntegerField()
    reviews = models.IntegerField()
    stock = models.IntegerField()
    release_date = models.DateField()
    warranty = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    specs = models.JSONField()
    amazon_link = models.URLField(blank=True)
    flipkart_link = models.URLField(blank=True)
    mdcomputers_link = models.URLField(blank=True)
    primeabgb_link = models.URLField(blank=True)
    vedantcomputers_link = models.URLField(blank=True)
    itdepot_link = models.URLField(blank=True)
    croma_link = models.URLField(blank=True)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    logo = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

class ComponentReview(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' - ' + self.user.username

class ComponentRating(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' - ' + self.user.username

class ComponentSpec(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    key = models.CharField(max_length=50)
    value = models.CharField(max_length=100)

    def __str__(self):
        return self.component.name + ' - ' + self.key
    
    class Meta:
        unique_together = ('component', 'key')
        

class ComponentImage(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' - ' + self.image.url

class ComponentVideo(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    video = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' - ' + self.video
    
class ComponentComparison(models.Model):
    component1 = models.ForeignKey('Component', related_name='component_comparison1', on_delete=models.CASCADE)
    component2 = models.ForeignKey('Component', related_name='component_comparison2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component1.name + ' vs ' + self.component2.name
    
    class Meta:
        unique_together = ('component1', 'component2')
    
class ComponentCompatibility(models.Model):
    component1 = models.ForeignKey('Component', related_name='component_compatibility1', on_delete=models.CASCADE)
    component2 = models.ForeignKey('Component', related_name='component_compatibility2', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component1.name + ' with ' + self.component2.name

    class Meta:
        unique_together = ('component1', 'component2')


class ComponentRecommendation(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    recommended_component = models.ForeignKey('Component', related_name='recommended_component', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' recommended with ' + self.recommended_component.name


class ComponentSale(models.Model):
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    sale_price_inr = models.DecimalField(max_digits=10, decimal_places=2)
    sale_start_date = models.DateField()
    sale_end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' on sale'
        
    
class ComponentWishlist(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' in wishlist'


    
# Add to build list

class ComponentBuildList(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    component = models.ForeignKey('Component', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.component.name + ' in build list'


class ComponentBuild(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name + ' by ' + self.user.username









