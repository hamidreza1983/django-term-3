from typing import Any
from django.core.management.base import BaseCommand
from accounts.models import CustomUser
from faker import Faker
from services.models import Category, Options, Services
import random


class Command(BaseCommand):
    help = "create fake data for developer"
    def __init__(self):
        super().__init__()
        self.faker = Faker()
        self.category = Category.objects.all()
        self.generals = Options.objects.all()
        self.category_list = ["c1", "c2", "c3"]
        self.general_list = ["g1", "g2", "g3"]


    def handle(self, *args, **options):
        for cat in self.category_list:
            Category.objects.get_or_create(title=cat)

        for general in self.general_list:
            Options.objects.get_or_create(title=general)

        for _ in range(20):
            service = Services.objects.create(
                title = self.faker.name(),
                name = self.faker.name(),
                content = self.faker.text(),
                description = self.faker.text(),
                price = self.faker.pyint(),
            )

            cat = random.choices(list(self.category), k=2)
            gen = random.choices(list(self.generals), k=2)
            service.category.set(cat)
            service.generals.set(gen)


        # for _ in range (10):
        #     CustomUser.objects.create_user(email=self.faker.email(), password=self.faker.password())
        print ("objects created")