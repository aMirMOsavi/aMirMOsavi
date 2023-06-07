import requests
from github import Github
from datetime import datetime
import base64
import shutil
import re
import os

repository_name = 'aMirMOsavi'


# کپی کردن فایل
shutil.copy2('./uploader.py', './uploader_copy.py')
shutil.copy2('./App uploader.py', './App_uploader_copy.py')

print("Removing Access_token In Python File...")

# ویرایش فایل کپی شده
with open('uploader_copy.py', 'r') as file:
    content = file.read()
# حذف مقدار access_token
content = re.sub(r"access_token\s*=\s*'.*'", "access_token = ''", content)
# ذخیره فایل با تغییرات
with open('uploader_copy.py', 'w') as file:
    file.write(content)


# ویرایش فایل کپی شده
with open('App_uploader_copy.py', 'r', encoding='utf-8') as file:
    content = file.read()
# حذف مقدار access_token
content = re.sub(r"access_token\s*=\s*'.*'", "access_token = ''", content)
# ذخیره فایل با تغییرات
with open('App_uploader_copy', 'w', encoding='utf-8') as file:
    file.write(content)



print("Connecting To Github...")

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)


file_path = "./get.py"

with open(file_path, 'r') as file:
    content = file.read()

now = datetime.now()
current_time = now.strftime("%H:%M")
timee=str(current_time)

file_name = "app/get.py"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha

commit_message = f"Update at {timee}"
print(f"Uploading {file_path} as {file_name}")
repo.update_file(file_name, commit_message, content, sha)

print(f"{file_path} Uploaded.")
print(f"--------------------")

file_path = "./uploader_copy.py"

with open(file_path, 'r') as file:
    content = file.read()

now = datetime.now()
current_time = now.strftime("%H:%M")
timee=str(current_time)

file_name = "app/uploader.py"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha

commit_message = f"Update at {timee}"
print(f"Uploading {file_path} as {file_name}")
repo.update_file(file_name, commit_message, content, sha)

print(f"{file_path} Uploaded.")
print(f"--------------------")


file_path = "./App_uploader_copy.py"

with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

now = datetime.now()
current_time = now.strftime("%H:%M")
timee=str(current_time)

file_name = "app/App uploader.py"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha

commit_message = f"Update at {timee}"
print(f"Uploading {file_path} as {file_name}")
repo.update_file(file_name, commit_message, content, sha)

print(f"{file_path} Uploaded.")


print("Upload successfully!")



# پاک کردن فایل کپی شده
print("Deleting Temp File...")
os.remove('uploader_copy.py')
os.remove('App_uploader_copy.py')
print("Done ._.")
