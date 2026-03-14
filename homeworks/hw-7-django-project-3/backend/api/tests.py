from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment

class APIEndpointsTests(APITestCase):
    def setUp(self):
        # два тестовых пользователя
        self.user1 = User.objects.create_user(username='author1', password='password123')
        self.user2 = User.objects.create_user(username='author2', password='password123')

        # тестовый пост от первого пользователя
        self.post = Post.objects.create(
            title='Test Post', 
            text='This is a test post text.', 
            author=self.user1
        )
        
        # тестовый коммент к посту от первого пользователя
        self.comment = Comment.objects.create(
            post=self.post, 
            text='Test Comment', 
            author=self.user1
        )

        # базовые юрл
        self.posts_url = '/api/posts/'
        self.comments_url = '/api/comments/'
        self.users_url = '/api/users/'

    # тесты для постов

    def test_get_posts_public(self):
        """Проверка, что список постов доступен без авторизации"""
        response = self.client.get(self.posts_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post_unauthorized(self):
        """Аноним не может создать пост"""
        data = {'title': 'New Post', 'text': 'Content'}
        response = self.client.post(self.posts_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_post_authorized(self):
        """Авторизованный пользователь может создать пост"""
        self.client.force_authenticate(user=self.user1)
        data = {'title': 'New Post', 'text': 'Content'}
        response = self.client.post(self.posts_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_post_by_author(self):
        """Автор может изменить свой пост"""
        self.client.force_authenticate(user=self.user1)
        response = self.client.patch(f"{self.posts_url}{self.post.id}/", {'title': 'Updated Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post_by_other_user(self):
        """Другой пользователь НЕ может изменить чужой пост (проверка IsAuthorOrReadOnly)"""
        self.client.force_authenticate(user=self.user2)
        response = self.client.patch(f"{self.posts_url}{self.post.id}/", {'title': 'Hacked Title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_lightweight_action(self):
        """Проверка кастомного метода lightweight"""
        response = self.client.get(f"{self.posts_url}lightweight/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('title', response.data[0])
        self.assertNotIn('text', response.data[0])

    # тесты для комментов

    def test_create_comment_authorized(self):
        """Авторизованный юзер может оставить комментарий"""
        self.client.force_authenticate(user=self.user2)
        data = {'post': self.post.id, 'text': 'Nice post!'}
        response = self.client.post(self.comments_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # тесты для пользователей

    def test_user_stats_action(self):
        """Проверка агрегированной статистики пользователя"""
        response = self.client.get(f"{self.users_url}{self.user1.id}/stats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['total_posts'], 1)
        self.assertEqual(response.data['total_comments'], 1)