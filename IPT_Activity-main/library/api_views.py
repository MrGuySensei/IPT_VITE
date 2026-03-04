from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Library, Author, Book, Member
from .serializers import (
    LibrarySerializer,
    AuthorSerializer,
    BookSerializer,
    MemberSerializer,
)


# ── Summary ──────────────────────────────────────────────────────────────────

@api_view(['GET'])
def api_root(request):
    """Overview of all available API endpoints."""
    return Response({
        'libraries': '/api/libraries/',
        'authors':   '/api/authors/',
        'books':     '/api/books/',
        'members':   '/api/members/',
    })


# ── Library ───────────────────────────────────────────────────────────────────

class LibraryListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/libraries/  → list all libraries
    POST /api/libraries/  → create a new library
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer


class LibraryDetailAPIView(generics.RetrieveDestroyAPIView):
    """
    GET    /api/libraries/<id>/  → retrieve a library
    DELETE /api/libraries/<id>/  → delete a library
    """
    queryset = Library.objects.all()
    serializer_class = LibrarySerializer
    lookup_field = 'library_id'


# ── Author ────────────────────────────────────────────────────────────────────

class AuthorListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/authors/  → list all authors (supports ?search=name)
    POST /api/authors/  → create a new author
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['author_name']
    ordering_fields = ['author_name', 'date_birth_year']
    ordering = ['author_name']


class AuthorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/authors/<id>/  → retrieve an author
    PUT    /api/authors/<id>/  → full update
    PATCH  /api/authors/<id>/  → partial update
    DELETE /api/authors/<id>/  → delete
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'author_id'


# ── Book ──────────────────────────────────────────────────────────────────────

class BookListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/books/  → list all books (supports ?search=title&author=id&library=id)
    POST /api/books/  → create a new book
    """
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['book_name', 'author__author_name']
    ordering_fields = ['book_name', 'date_published']
    ordering = ['book_name']

    def get_queryset(self):
        qs = Book.objects.select_related('author', 'library').all()
        author_id = self.request.query_params.get('author')
        library_id = self.request.query_params.get('library')
        if author_id:
            qs = qs.filter(author__author_id=author_id)
        if library_id:
            qs = qs.filter(library__library_id=library_id)
        return qs


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/books/<id>/  → retrieve a book
    PUT    /api/books/<id>/  → full update
    PATCH  /api/books/<id>/  → partial update
    DELETE /api/books/<id>/  → delete
    """
    queryset = Book.objects.select_related('author', 'library').all()
    serializer_class = BookSerializer
    lookup_field = 'book_id'


# ── Member ────────────────────────────────────────────────────────────────────

class MemberListCreateAPIView(generics.ListCreateAPIView):
    """
    GET  /api/members/  → list all members (supports ?search=name&book=id)
    POST /api/members/  → create a new member
    """
    serializer_class = MemberSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['member_name']
    ordering_fields = ['member_name', 'birth_year']
    ordering = ['member_name']

    def get_queryset(self):
        qs = Member.objects.select_related('book').all()
        book_id = self.request.query_params.get('book')
        if book_id:
            qs = qs.filter(book__book_id=book_id)
        return qs


class MemberDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET    /api/members/<id>/  → retrieve a member
    PUT    /api/members/<id>/  → full update
    PATCH  /api/members/<id>/  → partial update
    DELETE /api/members/<id>/  → delete
    """
    queryset = Member.objects.select_related('book').all()
    serializer_class = MemberSerializer
    lookup_field = 'member_id'
