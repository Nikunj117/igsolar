from django.urls import path
from .views import *
from django.conf.urls import *
from django.views.decorators.csrf import csrf_exempt
from django.contrib.sitemaps.views import sitemap
# from app_blog.sitemap import AllBlogsSitemap, HomeSitemap, TagSitemap

# sitemaps = {
#     "posts": AllBlogsSitemap,
#     'home': HomeSitemap,
#     'tags': TagSitemap,
# }

urlpatterns = [
    path('',Home.as_view(),name='home'),
    path('contact',ContactView.as_view(),name='contact'),
    path('about',AboutUS.as_view(),name='about'),
    path('productandservices',ProductAndService.as_view(),name='productandservices'),
    path('solarpowersystem',SolarPowerSystem.as_view(),name='solarpowersystem'),
    path('vectoriarebate',VectoriaRebate.as_view(),name='vectoriarebate'),
    path('blog',Blog.as_view(),name='blog'),
    # path('finance/blogs/<slug:slug>/', blogs_detail.as_view(), name='blog_detail'),
    # path('finance/tags/<slug:slug>/', TagSlug.as_view(), name='tag_details'),
    # path('blogs/',BlogsListView.as_view(),name='blogList'),
    # path('blog/sitemap.xml', SitemapView.as_view(), name='news_sitemap'),
    # path('search-blog/', BlogSearch.as_view(), name='search-blog'),
    # path('robots.txt', RobotsTxtView.as_view(), name='robots.txt'),
    # path('cookie-policy/', cookies.as_view(), name='cookie-policy'),
    # path('restart_services/', restart_services.as_view(), name='restart_services'),
    # path('privacy-policy/', policy.as_view(), name='privacy-policy'),
    # path('disclaimer/', disclaimer.as_view(), name='disclaimer'),
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="sitemap"), 
]


