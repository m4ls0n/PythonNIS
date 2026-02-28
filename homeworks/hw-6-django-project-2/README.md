# HW 6


## Запуск

Теперь и бд, и сам Django-бэкенд запускаются в Docker-контейнерах

1. **Запуск оркестратора:**
   ```bash
   docker-compose up -d --build
   ```

2. **Применение миграций (структура + моки):**
   ```bash
   docker-compose exec backend python manage.py migrate
   ```
   При первой миграции в базу автоматически загрузятся тестовые пользователи, посты и комментарии (Data Migrations)

3. **Создание суперпользователя (по желанию):**
   ```bash
   docker-compose exec backend python manage.py createsuperuser
   ```

API доступен по адресу: `http://127.0.0.1:8000/`

---

## Что реализовано

### 1. Моки 
- Создана Data Migration (0002_create_mock_data.py)
- Автозаполнение базы фейковыми юзерами, постами и комментами при развертывании

### 2. CRUD 
- Написаны ModelSerializer для всех моделей (User, Post, Comment)
- Созданы ModelViewSet для обработки логики запросов
- Настроен DefaultRouter для автоматической генерации URL-путей (/api/users/, /api/posts/, /api/comments/)

### 3. Совершенствование 
- Написан ридми по применению миграций в database/README.md
- Реализованы кастомные методы (actions) во ViewSet'ах:
  - GET /api/users/{id}/stats/ — получение агрегированных данных (колво постов и комментариев пользователя)
  - GET /api/posts/lightweight/ — получение легковесного списка постов (без тяжелого поля text)

### 4. Докеризация Бэкенда (1 балл)
- Написан Dockerfile для Django-приложения
- Обновлен docker-compose.yml: добавлены сервисы db и backend, настроена связь между ними (depends_on)
- Настроено подключение Django к PostgreSQL внутри сети Docker