from urllib import response
from django.test import TestCase
from plklsys.views import MainPage
from .models import FilmRequest


class HomePageTest(TestCase):
	def test_mainpage_as_seen_client(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')


	# def test_responding_post_request(self):
	# 	resp = self.client.post('/', data={'name' :'philiName',
	# 		'email': 'philiEmail',
	# 		'film': 'philiFilm',
	# 		'director': 'philiDir',
	# 		'genre': 'philiGenre',
	# 		'review': 'philiReview'})
	# 	self.assertIn('philiName', resp.content.decode())
	# 	self.assertTemplateUsed(resp, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', {'name' :'Mark Ledif Canoy',
	 		'email': 'markledif15@gmail.com',
	 		'film': 'Buy Bust',
	 		'director': 'Erik Matti',
			'genre': 'Action'})
		self.assertEqual(FilmRequest.objects.count(),1)
		inputData = FilmRequest.objects.first()
		self.assertEqual(inputData.cphile_name, 'Mark Ledif Canoy')
		self.assertEqual(inputData.cphile_email, 'markledif15@gmail.com')
		self.assertEqual(inputData.cphile_title, 'Buy Bust')
		self.assertEqual(inputData.cphile_director, 'Erik Matti')
		self.assertEqual(inputData.cphile_genre, 'Action')
		
	def test_POST_redirect(self):
		response = self.client.post('/', {'name' :'Mark Ledif Canoy',
	 		'email': 'markledif15@gmail.com',
	 		'film': 'Buy Bust',
	 		'director': 'Erik Matti',
			'genre': 'Action'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/')

	def test_only_saves_items_uf_necessary(self):
		self.client.get('/')
		self.assertEqual(FilmRequest.objects.count(), 0)

class ORMTEST(TestCase):
	def test_saving_retrive(self):
		FilmRequest_sheet = FilmRequest()
		FilmRequest_sheet.cphile_name = 'Mark Ledif Canoy'
		FilmRequest_sheet.cphile_email = 'markledif15@gmail.com'
		FilmRequest_sheet.cphile_title = 'Buy Bust'
		FilmRequest_sheet.cphile_director = 'Erik Matti'
		FilmRequest_sheet.cphile_genre = 'Action'
		
		FilmRequest_sheet.save()

		FilmRequest_sheet = FilmRequest()
		FilmRequest_sheet.cphile_name = 'Lxdif'
		FilmRequest_sheet.cphile_email = 'markfidel16@gmail.com'
		FilmRequest_sheet.cphile_title = 'Kisap Mata'
		FilmRequest_sheet.cphile_director = 'Mike De Leon'
		FilmRequest_sheet.cphile_genre = 'Action'
		
		FilmRequest_sheet.save()

		FilmRequest_DB = FilmRequest.objects.all()
		self.assertEqual(FilmRequest_DB.count(), 2)

		plkldata1 = FilmRequest_DB[0]
		plkldata2 = FilmRequest_DB[1]

		self.assertEqual(plkldata1.cphile_name, 'Mark Ledif Canoy')
		self.assertEqual(plkldata1.cphile_email, 'markledif15@gmail.com')
		self.assertEqual(plkldata1.cphile_title, 'Buy Bust')
		self.assertEqual(plkldata1.cphile_director, 'Erik Matti')
		self.assertEqual(plkldata1.cphile_genre, 'Action')
		

		self.assertEqual(plkldata2.cphile_name, 'Lxdif')
		self.assertEqual(plkldata2.cphile_email, 'markfidel16@gmail.com')
		self.assertEqual(plkldata2.cphile_title, 'Kisap Mata')
		self.assertEqual(plkldata2.cphile_director, 'Mike De Leon')
		self.assertEqual(plkldata2.cphile_genre, 'Action')
			

	def test_template_display_list(self):
		FilmRequest.objects.create(cphile_name = 'Lxdif',
			cphile_email = 'markfidel16@gmail.com',
			cphile_title = 'Kisap Mata',
			cphile_director = 'Mike De Leon',
			cphile_genre = 'Action')

		FilmRequest.objects.create(cphile_name = 'Mark Ledif Canoy',
			cphile_email = 'markledif15@gmail.com',
			cphile_title = 'Buy Bust',
			cphile_director = 'Erik Matti',
			cphile_genre = 'Action')

		response = self.client.get('/')
		self.assertIn('Lxdif, markfidel16@gmail.com, Kisap Mata, Mike De Leon, Action', response.content.decode())
		self.assertIn('Mark Ledif Canoy, markledif15@gmail.com, Buy Bust, Erik Matti, Action', response.content.decode())


