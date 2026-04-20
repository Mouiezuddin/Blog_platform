# 🚀 Developers Tale - Modern Blog Platform

[![Django Version](https://img.shields.io/badge/Django-5.2+-green.svg)](https://www.djangoproject.com/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-3.0+-blue.svg)](https://tailwindcss.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Developers Tale** is a premium, developer-focused blog platform designed for technical storytelling. It combines a sleek, modern UI with powerful features like Markdown support, code syntax highlighting, and a robust community system.

---

## ✨ Key Features

### 📝 Content Creation
- **Rich Markdown Editor**: Write effortlessly with the integrated **EasyMDE** editor.
- **Code Syntax Highlighting**: Automatic highlighting for over 100 languages using `highlight.js`.
- **Dynamic Previews**: See exactly how your post looks before publishing.
- **Image Uploads**: Custom cover images for every post.

### 👥 Community & Social
- **User Profiles**: Showcase your skills, GitHub, and social links.
- **Follow System**: Stay updated with your favorite technical authors.
- **Interactions**: Like posts, bookmark for later, and join the conversation with nested comments.
- **Sharing**: One-click URL copying for easy social sharing.

### 🛠️ Developer Experience
- **RESTful API**: Full API support using **Django REST Framework** (`/api/posts/`).
- **One-Click Setup**: Includes a `setup.py` script for automated environment configuration.
- **Advanced Search**: Filter by categories, tags, or full-text query.
- **Analytics**: Personal dashboard to track views, likes, and engagement.

---

## 📸 Screen Previews

| Home Page | Post View | Dashboard |
| :--- | :--- | :--- |
| ![Home](https://raw.githubusercontent.com/Mouiezuddin/Blog_platform/main/static/img/preview_home.png) | ![Post](https://raw.githubusercontent.com/Mouiezuddin/Blog_platform/main/static/img/preview_post.png) | ![Dashboard](https://raw.githubusercontent.com/Mouiezuddin/Blog_platform/main/static/img/preview_dashboard.png) |
> *Note: Add your own screenshots to the `static/img/` folder to display here.*

---

## 🚀 Quick Start (Local Setup)

### Prerequisites
- **Python 3.10+**
- **Git**

### Installation Steps

1. **Clone & Enter**:
   ```bash
   git clone https://github.com/Mouiezuddin/Blog_platform.git
   cd Blog_platform
   ```

2. **Automated Setup**:
   Run our "One-Click" setup script which handles venv, dependencies, and database migrations:
   ```bash
   python setup.py
   ```

3. **Launch**:
   ```bash
   # Windows
   venv\Scripts\python manage.py runserver
   
   # Linux / Mac
   source venv/bin/activate
   python manage.py runserver
   ```
   Explore at: `http://127.0.0.1:8000`

---

## 📂 Project Structure

```text
.
├── blog/             # Core blog logic (Posts, Categories, Likes)
├── users/            # Authentication & User Profiles
├── comments/         # Nested comment system
├── developer_tale/   # Project configuration & settings
├── static/           # UI Assets (CSS, JS, Images)
├── templates/        # HTML Layouts (Tailwind CSS)
├── media/            # Uploaded cover images & avatars
├── setup.py          # Automated installation script
└── manage.py         # Django CLI
```

---

## 🛠️ Tech Stack

- **Backend**: Python 🐍, Django 5.2
- **Frontend**: Tailwind CSS 🎨, JavaScript (Vanilla ES6)
- **Database**: SQLite (Development) / PostgreSQL (Production ready)
- **APIs**: Django REST Framework
- **Tools**: WhiteNoise (Static serving), Python-Decouple (Config management)

---

## 📡 API Documentation

Access the API endpoints at `/api/`:
- `GET /api/posts/` - List all published posts
- `GET /api/posts/<slug>/` - Retrieve post details
- `GET /api/categories/` - List all available categories

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See `LICENSE` for more information.

---

## ✉️ Contact

**Author Name** - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Project Link: [https://github.com/Mouiezuddin/Blog_platform](https://github.com/Mouiezuddin/Blog_platform)

---
<p align="center">Made with ❤️ for the Developer Community</p>
