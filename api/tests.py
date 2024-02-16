from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        UserModel = get_user_model()
        self.user = UserModel.objects.create(
            username = 'firstuser23',
            email='ourfirstser@email.com',
            password='ourlittlesecret'
        )
    
    def test_user_model_content(self):
        user = self.user
        username = user.username
        email = user.email
        password = user.password
        self.assertEqual(username, 'firstuser23')
        self.assertEqual(email, 'ourfirstser@email.com')
        self.assertEqual(password, 'ourlittlesecret')
    
class UserApiTest(TestCase):
    user = {
        'username':'seconduser23',
        'email':'ourseconduser@email.com',
        'password':'ourlittlesecret',
        }

    def test_user_register_api(self):
        res = self.client.post(reverse('register'), self.user)
        self.assertEqual(res.status_code, 201)

    def test_user_login_api(self):
        self.client.post(reverse('register'), self.user)
        res = self.client.post(reverse('login'), {'email':self.user['email'],'password':self.user['password']})
        self.assertEqual(res.status_code, 200)

    def test_user_logout_api(self):
        self.client.post(reverse('register'), self.user)
        self.client.post(reverse('login'), {'email':self.user['email'],'password':self.user['password']})
        res = self.client.post(reverse('logout'))
        self.assertEqual(res.status_code, 200)

    def test_user_view_api(self):
        self.client.post(reverse('register'), self.user)
        self.client.post(reverse('login'), {'email':self.user['email'],'password':self.user['password']})
        res = self.client.get(reverse('user'))
        self.assertEqual(res.status_code, 200)