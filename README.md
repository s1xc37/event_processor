# Event Processor

## 🚀 Быстрый старт

### 1. Клонирование репозитория

```bash
git clone <repo_url>
cd <project_folder>
```

---

### 2. Запуск инфраструктуры

```bash
docker-compose up -d
```

---

### 3. Проверка контейнеров

```bash
docker ps
```

Ожидаемые сервисы:

* postgres
* kafka
* zookeeper

---

## 🗄️ PostgreSQL

Доступ к базе:

* Host: `localhost`
* Port: `5432`
* User: `user`
* Password: `password`
* Database: `app_db`

---

## 📡 Kafka

* Broker: `localhost:9092`

Можно использовать для продюсинга и консюминга сообщений.

---

## 📦 Зависимости Python

Установка зависимостей:

```bash
pip install -r requirements.txt
```

---

## 📁 Структура проекта

```
project/
│
├── app/                # основной код приложения
├── tests/              # тесты
├── docker/             # docker-конфигурации (если будут)
├── scripts/            # вспомогательные скрипты
│
├── docker-compose.yml
├── requirements.txt
├── README.md
```

---

## 🛠️ Разработка

Рекомендуется использовать виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

---

## 🧹 Остановка сервисов

```bash
docker-compose down
```
