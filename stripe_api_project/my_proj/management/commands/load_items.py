import csv

from django.core.management.base import BaseCommand

from my_proj.models import Item


class Command(BaseCommand):
    help = 'Импорт товаров из csv файла.'

    def load_items(self):
        if Item.objects.exists():
            return

        with open('../data/items.csv', encoding='utf8') as file:
            data = csv.reader(file)
            for row in data:
                Item.objects.create(
                    name=row[0],
                    description=row[1],
                    price=row[2],
                    currency=row[-1]
                )

    def handle(self, *args, **kwargs):
        self.load_items()
