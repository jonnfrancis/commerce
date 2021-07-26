from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing/new",views.newListing,name="newListing"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("watchlist/<int:listing_id>/change/<str:reverse_method>", views.change_watchlist, name="change_watchlist"),
    path("listing/<int:listing_id>", views.listing, name="listing"),
    path("listing/<int:listing_id>/bid", views.take_bid, name="take_bid"),    
    path("listing/<int:listing_id>/close", views.close_listing, name="close_listing"),
    path("listing/<int:listing_id>/comment", views.comment, name="comment"),
    path("categories", views.categories, name="categories"),

]
