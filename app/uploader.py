from github import Github
from datetime import datetime

access_token = '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'
repository_name = 'aMirMOsavi'
file_path = "./ss.txt"

g = Github(access_token)
repo = g.get_user().get_repo(repository_name)

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
repo.update_file(file_name, commit_message, content, sha)

file_path = "./sss.txt"

with open(file_path, 'r') as file:
    content = file.read()
    num_lines = len(content.splitlines())

file_name = "server"
file_contents = repo.get_contents(file_name)
sha = file_contents.sha    

commit_message = f"Update at {timee} - {num_lines} server"
repo.update_file(file_name, commit_message, content, sha)

print("File uploaded successfully to GitHub!")
