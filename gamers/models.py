# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext

# Create your models here.
class Games(models.Model):
    name = models.CharField(max_length=130, default='Tetra')
#    members = models.CharField(max_length=13, blank=True)

    class Meta:
         ordering = ('name',)
    def __str__(self):
        return self.name

class Members(models.Model):
    name = models.CharField(max_length=130, default='Bob')
    GamesJoined = models.ManyToManyField(Games, related_name='joiners', null=True)
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
         ordering = ('name',)
    def __str__(self):
        return self.name









class StoreCategory(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Store(models.Model):
    name = models.CharField(max_length=250)
    store_category = models.ForeignKey(
        StoreCategory,
        related_name='stores',
        on_delete=models.CASCADE)
    been_audited = models.BooleanField(default=False)
    inserted_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Manager(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = ((MALE, 'Male'),(FEMALE, 'Female'),)
    name = models.CharField(max_length=150, blank=False, default='')
    gender = models.CharField(max_length=130,choices=GENDER_CHOICES,default=MALE,)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Region(models.Model):
    manager = models.ForeignKey(
        Manager,
        related_name='regions',
        on_delete=models.CASCADE)
    store = models.ForeignKey(
        Store,
        on_delete=models.CASCADE)
    store_of_month = models.IntegerField()
    established = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Order by distance in descending order
        ordering = ('-store_of_month',)
