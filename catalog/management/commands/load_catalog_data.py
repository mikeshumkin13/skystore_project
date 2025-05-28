from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Загружает тестовые данные из фикстур"

    def handle(self, *args, **kwargs):
        self.stdout.write("Удаляю существующие данные...")
        Product.objects.all().delete()
        Category.objects.all().delete()

        self.stdout.write("Загружаю новые данные из фикстур...")
        call_command("loaddata", "catalog/fixtures/catalog_data.json")

        self.stdout.write(self.style.SUCCESS("Данные успешно загружены."))
