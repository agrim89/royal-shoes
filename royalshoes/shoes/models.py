from django.db import models


class Registration(models.Model):
    name = models.CharField(max_length=1000, null=True, blank=True)
    mobile = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    dob = models.DateField(null=True, blank=True)
    password = models.CharField(max_length=50)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "User List"

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return "{}".format(self.name)


class CompanyList(models.Model):
    company_name = models.CharField(max_length=100)
    company_image = models.URLField()

    class Meta:
        ordering = ['company_name']
        verbose_name_plural = "Company List"

    def __str__(self):
        return "{}".format(self.company_name)

    def __unicode__(self):
        return "{}".format(self.company_name)


class CompanyBanner(models.Model):
    banner = models.URLField()
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Company Banner"

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return "{}".format(self.name)


class ShoeList(models.Model):
    shoe_image = models.URLField()
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    size = models.CharField(max_length=100)
    company = models.ForeignKey(to=CompanyList, on_delete=models.CASCADE)
    company_banner = models.ForeignKey(to=CompanyBanner, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Shoes List"

    def __str__(self):
        return "{}".format(self.name)

    def __unicode__(self):
        return "{}".format(self.name)


class AddToCart(models.Model):
    shoe = models.ForeignKey(to=ShoeList, on_delete=models.CASCADE)
    user = models.ForeignKey(to=Registration, on_delete=models.CASCADE)
    items = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()
    status = models.BooleanField(default=True)

    class Meta:
        ordering = ['shoe']
        verbose_name_plural = "Add To Cart"

    def __str__(self):
        return "{} : {}".format(self.shoe, self.user)

    def __unicode__(self):
        return "{} : {}".format(self.shoe, self.user)
