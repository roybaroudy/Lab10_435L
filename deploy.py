import os
import shutil
import subprocess
import sys

# Configuration
LOCAL_DEPLOY_DIR = "C:\\Users\\royba\\Downloads\\deploy"  # change for local deployment
REMOTE_USER = "username"                        # remote server username
REMOTE_HOST = "example.com"                     # remote server address
REMOTE_DIR = "/home/username/myapp"            # remote path
USE_REMOTE = False                              # Set True to deploy remotely

def deploy_local():
    if not os.path.exists(LOCAL_DEPLOY_DIR):
        os.makedirs(LOCAL_DEPLOY_DIR)
    # Copy files to local deployment directory
    for item in os.listdir("."):
        if item not in [LOCAL_DEPLOY_DIR, ".git", "venv"]:
            src = os.path.join(".", item)
            dst = os.path.join(LOCAL_DEPLOY_DIR, item)
            if os.path.isdir(src):
                shutil.copytree(src, dst, dirs_exist_ok=True)
            else:
                shutil.copy2(src, dst)
    print(f"Application deployed locally to {LOCAL_DEPLOY_DIR}")

def deploy_remote():
    print(f"Deploying to {REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}")
    # Copy files using scp
    subprocess.run([
        "scp", "-r", "./*", f"{REMOTE_USER}@{REMOTE_HOST}:{REMOTE_DIR}"
    ])
    # Optional: restart service or run commands on remote server
    subprocess.run([
        "ssh", f"{REMOTE_USER}@{REMOTE_HOST}", "echo 'Deployment complete!'"
    ])
    print("Remote deployment finished.")

if __name__ == "__main__":
    if USE_REMOTE:
        deploy_remote()
    else:
        deploy_local()