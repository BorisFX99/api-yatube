from django.contrib import admin

from .models import Comment, Group, Post


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0  # Не показывать пустые формы для добавления (ибо так захотелось)
    fields = ('author', 'text', 'created')  # Какие поля показывать
    readonly_fields = ('author', 'text', 'created')  # Запрещаем редактировать их прямо в списке
    show_change_link = True  # Добавляет ссылку "Изменить - вся крутота тут!"
    max_num = 0  # Запрещаем добавлять новые комментарии прямо из карточки поста


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'pub_date', 'author')
    list_display_links = ('text',)
    search_fields = ('text',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'
    inlines = [CommentInline]  # Привязываем комментарии к посту


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    # Указываем, какие поля выводить в списке
    list_display = ('id', 'author', 'post', 'text', 'created')
