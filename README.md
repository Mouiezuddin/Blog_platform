# Developers Tale 🚀

A modern, developer-focused blog platform built with Django.

## Features
- 📝 **Markdown Editor**: Write posts using EasyMDE with syntax highlighting.
- 🎨 **Responsive UI**: Built with Tailwind CSS and Material Design aesthetics.
- 👤 **User Profiles**: Manage your profile, bio, and social links.
- 💬 **Interactions**: Like, bookmark, and comment on posts.
- 🔍 **Search**: Find content by tags, categories, or keywords.
- 📊 **Dashboard**: Analytics for your posts.
- 🛡️ **Authentication**: Secure registration and login.

## Quick Setup

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd Developer_tale
   ```

2. **Run the setup script**:
   ```bash
   python setup.py
   ```
   *This will create a virtual environment, install dependencies, and set up the database.*

3. **Run the server**:
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` in your browser.

## Tech Stack
- **Framework**: Django
- **Styling**: Tailwind CSS
- **Database**: SQLite (default)
- **API**: Django REST Framework
- **Others**: WhiteNoise, Crispy Forms, EasyMDE
