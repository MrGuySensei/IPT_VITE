from django.urls import path
from . import views
from . import api_views

urlpatterns = [

    # ── HTML Views (unchanged) ────────────────────────────────────────────────

    path('', views.home, name='home'),

    # Library
    path('libraries/', views.library_list, name='library_list'),
    path('libraries/create/', views.create_library, name='create_library'),
    path('libraries/delete/<int:library_id>/', views.delete_library, name='delete_library'),

    # Author
    path('authors/', views.author_list, name='author_list'),
    path('authors/create/', views.create_author, name='create_author'),
    path('authors/update/<int:author_id>/', views.update_author, name='update_author'),
    path('authors/delete/<int:author_id>/', views.delete_author, name='delete_author'),

    # Book
    path('books/', views.book_list, name='book_list'),
    path('books/create/', views.create_book, name='create_book'),
    path('books/update/<int:book_id>/', views.update_book, name='update_book'),
    path('books/delete/<int:book_id>/', views.delete_book, name='delete_book'),

    # Member
    path('members/', views.member_list, name='member_list'),
    path('members/create/', views.create_member, name='create_member'),
    path('members/update/<int:member_id>/', views.update_member, name='update_member'),
    path('members/delete/<int:member_id>/', views.delete_member, name='delete_member'),

    # ── REST API Endpoints ────────────────────────────────────────────────────

    path('api/', api_views.api_root, name='api_root'),

    # Library API
    path('api/libraries/', api_views.LibraryListCreateAPIView.as_view(), name='api_library_list'),
    path('api/libraries/<int:library_id>/', api_views.LibraryDetailAPIView.as_view(), name='api_library_detail'),

    # Author API
    path('api/authors/', api_views.AuthorListCreateAPIView.as_view(), name='api_author_list'),
    path('api/authors/<int:author_id>/', api_views.AuthorDetailAPIView.as_view(), name='api_author_detail'),

    # Book API
    path('api/books/', api_views.BookListCreateAPIView.as_view(), name='api_book_list'),
    path('api/books/<int:book_id>/', api_views.BookDetailAPIView.as_view(), name='api_book_detail'),

    # Member API
    path('api/members/', api_views.MemberListCreateAPIView.as_view(), name='api_member_list'),
    path('api/members/<int:member_id>/', api_views.MemberDetailAPIView.as_view(), name='api_member_detail'),
]
