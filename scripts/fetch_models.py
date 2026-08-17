import os
import sys

def main():
    print("Please manually download the following models due to size constraints:")
    print("1. Core Model (GGUF):")
    print("   Download 'wan2.2-i2v-14B-Q3_K.gguf' (or 'Q4_K')")
    print("   Place in: ComfyUI_windows_portable/ComfyUI/models/unet/")
    print("2. Text Encoder (8-bit):")
    print("   Download 'UMT5-XXL' model")
    print("   Place in: ComfyUI_windows_portable/ComfyUI/models/clip/")
    print("\nNote: The text encoder is forced to run entirely on CPU in 8-bit to respect the 6GB VRAM limit.")

if __name__ == "__main__":
    main()
