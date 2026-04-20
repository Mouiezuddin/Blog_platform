"""
Setup script: Creates superuser and seeds sample data.
Run: python setup_data.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'developer_tale.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Category, Post
from users.models import Profile

# Create superuser
print("Creating superuser...")
if not User.objects.filter(username='admin').exists():
    admin = User.objects.create_superuser('admin', 'admin@developerstale.com', 'admin123')
    Profile.objects.get_or_create(user=admin, defaults={
        'bio': 'Platform administrator and developer',
        'github': 'developerstale',
        'skills': 'Python, Django, JavaScript, DevOps',
    })
    print("[OK] Superuser created: admin / admin123")
else:
    print("[--] Superuser already exists")

# Create categories
print("\nCreating categories...")
categories_data = [
    {'name': 'Python', 'color': '#3b82f6', 'icon': 'code', 'description': 'Python programming tutorials and tips'},
    {'name': 'Django', 'color': '#10b981', 'icon': 'web', 'description': 'Django framework guides and best practices'},
    {'name': 'JavaScript', 'color': '#f59e0b', 'icon': 'javascript', 'description': 'JavaScript and web development'},
    {'name': 'DevOps', 'color': '#ef4444', 'icon': 'settings', 'description': 'Docker, CI/CD, deployment guides'},
    {'name': 'AI & ML', 'color': '#8b5cf6', 'icon': 'psychology', 'description': 'Machine learning and AI articles'},
    {'name': 'React', 'color': '#06b6d4', 'icon': 'html', 'description': 'React.js tutorials and patterns'},
    {'name': 'Database', 'color': '#f97316', 'icon': 'storage', 'description': 'SQL, NoSQL, and data management'},
    {'name': 'Career', 'color': '#ec4899', 'icon': 'work', 'description': 'Developer career and productivity tips'},
]

cats = {}
for cat_data in categories_data:
    cat, created = Category.objects.get_or_create(name=cat_data['name'], defaults=cat_data)
    cats[cat.name] = cat
    print(f"  {'✅' if created else 'ℹ️ '} {cat.name}")

# Create demo user
print("\nCreating demo user...")
if not User.objects.filter(username='johndoe').exists():
    demo = User.objects.create_user('johndoe', 'john@example.com', 'password123',
                                    first_name='John', last_name='Doe')
    Profile.objects.get_or_create(user=demo, defaults={
        'bio': 'Full-stack developer passionate about Python, Django, and clean code.',
        'location': 'San Francisco, CA',
        'github': 'johndoe',
        'twitter': 'johndoe',
        'skills': 'Python, Django, React, PostgreSQL, Docker',
    })
    print("✅ Demo user created: johndoe / password123")
else:
    demo = User.objects.get(username='johndoe')
    print("ℹ️  Demo user already exists")

# Create sample posts
print("\nCreating sample posts...")
sample_posts = [
    {
        'title': 'Getting Started with Django REST Framework',
        'content': '''# Getting Started with Django REST Framework

Django REST Framework (DRF) is a powerful toolkit for building Web APIs in Django. In this tutorial, we'll cover the essentials.

## Installation

```bash
pip install djangorestframework
```

Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

## Creating a Simple API

First, create a serializer:

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at']
```

Then create a view:

```python
from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

## Conclusion

DRF makes building APIs with Django extremely easy. The combination of serializers, viewsets, and routers gives you a powerful, flexible toolkit.
''',
        'excerpt': 'Learn how to build powerful REST APIs with Django REST Framework in this comprehensive tutorial.',
        'category': cats.get('Django'),
        'status': 'published',
        'featured': True,
        'read_time': 8,
        'tags': ['django', 'api', 'python', 'rest'],
    },
    {
        'title': 'Python Type Hints: A Complete Guide',
        'content': '''# Python Type Hints: A Complete Guide

Type hints in Python make your code more readable and help catch bugs early. Let's explore them.

## Basic Type Hints

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def add(a: int, b: int) -> int:
    return a + b
```

## Complex Types

```python
from typing import List, Dict, Optional, Union

def process_items(items: List[str]) -> Dict[str, int]:
    return {item: len(item) for item in items}

def find_user(user_id: Optional[int] = None) -> Optional[str]:
    if user_id is None:
        return None
    return f"User {user_id}"
```

## Using TypedDict

```python
from typing import TypedDict

class UserProfile(TypedDict):
    name: str
    age: int
    email: str
```

Type hints are optional at runtime but incredibly valuable for development!
''',
        'excerpt': 'Master Python type hints and improve your code quality with static type checking.',
        'category': cats.get('Python'),
        'status': 'published',
        'featured': True,
        'read_time': 6,
        'tags': ['python', 'typing', 'best-practices'],
    },
    {
        'title': 'Docker for Developers: From Zero to Hero',
        'content': '''# Docker for Developers: From Zero to Hero

Docker has revolutionized how we build and deploy applications. Here's everything you need to know.

## What is Docker?

Docker is a platform that packages your application and its dependencies into a **container** — a lightweight, portable unit.

## Basic Commands

```bash
# Pull an image
docker pull python:3.11

# Run a container
docker run -it python:3.11 bash

# List running containers
docker ps

# Build from Dockerfile
docker build -t myapp .
```

## Writing a Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

## Docker Compose

```yaml
version: '3.8'
services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://postgres:password@db:5432/mydb
  db:
    image: postgres:15
    environment:
      POSTGRES_PASSWORD: password
```

Start everything with:
```bash
docker-compose up -d
```
''',
        'excerpt': 'Learn Docker from scratch with practical examples - containerize your first app today.',
        'category': cats.get('DevOps'),
        'status': 'published',
        'featured': True,
        'read_time': 12,
        'tags': ['docker', 'devops', 'containers', 'deployment'],
    },
]

for post_data in sample_posts:
    tags = post_data.pop('tags', [])
    if not Post.objects.filter(title=post_data['title']).exists():
        post = Post.objects.create(author=demo, **post_data)
        post.tags.add(*tags)
        print(f"  ✅ Created: {post.title}")
    else:
        print(f"  ℹ️  Post exists: {post_data['title']}")

print("\n" + "="*50)
print("✅ Setup complete!")
print("="*50)
print(f"\n🌐 Run: python manage.py runserver")
print(f"📚 Visit: http://localhost:8000")
print(f"🔧 Admin: http://localhost:8000/admin")
print(f"   Username: admin")
print(f"   Password: admin123")
