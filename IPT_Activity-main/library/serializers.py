from rest_framework import serializers
from .models import Library, Author, Book, Member


class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['library_id']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['author_id', 'author_name', 'phone_number', 'gender', 'date_birth_year']


class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.author_name', read_only=True)
    library_display = serializers.CharField(source='library.__str__', read_only=True)

    class Meta:
        model = Book
        fields = [
            'book_id', 'book_name', 'date_published',
            'author', 'author_name',
            'library', 'library_display',
        ]


class MemberSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.book_name', read_only=True)

    class Meta:
        model = Member
        fields = [
            'member_id', 'member_name', 'phone_number',
            'gender', 'birth_year',
            'book', 'book_title',
        ]