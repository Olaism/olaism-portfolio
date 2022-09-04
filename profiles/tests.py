from django.core import mail
from django.test import TestCase
from django.urls import reverse, resolve
from django.views.generic import TemplateView

from . import views
from .forms import ContactForm
from .models import Profile, About, Skill, Project

class ProfilesSetUpTestCase(TestCase):
    
    def setUp(self):
        self.profile = Profile.objects.create(
            full_name='Test User',
            job='Testing Developer',
            describe_yourself='I love to write tests.'
        )
        self.about = About.objects.create(
            heading='I am a software developer',
            details="I have a lot of details to write but not here."
        )
        self.skill = Skill.objects.create(
            class_name="FaBrand FaHTML5",
            name = 'HTML5',
            skill_range = 85
        )
        self.project = Project.objects.create(
            title='My First Project',
            demo="https://www.projectdemo.com/",
            code='https://www.github.com/',
            highlight='My First Project highlights',
            details='A lot of details here.',
            program='Testing'
        )

class ProfilesModelTest(ProfilesSetUpTestCase):

    def setUp(self):
        super().setUp()


    def test_profile(self):
        self.assertTrue(Profile.objects.exists())
        self.assertEqual(self.profile.full_name, 'Test User')
        self.assertEqual(self.profile.job, 'Testing Developer')
        self.assertEqual(self.profile.describe_yourself, 'I love to write tests.')

    def test_about(self):
        self.assertTrue(About.objects.exists())
        self.assertEqual(self.about.heading, 'I am a software developer')
        self.assertEqual(self.about.details, 'I have a lot of details to write but not here.')

    def test_skill(self):
        self.assertTrue(Skill.objects.exists())
        self.assertEqual(self.skill.class_name, 'FaBrand FaHTML5')
        self.assertEqual(self.skill.name, 'HTML5')
        self.assertEqual(self.skill.skill_range, 85)

    def test_project(self):
        self.assertTrue(Project.objects.exists())
        self.assertEqual(self.project.title, 'My First Project')
        self.assertEqual(self.project.demo, 'https://www.projectdemo.com/')
        self.assertEqual(self.project.code, 'https://www.github.com/')
        self.assertEqual(self.project.highlight, 'My First Project highlights')
        self.assertEqual(self.project.details, 'A lot of details here.')
        self.assertEqual(self.project.program, 'Testing')


class HomeViewTest(ProfilesSetUpTestCase):

    def setUp(self):
        super().setUp()
        url = reverse('home')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/')
        self.assertEquals(view.func, views.home)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/home.html')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class AboutViewTest(ProfilesSetUpTestCase):

    def setUp(self):
        super().setUp()
        url = reverse('about')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/about/')
        self.assertEquals(view.func, views.about)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/about.html')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class SkillsViewTest(ProfilesSetUpTestCase):

    def setUp(self):
        super().setUp()
        url = reverse('skills')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/skills/')
        self.assertEquals(view.func, views.skills)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/skills.html')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class ProjectsViewTest(ProfilesSetUpTestCase):

    def setUp(self):
        super().setUp()
        url = reverse('projects')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/projects/')
        self.assertEquals(view.func, views.projects)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/projects.html')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class ProjectsDetailViewTest(ProfilesSetUpTestCase):

    def setUp(self):
        super().setUp()
        url = reverse('project_detail', kwargs={'pk': self.project.pk})
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/projects/1/')
        self.assertEquals(view.func, views.project_detail)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/project_detail.html')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class SuccesfulContactViewTest(TestCase):

    def setUp(self):
        super().setUp()
        url = '/contact/thanks/'
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/contact/thanks/')
        self.assertEquals(view.func.view_class, TemplateView)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/thanks.html')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class ContactGetHomeViewTest(TestCase):

    def setUp(self):
        url = reverse('contact')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_url_resolves_correct_view(self):
        view = resolve('/get-in-touch/')
        self.assertEquals(view.func, views.contact)

    def test_view_uses_correct_template(self):
        self.assertTemplateUsed(self.response, '_base.html')
        self.assertTemplateUsed(self.response, 'profiles/contact.html')

    def test_has_csrf_protection(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_forms(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, ContactForm)

    def test_form_inputs(self):
        self.assertContains(self.response, '<input type="email" ', 1)
        self.assertContains(self.response, '<input type="text" ', 1)
        self.assertContains(self.response, '<textarea', 1)
        self.assertContains(self.response, '<button type="submit" ')

    def test_view_contains_correct_links(self):
        home_link = reverse('home')
        project_link = reverse('projects')
        about_link = reverse('about')
        skill_link = reverse('skills')
        contact_link = reverse('contact')
        
        self.assertContains(self.response, home_link)
        self.assertContains(self.response, project_link)
        self.assertContains(self.response, about_link)
        self.assertContains(self.response, skill_link)
        self.assertContains(self.response, contact_link)

class SuccessfulContactPostTestCase(TestCase):

    def setUp(self):
        url = reverse('contact')
        self.response = self.client.post(url, {
            'subject': 'Subject', 
            'message': 'This is my message', 
            'your_email': 'testuser01@gmail.com'
        })

    def test_redirect(self):
        success_link = '/contact/thanks/'
        self.assertRedirects(self.response, success_link)

    def test_send_mail(self):
        self.assertEqual(len(mail.outbox), 1)

class UnsuccessfulContactPostTestCase(TestCase):

    def setUp(self):
        url = reverse('contact')
        self.response = self.client.post(url, {
            'subject': 'My Subject',
            'message': 'This is my message',
            'your_email': 'Olaism'
        })

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_form_error(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)

class InvalidContactPostTestCase(TestCase):

    def setUp(self):
        url =reverse('contact')
        self.response = self.client.post(url, {
            'subject': '',
            'message': '',
            'your_email': ''
        })

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        form = self.response.context.get('form')
        self.assertTrue(form.errors)