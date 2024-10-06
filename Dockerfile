# Образ Python
FROM python:3.10.0
LABEL authors="Пользователь"

SHELL ["/bin/bash", "-c"]

# Рабочая директория
WORKDIR /carReviews

# Переменные окружения для Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Копирование файла зависимостей и устанавка зависимости
COPY requirements.txt /carReviews/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Копирование всех файлов проекта в контейнер
COPY . /carReviews/

# Порт
EXPOSE 8000

# Команда для запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

#ENTRYPOINT ["top", "-b"]

# Настройка записи и доступа
RUN chmod -R 777 ./