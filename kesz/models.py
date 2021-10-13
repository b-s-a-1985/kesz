from django.db import models


class Country(models.Model):
    name = models.CharField(
        default='Hungary',
        blank=False,
        max_length=200,
        unique=True
        )
    phone_code = models.CharField(
        blank=False,
        max_length=20
        )
    note = models.TextField(
        blank=True,
        null=True
        )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.name


class Address(models.Model):
    address = models.CharField(
        blank=False,
        max_length=250
        )
    note = models.TextField(
        blank=True,
        null=True
        )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.address


class Phone(models.Model):
    number = models.CharField(
        blank=False,
        max_length=20,
        unique=True
        )
    extension = models.CharField(
        blank=True,
        null=True,
        max_length=10
        )
    note = models.TextField(
        blank=True,
        null=True
        )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.number


class Email(models.Model):
    address = models.EmailField(
        max_length=254,
        unique=True
    )
    note = models.TextField(
        blank=True,
        null=True
        )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.address


class Position(models.Model):
    name = models.CharField(
        max_length=250,
        blank=False,
        null=False,
    )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.name


class Organization(models.Model):
    name = models.CharField(max_length=250)
    profile = models.CharField(max_length=250)
    country = models.ForeignKey(
        'Country',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        default='Hungary'
    )
    address = models.ManyToManyField('Address')
    phone = models.ManyToManyField('Phone')
    email = models.ManyToManyField('Email')
    note = models.TextField(
        blank=True,
        null=True
    )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(
        blank=False,
        null=False,
        max_length=200
        )
    country = models.ForeignKey(
        'Country',
        blank=False,
        null=False,
        on_delete=models.CASCADE,
        default='Hungary'
        )
    phone = models.ManyToManyField(
        'Phone',
        related_name='persons'
    )
    email = models.ManyToManyField(
        'Email',
        # blank=True,     # no effect
        # null=True,      # no effect
    )
    note = models.TextField(
        blank=True,
        null=True
        )
    organization = models.ForeignKey(
        'Organization',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    position = models.ForeignKey(
        'Position',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    owner = models.CharField(
        blank=True,
        null=True,
        max_length=20
    )

    def __str__(self):
        return self.name
