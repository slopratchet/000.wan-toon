import os
import sys
import subprocess
from pathlib import Path

def install_requirements():
    print("Installing requirements...")
    subprocess.check_call([
        sys.executable, "-m", "pip", "install",
        "huggingface_hub"
    ])

def clone_repos(custom_nodes_path):
    gguf_node_path = custom_nodes_path / "ComfyUI-GGUF"
    if not gguf_node_path.exists():
        print("Cloning ComfyUI-GGUF...")
        subprocess.call(["git", "config", "--global", "core.longpaths", "true"])
        subprocess.check_call([
            "git", "clone",
            "https://github.com/city96/ComfyUI-GGUF.git",
            str(gguf_node_path)
        ])
    else:
        print("ComfyUI-GGUF custom node folder already exists.")

def main():
    cwd = Path.cwd()
    comfyui_dir = cwd / "ComfyUI_windows_portable" / "ComfyUI"

    if not comfyui_dir.exists():
        comfyui_dir = cwd / "ComfyUI"
        if not comfyui_dir.exists():
            print("ComfyUI directory not found. Creating custom_nodes directory fallback...")
            comfyui_dir.mkdir(parents=True, exist_ok=True)

    custom_nodes_path = comfyui_dir / "custom_nodes"
    custom_nodes_path.mkdir(parents=True, exist_ok=True)

    install_requirements()
    clone_repos(custom_nodes_path)
    print("\n==========================================")
    print("Setup complete! You can now run the batch file.")
    print("==========================================")

if __name__ == "__main__":
    main()
