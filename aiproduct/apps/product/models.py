from django.db import models


class Category(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=False, null=False)
    icon = models.CharField(max_length=255, blank=False, null=False)
    color = models.CharField(max_length=255, blank=False, null=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.TextField(blank=False, null=False)
    url = models.TextField(blank=False, null=False)
    image_url = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, null=False, blank=False, related_name='products')
    domain = models.CharField(max_length=255, null=False)
    def __str__(self):
        return self.title


class ProductClick(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=255, null=False)
    click_source = models.TextField(blank=False, null=False)
    product = models.ForeignKey('Product', on_delete=models.DO_NOTHING, null=False, blank=False, related_name='clicks')

    def save(self, *args, **kwargs):
        super(ProductClick, self).save(*args, **kwargs)


class UserUtmParameter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uid = models.CharField(max_length=255, null=False)
    ctime = models.DateTimeField(null=False)
    utm_campaign = models.CharField(max_length=255, null=True, blank=True)
    utm_content = models.CharField(max_length=255, null=True, blank=True)
    utm_medium = models.CharField(max_length=255, null=True, blank=True)
    utm_source = models.CharField(max_length=255, null=True, blank=True)
    client_ip_address = models.TextField(null=True, blank=True)
    client_user_agent = models.TextField(null=True, blank=True)
    source_url = models.TextField(null=True, blank=True)
    utm_term = models.TextField(null=True, blank=True)
    fbclid = models.TextField(null=True, blank=True)
    gclid = models.TextField(null=True, blank=True)
    gbraid = models.TextField(null=True, blank=True)
    wbraid = models.TextField(null=True, blank=True)
    irclickid = models.TextField(null=True, blank=True)
    blogsource = models.CharField(max_length=255, null=True, blank=True)
    ttclid = models.TextField(null=True, blank=True)
    sccid = models.TextField(null=True, blank=True)