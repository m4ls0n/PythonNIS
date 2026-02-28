from django.db import migrations
from django.contrib.auth.hashers import make_password

def generate_mock_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    Post = apps.get_model('api', 'Post')
    Comment = apps.get_model('api', 'Comment')

    user1 = User.objects.create(username='mock_user_1', password=make_password('pass123'))
    user2 = User.objects.create(username='mock_user_2', password=make_password('pass123'))

    post1 = Post.objects.create(
        title='Первый тестовый пост', 
        text='Текст для проверки мок-данных из миграции.', 
        author=user1
    )
    post2 = Post.objects.create(
        title='Второй тестовый пост', 
        text='Еще немного текста для второго поста.', 
        author=user2
    )

    Comment.objects.create(post=post1, author=user2, text='Крутой пост, спасибо!')
    Comment.objects.create(post=post2, author=user1, text='Согласен, очень полезно.')

def reverse_mock_data(apps, schema_editor):
    User = apps.get_model('auth', 'User')
    User.objects.filter(username__in=['mock_user_1', 'mock_user_2']).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'), 
    ]

    operations = [
        migrations.RunPython(generate_mock_data, reverse_mock_data),
    ]