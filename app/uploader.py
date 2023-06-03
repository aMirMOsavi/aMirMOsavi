import requests
from github import Github
from datetime import datetime
import base64

access_token = ''
repository_name = 'aMirMOsavi'


print("Requesting...")

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)



file_path = "./ss.txt"


with open(file_path, 'r') as file:
    content = file.read()
    num_lines = len(content.splitlines())

now = datetime.now()
current_time = now.strftime("%H:%M")
timee=str(current_time)

file_name = "Server"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha

commit_message = f"Update at {timee} - {num_lines} Server"
print(f"Uploading {file_path} as {file_name} - {num_lines} server")
repo.update_file(file_name, commit_message, content, sha)

print(f"{file_path} Uploaded.")
print(f"--------------------")

file_path = "./sss.txt"


with open(file_path, 'r') as file:
    content = file.read()
    num_lines = len(content.splitlines())

file_name = "server"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha    

commit_message = f"Update at {timee} - {num_lines} server"
print(f"Uploading {file_path} as {file_name} - {num_lines} server")
repo.update_file(file_name, commit_message, content, sha)

print(f"{file_path} Uploaded.")
print(f"--------------------")

file_path = "./All_Configs_Sub.txt"


with open(file_path, 'r') as file:
    content = file.read()
    num_lines = len(content.splitlines())

file_name = "allsub"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha    

commit_message = f"Update at {timee} - {num_lines} server"
print(f"Uploading {file_path} as {file_name} - {num_lines} server")

# Encode content as base64
content_base64 = base64.b64encode(content.encode()).decode()

# Prepare the request payload
data = {
    "message": commit_message,
    "content": content_base64,
    "sha": sha
}

# Set the timeout value in seconds
timeout = 60

# Send the request with timeout
response = requests.put(
    f"https://api.github.com/repos/{repository_name}/{repository_name}/contents/{file_name}",
    headers={"Authorization": f"Bearer {access_token}"},
    json=data,
    timeout=timeout
)

if response.status_code == 200:
    print(f"{file_path} Uploaded.")
else:
    print(f"Failed - Error: {response.text}")


print("Upload successfully!")
