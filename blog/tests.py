from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse, resolve
from .views import post_list, post_detail
from .models import Post

class PostListTestCase(TestCase):

    def setUp(self):
        pass

    def test_post_list_url_reverse_correctly(self):
        url = reverse('blog:post_list')
        self.assertEqual(url, '/')

    def test_post_list_url_resolves_correctly(self):
        url = reverse('blog:post_list')
        found = resolve(url)
        self.assertEqual(found.func, post_list)

    def test_post_list_returns_correct_html(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_post_list_page(self):
        url = reverse('blog:post_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'blog/post_list.html')

    # def test_post_list_contains(self):
    #     url = reverse('post_list')
    #     response = self.client.get(url)
    #     self.assertContains(response, )


class PostDetailTestCase(TestCase):

    def setUp(self):
        pass
        # me = User.objects.get(username="mussaiin")
        # Post.objects.create(author=me, title="test", text="test")

    def test_post_detail_url_reverse_correctly(self):
        url = reverse('blog:post_detail', kwargs={'pk': 1})
        # print(url)
        self.assertEqual(url, '/post/1/')

    def test_post_list_detail_resolves_correctly(self):
        url = reverse('blog:post_detail', kwargs={'pk': 1})
        found = resolve(url)
        self.assertEqual(found.func, post_detail)

    # def test_post_detail_returns_correct_html(self):
    #     url = reverse('blog:post_detail', kwargs={'pk': 9})
    #     response = self.client.get(url)
    #     self.assertEqual(response.status_code, 200)

    def test_post_detail_page(self):
        url = reverse('blog:post_detail', kwargs={'pk': 9})
        response = self.client.get(url)
        print(response)
        # self.assertTemplateUsed(response, 'blog/post_detail.html')
