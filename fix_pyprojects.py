"""
Fix pyproject.toml files to include explicit package paths
"""
from pathlib import Path

# Mapping of new package names to their src folder names
PACKAGES = {
    "pylogfmt-rj": "logfmt",
    "pycachely-rj": "cachely",
    "pyretryit-rj": "retryit",
    "pyvaliddict-rj": "validdict",
    "pytimefunc-rj": "timefunc",
    "pycliprog-rj": "cliprog",
    "pyprojectcheck-rj": "pyprojectcheck"
}

def fix_pyproject(pkg_dir_name, src_folder_name):
    """Add hatch build config to pyproject.toml"""
    toml_file = Path("packages") / pkg_dir_name / "pyproject.toml"
    
    if not toml_file.exists():
        print(f"❌ {toml_file} not found")
        return
    
    content = toml_file.read_text()
    
    # Check if already has build config
    if "[tool.hatch.build.targets.wheel]" in content:
        print(f"⏭️  {pkg_dir_name} already has build config")
        return
    
    # Add the build config at the end
    build_config = f'''

[tool.hatch.build.targets.wheel]
packages = ["src/{src_folder_name}"]
'''
    
    content += build_config
    toml_file.write_text(content)
    print(f"✅ Fixed {pkg_dir_name}/pyproject.toml")

def main():
    for pkg_dir, src_folder in PACKAGES.items():
        fix_pyproject(pkg_dir, src_folder)
    
    print("\n✅ All pyproject.toml files fixed!")

if __name__ == "__main__":
    main()
