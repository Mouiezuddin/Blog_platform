import os
import random
import django
from django.utils import timezone
from django.utils.text import slugify

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'developer_tale.settings')
django.setup()

from django.contrib.auth.models import User
from blog.models import Post, Category
from taggit.models import Tag

def seed_posts():
    print("Clearing existing posts and tags...")
    Post.objects.all().delete()
    Tag.objects.all().delete()
    
    print("Ensuring categories exist...")
    categories_data = [
        {'name': 'Python', 'color': '#3b82f6', 'icon': 'code', 'description': 'Python programming tutorials'},
        {'name': 'Django', 'color': '#10b981', 'icon': 'web', 'description': 'Django framework guides'},
        {'name': 'JavaScript', 'color': '#f59e0b', 'icon': 'javascript', 'description': 'Web development'},
        {'name': 'DevOps', 'color': '#ef4444', 'icon': 'settings', 'description': 'Deployment guides'},
        {'name': 'AI & ML', 'color': '#8b5cf6', 'icon': 'psychology', 'description': 'Machine learning articles'},
        {'name': 'React', 'color': '#06b6d4', 'icon': 'html', 'description': 'React.js tutorials'},
        {'name': 'Database', 'color': '#f97316', 'icon': 'storage', 'description': 'SQL and data management'},
        {'name': 'Career', 'color': '#ec4899', 'icon': 'work', 'description': 'Career and productivity'},
    ]
    
    for cat_data in categories_data:
        Category.objects.get_or_create(name=cat_data['name'], defaults=cat_data)
    
    print("Starting unique seeding process...")
    
    users = list(User.objects.all())
    categories = list(Category.objects.all())
    
    if not users:
        print("Error: No users found. Please create a superuser first.")
        return
    if not categories:
        print("Error: Failed to create/find categories.")
        return

    # Handle images safely
    image_dir = 'post_covers'
    media_path = os.path.join('media', image_dir)
    images = []
    
    if os.path.exists(media_path):
        images = [f for f in os.listdir(media_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not images:
        print("Warning: No images found in media/post_covers/. Posts will be created without cover images.")
    else:
        print(f"Found {len(images)} images. Assigning to posts...")
        random.shuffle(images)
    
    tech_topics = [
        ("The Zen of Python: Modern Best Practices", "Exploring the philosophy behind clean Python code and how it applies to today's cloud-native applications."),
        ("React 19: Everything You Need to Know", "A comprehensive guide to the latest experimental features, from Actions to the new Compiler."),
        ("Building a Real-time Chat App with Django Channels", "Learn how to handle WebSockets and asynchronous tasks in your Django project."),
        ("Go vs Rust for System Programming", "We compare the performance, safety, and developer experience of the two titans of modern infra."),
        ("Mastering the Chrome DevTools for Frontend Performance", "Stop guessing why your site is slow. Use these pro tips to find and fix bottlenecks."),
        ("Introduction to Vector Databases in the LLM Era", "Understanding the storage layer of modern AI applications. Pinecone, Milvus, and pgvector."),
        ("The Architecture of a Scalable E-commerce Backend", "How to handle traffic spikes, consistency, and inventory management at scale."),
        ("Deep Dive into TypeScript Decorators", "A look at the new stage 3 decorators and how they simplify your metadata-driven code."),
        ("Securing Your API: Beyond Simple JWTs", "Advanced security patterns including refreshing tokens, scopes, and OIDC."),
        ("Why Svelte might be your next favorite framework", "Simplicity and performance. Discover why developer satisfaction is so high with Svelte."),
        ("Database Indexing: Internal Mechanics and Optimization", "A look under the hood at B-Trees, LSM-Trees, and how they affect your query speed."),
        ("Kubernetes Anti-patterns: What NOT to do", "Real-world stories of K8s deployments gone wrong and lessons learned the hard way."),
        ("Advanced CSS: Beyond the Basics of Grid", "Subgrid, container queries, and the new :has() selector changing web design forever."),
        ("The Future of WebAssembly: System Interface (WASI)", "Running compiled code outside the browser. Is this the end of traditional containers?"),
        ("Effective Error Handling in Distributed Systems", "Circuit breakers, retries with exponential backoff, and observability."),
        ("Building Accessible UIs with ARIA and Semantic HTML", "Making the web usable for everyone is not just a trend—it's a requirement."),
        ("A Developer's Guide to Prompt Engineering", "How to talk to LLMs to get better code, documentation, and architecture advice."),
        ("Testing in Production: The Safe Way to Do It", "Feature flags, canary releases, and robust monitoring strategies."),
        ("Scaling PostgreSQL to Terabytes of Data", "Partitioning, sharding, and managed services. When do you outgrow a single instance?"),
        ("The Impact of Copilot on Junior Developer Careers", "Will AI replace us? A balanced look at the future of entry-level software roles."),
        ("Modern State Management in React", "Zustand, Recoil, or just Context? Navigating the complex ecosystem of UI state."),
        ("Dockerizing Complex Multi-service Applications", "A masterclass on Docker Compose for development and production environments."),
        ("Understanding the Internals of the Linux Kernel", "A high-level look at process management, memory, and the virtual file system."),
        ("The Evolution of GraphQL: 2024 and Beyond", "New standards, federation, and the shift towards client-side efficiency."),
        ("Building a Custom CMS with Python and Wagtail", "Moving beyond simple blogs. Flexible content management for professionals."),
        ("Introduction to Functional Programming in JavaScript", "Immutability, pure functions, and higher-order logic for cleaner code."),
        ("Game Dev for Web Developers: Getting started with Three.js", "Bringing 3D experiences to the browser with modern GPU APIs."),
        ("The Rise of Edge Computing and Serverless 2.0", "Moving logic closer to the user with V8 isolates and global edge networks."),
        ("Advanced SQL: Window Functions and CTEs", "Level up your data analysis skills with these powerful database features."),
        ("Cybersecurity Fundamentals for Web Developers", "OWASP Top 10, XSS, CSRF, and how to defend your application from scratch.")
    ]

    lorem_content_templates = [
        "## Deep Dive\nExploration of core concepts is essential for any modern developer. In this post, we look at the intricate details that make this technology so powerful.",
        "## The Practical Guide\nSetting up a professional environment requires more than just installation. It requires understanding the workflow and the ecosystem.",
        "## Challenges and Solutions\nEvery technology has its drawbacks. We analyze the common pitfalls and provide battle-tested solutions."
    ]

    for i in range(len(tech_topics)):
        title, excerpt = tech_topics[i]
        author = random.choice(users)
        category = random.choice(categories)
        status = 'published'
        featured = (i % 8 == 0) # Every 8th post is featured
        
        # Take the next unique image from the shuffled list if available
        cover_image = None
        if images and i < len(images):
            cover_image = f"{image_dir}/{images[i]}"

        post = Post.objects.create(
            title=title,
            slug=slugify(title) + f"-{random.randint(1000, 9999)}",
            author=author,
            content=f"# {title}\n\n{random.choice(lorem_content_templates)}\n\n### Code Example\n```python\n# Implementation Detail\ndef solve():\n    return 'Success'\n```\n\nThis is unique content for post {i+1}.",
            excerpt=excerpt,
            category=category,
            status=status,
            featured=featured,
            cover_image=cover_image,
            read_time=random.randint(4, 15),
            views=random.randint(100, 8000),
            published_at=timezone.now()
        )
        
        # Add tags
        post.tags.add('tech', slugify(category.name), 'modern', 'guide')

        print(f"Created post {i+1}: {title}")

    print("Unique seeding complete!")

if __name__ == "__main__":
    seed_posts()

