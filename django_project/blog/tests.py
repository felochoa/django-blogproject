from django.test import TestCase
from django.contrib.auth import get_user_model #for user related tests
from django.urls import reverse

from .models import Post

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser", email= "test@email.com", password= "secret"
        )

        cls.post = Post.objects.create(
            title="Good title",
            body="great body",
            author =cls.user,
            )

    def test_post_model(self):
        #we test all fields and mehtods of the post model
        self.assertEqual(self.post.title, "Good title")
        self.assertEqual(self.post.body, "great body")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "Good title") #__str__ method test
        self.assertEqual(self.post.get_absolute_url(), "/post/1/") #get absolute url test
        
    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_exists_at_corect_location_detailview(self):
        response = self.client.get("/post/1/")  
        self.assertEqual(response.status_code, 200)  
    
    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "great body")
        self.assertTemplateUsed(response, "home.html")
    
    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail", kwargs={"pk": self.post.pk}))
        no_response = self.client.get("/post/100000/") # post that is not created
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Good title")
        self.assertTemplateUsed(response, "post_detail.html")

