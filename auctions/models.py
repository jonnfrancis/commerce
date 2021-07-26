from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    pass


class Category(models.Model):
    category = models.CharField(max_length=30)



    def __str__(self):
        return f"{self.category}"


class Photo(models.Model):
    image_name = models.TextField()
    url = models.TextField()

    def __str__(self):
        return f"{self.url}"

class Listing(models.Model):
    title = models.CharField(max_length=60)
    flActive = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.CharField(null=True, max_length=300)
    startingBid = models.FloatField()
    currentBid = models.FloatField(blank=True, null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name="similar_listings")
    creator = models.ForeignKey(User, on_delete=models.PROTECT, related_name="all_creator_listings")
    photos = models.ManyToManyField(Photo, related_name='photos', blank=True)
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_listings")
    buyer = models.ForeignKey(User, null=True, on_delete=models.PROTECT)



    def __str__(self):
        return f"{self.title} - {self.startingBid}"        


class Bid(models.Model):
    auction = models.ForeignKey(Listing,on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    offer = models.FloatField()
    date = models.DateTimeField(auto_now=True)



class Comment(models.Model):
    comment = models.CharField(max_length=100)
    createdDate = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="get_comments")

    def get_creation_date(self):
        return self.createdDate.strftime('%B %d %Y')

    def __str__(self):
        return f"{self.user} {self.listing} {self.comment}"    

class WatchList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    auctions = models.ManyToManyField(Listing, related_name="auctions", blank=True)
    
    def __str__(self):
        return f"{self.user}'s watchlist'"



