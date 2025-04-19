from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    path('search/', views.search_books, name='books.search'),
    path('search/', views.search_books, name='search_books'),
    path('simple/query', views.simple_query, name='books.simple_query'),
    path('complex/query', views.complex_query, name='books.complex_query'),
    path('lab9/task1', views.task1, name='lab9.task1'),
    path('lab9/task2', views.task2, name='lab9.task2'),
    path('lab9/task3', views.task3, name='lab9.task3'),
    path('lab9/task4', views.task4, name='lab9.task4'),
    
]