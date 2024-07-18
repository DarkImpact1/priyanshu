import subprocess
def clone_repo(repo_url):
    try:
        subprocess.run(['git', 'clone', repo_url], check=True)
        print(f"Repository '{repo_url}' cloned successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to clone repository '{repo_url}': {e}")

def push():
    subprocess.run(['git', 'add', '.'])
    subprocess.run(['git', 'commit', '-m', 'Update'])
    subprocess.run(['git', 'remote', 'add', 'https://github.com/priyanshuthakran1/cipher_mern_stack.git'])
    subprocess.run(['git', 'push', '-u', 'origin','main'])
    print("Repository pushed successfully.")


urls = ['https://github.com/priyanshuthakran1/Lecture-51-CipherSchools-P-B']

# for url in urls:
#     clone_repo(url)
push()