from pathlib import Path
from git import Repo

# Repository root
repo_path = Path("/workspaces/Test")

# Open existing Git repository
repo = Repo(repo_path)

commit_msg = "Create repository folder structure"

# Root folders
root_folders = [
    "WeeklyModules",
    "Assignments",
    "data"
]

# Create root folders and .gitkeep files
for folder in root_folders:
    folder_path = repo_path / folder
    folder_path.mkdir(parents=True, exist_ok=True)

    # Create placeholder file so Git tracks folder
    (folder_path / ".gitkeep").touch(exist_ok=True)

# Weekly module folders
weekly_modules = repo_path / "WeeklyModules"

for week_num in range(1, 15):
    week_folder = weekly_modules / f"Week{week_num:02d}"
    week_folder.mkdir(parents=True, exist_ok=True)

    # Create placeholder file
    (week_folder / ".gitkeep").touch(exist_ok=True)

# Stage all changes
repo.git.add(A=True)

# Commit only if changes exist
if repo.is_dirty(untracked_files=True):
    repo.index.commit(commit_msg)
    print("Changes committed.")
else:
    print("No changes to commit.")

print("Folder structure created successfully!")