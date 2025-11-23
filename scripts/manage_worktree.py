import argparse
import subprocess
import sys
from pathlib import Path


def run_command(command, cwd=None):
    try:
        result = subprocess.run(
            command, cwd=cwd, check=True, text=True, capture_output=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error running command: {' '.join(command)}")
        print(f"Stderr: {e.stderr}")
        sys.exit(1)


def create_worktree(branch_name):
    project_root = Path(__file__).parent.parent
    worktrees_dir = project_root / ".worktrees"
    worktree_path = worktrees_dir / branch_name

    if worktree_path.exists():
        print(f"Worktree already exists at {worktree_path}")
        return

    print(f"Creating worktree for branch '{branch_name}' at {worktree_path}...")

    # Create the directory if it doesn't exist (git worktree add will create the leaf dir, but good to be safe with parents)
    worktrees_dir.mkdir(exist_ok=True)

    # Check if branch exists
    try:
        run_command(
            ["git", "show-ref", "--verify", f"refs/heads/{branch_name}"],
            cwd=project_root,
        )
        branch_exists = True
    except SystemExit:
        branch_exists = False

    cmd = ["git", "worktree", "add"]
    if not branch_exists:
        cmd.extend(["-b", branch_name])

    cmd.append(str(worktree_path))
    if branch_exists:
        cmd.append(branch_name)

    run_command(cmd, cwd=project_root)
    print(f"Successfully created worktree at {worktree_path}")


def list_worktrees():
    project_root = Path(__file__).parent.parent
    output = run_command(["git", "worktree", "list"], cwd=project_root)
    print(output)


def main():
    parser = argparse.ArgumentParser(description="Manage git worktrees for agents.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("create", help="Create a new worktree")
    create_parser.add_argument("branch_name", help="Name of the branch/worktree")

    list_parser = subparsers.add_parser("list", help="List existing worktrees")

    args = parser.parse_args()

    if args.command == "create":
        create_worktree(args.branch_name)
    elif args.command == "list":
        list_worktrees()


if __name__ == "__main__":
    main()
