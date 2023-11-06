from django.test import TestCase, Client
from django.urls import reverse
from member.models import Member
from Mediatheque_root.models import Book, Cd, Dvd, BoardGame

# Create your tests here.

class TestShowMembers(TestCase):
    
    def setUp(self):
        self.client = Client()
        Member.objects.create(firstname="Kevin", lastname="Rognon")
        Member.objects.create(firstname="Laurie", lastname="Louis")
        
        self.show_members_url = reverse("show_members")
    
    def test_show_members(self):
        response = self.client.get(self.show_members_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_members.html')
        
        self.assertIn('members', response.context)
        
        self.assertEqual(len(response.context['members']), 2)
        
        
class TestShowMedias(TestCase):
    
    def setUp(self):
        self.client = Client()
        Book.objects.create(name="Le seigneur des anneaux. La communauté ce l'anneau", author="JRR Tolkien")
        Cd.objects.create(name="The Black Album", artist="Metallica")
        Dvd.objects.create(name="Interstellar", realisator="Christopher Nolan")
        BoardGame.objects.create(name="Banque Route", creator="Alpaga")
        
        self.show_medias_url = reverse("show_medias")
        
    def test_show_medias(self):
        response = self.client.get(self.show_medias_url)
        
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'show_medias_employee.html')
        
        
        self.assertIn('books', response.context)
        self.assertIn('cds', response.context)
        self.assertIn('dvds', response.context)
        self.assertIn('boardgames', response.context)
        
        self.assertEqual(len(response.context['books']), 1)
        self.assertEqual(len(response.context['cds']), 1)
        self.assertEqual(len(response.context['dvds']), 1)
        self.assertEqual(len(response.context['boardgames']), 1)
        
class TestAddMedia(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.add_media_url = reverse('add_media')
        
    def test_add_book(self):
        response = self.client.post(self.add_media_url, {
            'type_media': 'BOOK',
            'title_media': 'Dune',
            'author_media': 'Frank Herbert'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Book.objects.count(), 1)
        new_book = Book.objects.first()
        self.assertEqual(new_book.name, 'Dune')
        self.assertEqual(new_book.author, 'Frank Herbert')
        self.assertEqual(new_book.available, True)
        
    def test_add_cd(self):
        response = self.client.post(self.add_media_url, {
            'type_media': 'CD',
            'title_media': 'The Black Album',
            'author_media': 'Metallica'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Cd.objects.count(), 1)
        new_cd = Cd.objects.first()
        self.assertEqual(new_cd.name, 'The Black Album')
        self.assertEqual(new_cd.artist, 'Metallica')
        self.assertEqual(new_cd.available, True)
        
    def test_add_dvd(self):
        response = self.client.post(self.add_media_url, {
            'type_media': 'DVD',
            'title_media': 'Interstellar',
            'author_media': 'Christopher Nolan'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Dvd.objects.count(), 1)
        new_dvd = Dvd.objects.first()
        self.assertEqual(new_dvd.name, 'Interstellar')
        self.assertEqual(new_dvd.realisator, 'Christopher Nolan')
        self.assertEqual(new_dvd.available, True)
        
    def test_add_boardgame(self):
        response = self.client.post(self.add_media_url, {
            'type_media': 'BOARDGAME',
            'title_media': 'Banque Route',
            'author_media': 'Alpaga'
        })
        
        self.assertEqual(response.status_code, 302)
        self.assertEqual(BoardGame.objects.count(), 1)
        new_boardgame = BoardGame.objects.first()
        self.assertEqual(new_boardgame.name, 'Banque Route')
        self.assertEqual(new_boardgame.creator, 'Alpaga')
