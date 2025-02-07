from django.contrib import admin
from .models import Author, Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')  # Show title, author, and price
    list_filter = ('author',)  # Add a filter by author
    search_fields = ('title',)  # Enable search by book title

    actions = ['mark_as_discounted']

    @admin.action(description="Apply 10% discount to selected books")
    def mark_as_discounted(self, request, queryset):
        for book in queryset:
            book.price *= 0.9
            book.save()

class BookInline(admin.TabularInline):
    model = Book
    extra = 1  # Allows adding books directly in the Author admin page

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]  # Inline editing of books inside the Author admin page

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
