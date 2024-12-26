from github import Github
import random
import os
import time

# Configuration
TOKEN = "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"
REPO_NAME = "R1SH4BH81/redesign"
FILE_PATH = "auto.md"  # File to edit
COMMIT_MESSAGE = " update for in auto.md"

# Initialize GitHub API
g = Github(TOKEN)
repo = g.get_repo(REPO_NAME)

def get_file_contents(repo, path):
    """Fetch the file contents from the repository."""
    file = repo.get_contents(path)
    return file.decoded_content.decode(), file.sha

def make_random_changes(content):
    """Modify the content randomly."""
    lines = content.splitlines()
    if lines:
        random_line = random.randint(0, len(lines) - 1)
        lines[random_line] += " 🌟"  # Add a star emoji to a random line
    else:
        lines.append("Random Contribution!")
    return "\n".join(lines)

def update_file(repo, path, content, sha):
    """Update the file with new content."""
    repo.update_file(
        path,
        COMMIT_MESSAGE,
        content,
        sha,
        branch="main"  # Ensure you're working on the correct branch
    )
    print(f"Updated {path} successfully!")

if __name__ == "__main__":
    try:
        # Fetch current file content
        content, sha = get_file_contents(repo, FILE_PATH)
        
        # Make random changes
        updated_content = make_random_changes(content)
        
        # Update the file
        update_file(repo, FILE_PATH, updated_content, sha)
        
        print("Contribution made successfully!")
    except Exception as e:
        print(f"Error: {e}")
