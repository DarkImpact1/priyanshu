import os
import shutil
import git

# List of repository URLs
repository_urls = [
    "https://github.com/priyanshuthakran1/Lecture-46-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-47-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-48-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-49-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-50-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-51-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-52-CipherSchools",
    "https://github.com/priyanshuthakran1/Lecture-53-CipherSchools",
]

# Directory of the current working repository
current_repo_path = 'C:/Users/sony/Desktop/priyanshu'
cloning_path = 'C:/Users/sony/Desktop/priyanshu/temp_cloning_dir'  # Temporary path for cloning

# Ensure the cloning path exists
os.makedirs(cloning_path, exist_ok=True)

# Function to copy contents excluding .git directory
def copy_contents(src, dest):
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            if item != '.git':  # Skip .git directories
                shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            shutil.copy2(s, d)

# Clone each repository into the temporary directory and copy contents
for url in repository_urls:
    repo_name = url.split('/')[-1]
    temp_clone_path = os.path.join(cloning_path, repo_name)
    final_clone_path = os.path.join(current_repo_path, repo_name)

    # Clone the repo to the temporary directory
    git.Repo.clone_from(url, temp_clone_path)
    
    # Ensure the final directory exists
    os.makedirs(final_clone_path, exist_ok=True)
    
    # Copy the contents to the final directory in the current repo
    copy_contents(temp_clone_path, final_clone_path)


# Commit and push the changes to your current repository
repo = git.Repo(current_repo_path)
repo.git.add(A=True)
repo.index.commit("Added sub-repositories with contents")
origin = repo.remote(name='origin')
origin.push()
