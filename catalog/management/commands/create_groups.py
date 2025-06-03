from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from catalog.models import Product
from django.contrib.contenttypes.models import ContentType


class Command(BaseCommand):
    help = "Создаёт группы и права"

    def handle(self, *args, **kwargs):
        # Получаем ContentType для модели Product
        content_type = ContentType.objects.get_for_model(Product)

        # Создаём/получаем группу "Модератор продуктов"
        moderator_group, created = Group.objects.get_or_create(name="Модератор продуктов")

        # Права: удаление и отмена публикации
        can_delete = Permission.objects.get(codename="delete_product")
        can_unpublish, _ = Permission.objects.get_or_create(
            codename="can_unpublish_product",
            name="Может отменить публикацию товара",
            content_type=content_type
        )

        moderator_group.permissions.set([can_delete, can_unpublish])
        moderator_group.save()

        self.stdout.write(self.style.SUCCESS("Группа 'Модератор продуктов' успешно создана и настроена"))

