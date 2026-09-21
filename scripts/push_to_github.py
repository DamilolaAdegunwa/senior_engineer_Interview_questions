#!/usr/bin/env python3
"""
Script to create the remote GitHub repo and push to it.
Uses credentials stored in ~/.git-credentials.
Supports unverified SSL context or curl for macOS CA trust issues.
"""

import os
import sys
import json
import ssl
import urllib.request
import urllib.error
import subprocess

REPO_NAME = "senior_engineer_Interview_questions"
REPO_DESC = "10,000 Senior Engineer Interview Questions — An O'Reilly-Style Field Manual for Staff, Principal, and Senior Infrastructure Engineers"

# Create SSL context that falls back gracefully
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_github_token():
    creds_path = os.path.expanduser("~/.git-credentials")
    if not os.path.exists(creds_path):
        print(f"Credentials file not found at {creds_path}")
        return None, None
    with open(creds_path) as f:
        for line in f:
            if "github.com" in line:
                # format: https://user:token@github.com or https://token@github.com
                part = line.strip().split("@github.com")[0].split("//")[-1]
                if ":" in part:
                    user, token = part.split(":", 1)
                    return user, token
                return None, part
    return None, None

def create_remote_repo(token):
    url = "https://api.github.com/user/repos"
    payload = json.dumps({
        "name": REPO_NAME,
        "description": REPO_DESC,
        "private": False,
        "has_issues": True,
        "has_projects": True,
        "has_wiki": True
    }).encode("utf-8")
    
    req = urllib.request.Request(url, data=payload, method="POST")
    req.add_header("Authorization", f"token {token}")
    req.add_header("Accept", "application/vnd.github.v3+json")
    req.add_header("User-Agent", "Python-GitHub-Creator")
    
    try:
        with urllib.request.urlopen(req, context=ctx) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            print(f"Successfully created remote repository: {data.get('html_url')}")
            return data.get("clone_url"), data.get("html_url")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8")
        if e.code == 422: # Repo may already exist
            print(f"Repository {REPO_NAME} may already exist: {body}")
            user_req = urllib.request.Request("https://api.github.com/user")
            user_req.add_header("Authorization", f"token {token}")
            user_req.add_header("User-Agent", "Python-GitHub-Creator")
            with urllib.request.urlopen(user_req, context=ctx) as user_resp:
                user_data = json.loads(user_resp.read().decode("utf-8"))
                username = user_data["login"]
                clone_url = f"https://github.com/{username}/{REPO_NAME}.git"
                html_url = f"https://github.com/{username}/{REPO_NAME}"
                return clone_url, html_url
        else:
            print(f"Failed to create repo via API (HTTP {e.code}): {body}")
            raise

def main():
    user, token = get_github_token()
    if not token:
        print("Could not locate GitHub token in ~/.git-credentials.")
        sys.exit(1)
        
    print(f"Detected GitHub user/token for authentication.")
    clone_url, html_url = create_remote_repo(token)
    print(f"Target repository URL: {html_url}")
    
    # Configure git remote
    remote_target = f"https://{token}@github.com/{user}/{REPO_NAME}.git" if user else f"https://{token}@github.com/{REPO_NAME}.git"
    
    # Check current remote
    remotes = subprocess.run(["git", "remote"], capture_output=True, text=True).stdout.split()
    if "origin" in remotes:
        subprocess.run(["git", "remote", "remove", "origin"], check=True)
        
    subprocess.run(["git", "remote", "add", "origin", remote_target], check=True)
    print("Added git remote origin.")
    
    print("Pushing to GitHub (main branch)...")
    push_res = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True)
    if push_res.returncode != 0:
        print(f"Push failed: {push_res.stderr}")
        # Try pushing with force or standard
        sys.exit(push_res.returncode)
        
    print("Push completed successfully!")
    
    # Clean remote to standard URL without embedding token in git config
    clean_url = f"https://github.com/{user}/{REPO_NAME}.git" if user else html_url + ".git"
    subprocess.run(["git", "remote", "set-url", "origin", clean_url], check=True)
    print(f"Remote reset to clean URL: {clean_url}")
    print(f"\nFinal Repository Link: {html_url}\n")

if __name__ == "__main__":
    main()
