from django.test import TestCase
from django.contrib.auth.models import User


from .models import Word


class WordModelTests(TestCase):
    def test_adding_word(self):
        new_user = User(username='foo')
        new_word = Word(title='bar', user=new_user)
        self.assertEqual(new_word.title, 'bar')
