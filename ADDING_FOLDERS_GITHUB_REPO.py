from pathlib import Path
from git import Repo 

#--- setup ---------------------------------------------------------------
repo_path = Path("/workspaces/MSSP607/")     # path to your local clone
folder     = repo_path/"WeeklyModules/Weekly2"   # folder you want to add
commit_msg = "Add Weekly Module folder with placeholder"

# --- create the folder & placeholder -------------------------------------
folder.mkdir(parents=True, exist_ok=True)
(folder / ".gitkeep").touch()               # ensures Git tracks an empty dir

# --- stage, commit, push --------------------------------------------------
repo = Repo(repo_path)
repo.index.add([str(p.relative_to(repo_path)) for p in folder.rglob("*")])
repo.index.commit(commit_msg)

origin = repo.remote(name="origin")
origin.push()                               # push to the same branch
print("✅ Folder pushed!")