"""
Developers Tale - One-Click Local Setup Script
Run:  python setup.py
"""

import os
import sys
import subprocess
import shutil


def run(cmd, check=True):
    print(f"\n>> {cmd}")
    result = subprocess.run(cmd, shell=True, check=check)
    return result


def main():
    print("=" * 60)
    print("   Developers Tale - Local Setup")
    print("=" * 60)

    # 1. Check Python version
    if sys.version_info < (3, 10):
        print("❌  Python 3.10 or higher is required.")
        sys.exit(1)
    print(f"✅  Python {sys.version.split()[0]} detected.")

    # 2. Create virtual environment if not exists
    if not os.path.exists("venv"):
        print("\n📦  Creating virtual environment...")
        run(f"{sys.executable} -m venv venv")
    else:
        print("✅  Virtual environment already exists.")

    # 3. Determine pip/python paths inside venv
    if sys.platform == "win32":
        pip = os.path.join("venv", "Scripts", "pip")
        python = os.path.join("venv", "Scripts", "python")
    else:
        pip = os.path.join("venv", "bin", "pip")
        python = os.path.join("venv", "bin", "python")

    # 4. Install dependencies
    print("\n📥  Installing dependencies from requirements.txt...")
    run(f"{pip} install -r requirements.txt")

    # 5. Create .env if it doesn't exist
    if not os.path.exists(".env"):
        if os.path.exists(".env.example"):
            shutil.copy(".env.example", ".env")
            print("\n✅  Created .env from .env.example")
        else:
            # Write a default .env
            with open(".env", "w") as f:
                f.write("SECRET_KEY=django-insecure-local-dev-key-change-me\n")
                f.write("DEBUG=True\n")
                f.write("ALLOWED_HOSTS=localhost,127.0.0.1\n")
            print("\n✅  Created default .env file.")
    else:
        print("✅  .env file already exists.")

    # 6. Run migrations
    print("\n🗄️  Running database migrations...")
    run(f"{python} manage.py migrate")

    # 7. Create superuser (optional)
    print("\n" + "=" * 60)
    create_super = input("👤  Create a superuser (admin) account? [y/N]: ").strip().lower()
    if create_super == "y":
        run(f"{python} manage.py createsuperuser", check=False)

    # 8. Seed sample data (optional)
    if os.path.exists("seed_posts.py"):
        print("\n" + "=" * 60)
        seed = input("🌱  Seed sample blog posts? [y/N]: ").strip().lower()
        if seed == "y":
            run(f"{python} seed_posts.py", check=False)

    # 9. Done
    print("\n" + "=" * 60)
    print("🎉  Setup complete!")
    print("\nTo start the development server, run:")
    if sys.platform == "win32":
        print("   venv\\Scripts\\python manage.py runserver")
    else:
        print("   source venv/bin/activate && python manage.py runserver")
    print("\nThen open: http://127.0.0.1:8000")
    print("Admin panel: http://127.0.0.1:8000/admin")
    print("=" * 60)


if __name__ == "__main__":
    main()
