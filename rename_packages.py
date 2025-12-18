"""
Rename packages to unique PyPI names
"""
import os
import shutil
from pathlib import Path

# Mapping of old names to new unique names
RENAMES = {
    "logfmt": "pylogfmt-rj",
    "cachely": "pycachely-rj",  
    "retryit": "pyretryit-rj",
    "validdict": "pyvaliddict-rj",
    "timefunc": "pytimefunc-rj",
    "cliprog": "pycliprog-rj",
    "pyprojectcheck": "pyprojectcheck-rj"
}

def rename_package(old_name, new_name):
    """Rename a package directory and update its configuration"""
    packages_dir = Path("packages")
    old_dir = packages_dir / old_name
    new_dir = packages_dir / new_name
    
    if not old_dir.exists():
        print(f"❌ {old_name} doesn't exist")
        return
    
    # Rename directory
    old_dir.rename(new_dir)
    print(f"📁 Renamed {old_name} -> {new_name}")
    
    # Update pyproject.toml
    toml_file = new_dir / "pyproject.toml"
    if toml_file.exists():
        content = toml_file.read_text()
        content = content.replace(f'name = "{old_name}"', f'name = "{new_name}"')
        toml_file.write_text(content)
        print(f"✅ Updated {new_name}/pyproject.toml")

def main():
    for old, new in RENAMES.items():
        rename_package(old, new)
    
    print("\n✅ All packages renamed!")
    print("Now update publish_packages.py with the new names.")

if __name__ == "__main__":
    main()
