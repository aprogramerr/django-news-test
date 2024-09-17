from tqdm import tqdm
from faker import Faker
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from app_news.models import News

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
        User.objects.create_superuser(
            username='admin',
            password='sahm1383',
        )
        fake= Faker()
        for i in tqdm(range(100)):
            first_name = fake.first_name()
            last_name = fake.last_name()
            author,created = User.objects.get_or_create(
                username = first_name + '.' + last_name,
                first_name=first_name,
                last_name=last_name, 
                )
        for j in range(20):    
            News.objects.create(
                author = author,
                title = fake.paragraph(nb_sentences=1),
                description = fake.paragraph(nb_sentences=20),
                status = 'pb', 
            )
        #     # self.stdout.write(
            #     self.style.SUCCESS('Successfully closed poll "%s"' % 2)
            # )