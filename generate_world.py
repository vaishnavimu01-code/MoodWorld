# generate_world.py

import os
import torch
from diffusers import AutoPipelineForText2Image


MODEL_ID = "stable-diffusion-v1-5/stable-diffusion-v1-5"

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

if DEVICE == "cuda":
    DTYPE = torch.float16
else:
    DTYPE = torch.float32


_pipeline = None


def get_pipeline():
    global _pipeline

    if _pipeline is not None:
        return _pipeline

    print("=" * 60)
    print("Loading Stable Diffusion...")
    print(f"Device: {DEVICE}")
    print("=" * 60)

    load_arguments = {
        "torch_dtype": DTYPE,
        "use_safetensors": True
    }

    if DEVICE == "cuda":
        load_arguments["variant"] = "fp16"

    _pipeline = AutoPipelineForText2Image.from_pretrained(
        MODEL_ID,
        **load_arguments
    )

    _pipeline = _pipeline.to(DEVICE)

    # Helps reduce memory usage.
    try:
        _pipeline.enable_attention_slicing()
    except Exception:
        pass

    return _pipeline


def generate_world(
    prompt,
    output_path,
    negative_prompt=None,
    steps=15,
    seed=42
):
    pipe = get_pipeline()

    if negative_prompt is None:
        negative_prompt = """
        low quality, blurry, distorted,
        ugly, deformed, duplicate objects,
        text, letters, watermark, logo,
        bad composition, oversaturated,
        unrealistic geometry
        """

    generator = torch.Generator(device=DEVICE).manual_seed(seed)

    print("Generating world...")
    print(f"Steps: {steps}")

    result = pipe(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_inference_steps=steps,
        guidance_scale=7.0,
        height=512,
        width=512,
        generator=generator
    )

    image = result.images[0]

    os.makedirs(
        os.path.dirname(output_path),
        exist_ok=True
    )

    image.save(output_path)

    print(f"Image saved to: {output_path}")

    return output_path