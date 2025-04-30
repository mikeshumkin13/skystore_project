echo "# 🛍️ SkyStore

Учебный Django-проект — мини-магазин плагинов и утилит.  
Домашнее задание 21.2 — шаблоны, статика, формы.

## 📦 Функционал
- Главная страница с карточкой продукта
- Страница \"Контакты\" с формой обратной связи
- Обработка POST-запроса и вывод данных в консоль
- Перенаправление на страницу благодарности
- Подключение Bootstrap через статику

## 🗂️ Структура проекта
\`\`\`
skystore_project/
├── catalog/
│   ├── static/                # Bootstrap файлы
│   ├── templates/catalog/     # HTML-шаблоны
│   ├── views.py               # Контроллеры
│   └── urls.py                # Маршруты приложения
├── skystore/
│   ├── settings.py            # Настройки Django
│   └── urls.py                # Главный роутинг
└── manage.py
\`\`\`

## 🚀 Как запустить
\`\`\`bash
pip install -r requirements.txt
python manage.py runserver
\`\`\`

## 🔧 Требования
- Python 3.12
- Django 5.2

---

📝 Задание выполнено в рамках курса SkyPro  
Автор: [@mikeshumkin13](https://github.com/mikeshumkin13)
