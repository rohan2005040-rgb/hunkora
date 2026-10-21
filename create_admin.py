import os
import django

# Django environment setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # আপনার প্রজেক্টের সেটিংস ফাইলের নাম যদি আলাদা হয়, তবে 'config.settings' এর জায়গায় তা বসিয়ে দিন
django.setup()

from django.contrib.auth.models import User

username = 'hunkora22'
# email = 'admin@hunkora.com'
password = 'B452385b#@$'  # আপনার পছন্দমতো একটি পাসওয়ার্ড এখানে লিখে দিন

if not User.objects.filter(username=username).exists():
  User.objects.create_superuser(username, password)
  print(f'Superuser "{username}" created successfully in the Live Database!')
else:
  print(f'Superuser "{username}" already exists!')