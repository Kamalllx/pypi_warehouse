"""
Script to publish PyPI Warehouse packages to PyPI
Publishes each package individually with proper error handling
"""

import subprocess
import sys
from pathlib import Path

# IMPORTANT: Set your PyPI API token here or via environment variable
# Get your token from: https://pypi.org/manage/account/token/
PYPI_TOKEN = "YOUR_PYPI_TOKEN_HERE"  # Replace with your actual token

PACKAGES = [
    "envmaster",
    "pylogfmt-rj",
    "pycachely-rj",
    "pyretryit-rj",
    "pyvaliddict-rj",
    "pytimefunc-rj",
    "pycliprog-rj",
    "pyprojectcheck-rj"
]

def publish_package(package_name):
    """Build and publish a single package to PyPI"""
    package_dir = Path("packages") / package_name
    
    if not package_dir.exists():
        print(f"❌ Package directory not found: {package_dir}")
        return False
    
    print(f"\n{'='*60}")
    print(f"📦 Publishing: {package_name}")
    print(f"{'='*60}\n")
    
    try:
        # Clean previous builds
        dist_dir = package_dir / "dist"
        if dist_dir.exists():
            import shutil
            shutil.rmtree(dist_dir)
            print("🧹 Cleaned old build artifacts")
        
        # Build the package
        print("🔨 Building package...")
        result = subprocess.run(
            [sys.executable, "-m", "build"],
            cwd=package_dir,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            print(f"❌ Build failed:\n{result.stderr}")
            return False
        
        print("✅ Build successful!")
        
        # Upload to PyPI
        print("📤 Uploading to PyPI...")
        
        # Check if using token or username/password
        if PYPI_TOKEN and PYPI_TOKEN != "YOUR_PYPI_TOKEN_HERE":
            upload_result = subprocess.run(
                [
                    sys.executable, "-m", "twine", "upload",
                    "--username", "__token__",
                    "--password", PYPI_TOKEN,
                    "dist/*"
                ],
                cwd=package_dir,
                capture_output=True,
                text=True
            )
        else:
            print("\n⚠️  No API token configured. Using interactive login:")
            upload_result = subprocess.run(
                [sys.executable, "-m", "twine", "upload", "dist/*"],
                cwd=package_dir
            )
        
        if upload_result.returncode != 0:
            if "already exists" in upload_result.stderr.lower():
                print(f"⚠️  Package already exists on PyPI (possibly older version)")
            else:
                print(f"❌ Upload failed:\n{upload_result.stderr}")
                return False
        
        print(f"✅ {package_name} published successfully!")
        print(f"🔗 https://pypi.org/project/{package_name}/")
        return True
        
    except Exception as e:
        print(f"❌ Error publishing {package_name}: {e}")
        return False

def main():
    """Publish all packages"""
    print("🚀 PyPI Warehouse Package Publisher")
    print("=" * 60)
    
    if PYPI_TOKEN == "YOUR_PYPI_TOKEN_HERE":
        print("\n⚠️  WARNING: No API token configured!")
        print("You'll need to enter your PyPI username and password for each package.")
        print("\nTo avoid this, set your API token in this script or use:")
        print("export TWINE_PASSWORD=your-token-here\n")
        
        response = input("Continue with interactive login? (y/n): ")
        if response.lower() != 'y':
            print("❌ Cancelled")
            return
    
    successful = []
    failed = []
    
    for package in PACKAGES:
        if publish_package(package):
            successful.append(package)
        else:
            failed.append(package)
        
        # Small delay between uploads
        import time
        time.sleep(2)
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 PUBLISHING SUMMARY")
    print("=" * 60)
    print(f"✅ Successful: {len(successful)}")
    for pkg in successful:
        print(f"   • {pkg}")
    
    if failed:
        print(f"\n❌ Failed: {len(failed)}")
        for pkg in failed:
            print(f"   • {pkg}")
    
    print("\n🎉 Publishing complete!")

if __name__ == "__main__":
    main()
