import subprocess
import os
import shutil

def clone_repo(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository '{repo_url}' cloned successfully.")
        repo_name = repo_url.split('/')[-1]
        return repo_name
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository '{repo_url}': {e}")
        return None

def push_changes_to_current_repo(repo_name, current_repo_path):
    try:
        # Copy files from the cloned repo to the current repo
        for item in os.listdir(repo_name):
            source = os.path.join(repo_name, item)
            destination = os.path.join(os.getcwd(), item)
            if os.path.isdir(source):
                shutil.copytree(source, destination, dirs_exist_ok=True)
            else:
                shutil.copy2(source, destination)
        
        # Remove the cloned repository directory
        shutil.rmtree(repo_name)

        # Initialize git in the current directory if not already a git repo
        if not os.path.isdir('.git'):
            subprocess.run(['git', 'init'], check=True)

        subprocess.run(['git', 'remote', 'set-url', 'origin', current_repo_path], check=True)
        subprocess.run(['git', 'add', '.'], check=True)
        subprocess.run(['git', 'commit', '-m', 'Update'], check=True)
        subprocess.run(['git', 'push', 'origin', 'main'], check=True)
        print("Changes pushed successfully to the current repository.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to push changes: {e}")


# Example usage
if __name__ == "__main__":
    urls = ['https://github.com/priyanshuthakran1/Lecture-49-CipherSchools']
    current_repo_path = 'https://github.com/priyanshuthakran1/cipher_mern_stack.git'  # Change this to your current repo path


    for url in urls:
        repo_name = clone_repo(url)
        if repo_name:
            push_changes_to_current_repo(repo_name, current_repo_path)
            print(f"Finished cloning and pushing of {repo_name}")



# ruk ja bhai thodha time lg  rha lekin jld hi kr dunga.. frr bs ek click and task khtm smjha  ok