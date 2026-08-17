# Self-Contained ComfyUI-Wan2.x Local Automation

This repository provides a local execution environment for Wan 2.x Image-to-Video (I2V) designed specifically for hardware with limited system RAM and VRAM. It leverages the official ComfyUI Windows Portable release to bypass system Python mismatches and provide isolated package management.

## Prerequisites
- Windows OS (due to `.bat` launcher and ComfyUI portable)
- Hardware Constraint: **NVIDIA RTX 2060 (6GB VRAM)**. Because of this strict 6GB VRAM limit, the pipeline relies on extreme quantization, aggressive offloading, and tiled processing. All scripts, documentation, and configuration files reflect this constraint.

## Setup Instructions

1. **Download ComfyUI Portable**
   Download the official ComfyUI Windows Portable release from the [ComfyUI GitHub Releases page](https://github.com/comfyanonymous/ComfyUI/releases).
   Extract it directly into the root folder of this repository so that a folder named `ComfyUI_windows_portable` is present next to `run_wan2x_comfy.bat`.

2. **Download Models Manually**
   Due to size constraints and format requirements, you need to manually download the GGUF and 8-bit text encoder models.
   - Core Model: Download the quantized Wan 2.x 14B I2V model `wan2.2-i2v-14B-Q3_K.gguf` (or `Q4_K`) and place it in `ComfyUI_windows_portable/ComfyUI/models/unet`.
   - Text Encoder: Download the `UMT5-XXL` model and place it in `ComfyUI_windows_portable/ComfyUI/models/clip`. This is forced to run entirely on CPU in 8-bit.

3. **Input Staging**
   Place your input images into the `input` staging directory. The `worker-sower` automation scripts will handle routing from there to the ComfyUI input directory.

4. **Launch**
   Double-click `run_wan2x_comfy.bat`.

   The script will:
   - Use the isolated Python environment within `ComfyUI_windows_portable`.
   - Install required dependencies automatically.
   - Clone necessary custom nodes (`ComfyUI-GGUF`).
   - Launch ComfyUI with the essential `--lowvram` and `--fp8_e4m3fn-text-enc` arguments.

## Using the Workflow
Load `workflows/wan2x_low_vram_template.json` from the ComfyUI web interface. It comes pre-configured with the following constraints:
- 17 frames
- 832x480 resolution
- 20-25 FlowMatchEuler sampling steps
- CFG of 5.5
- VAE Decode (Tiled) set to Tile size: 256x256, temporal: 8

Adjust your inputs within the loaded nodes as necessary. Processed video outputs will be retrieved and staged into the `output` directory by the `worker-sower`.
