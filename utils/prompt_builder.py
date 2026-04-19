prompt_builder.py
Builds richly-detailed visual and caption prompts tuned for each social platform.
"""
from __future__ import annotations

STYLE_PRESETS: dict[str, str] = {
    "Cinematic": (
        "cinematic wide-angle shot, dramatic lighting, film grain, "
        "anamorphic lens flare, shallow depth of field, color graded, "
        "professional photography, 8K resolution"
    ),
    "Minimal & Clean": (
        "minimalist composition, clean white background, soft diffused light, "
        "negative space, editorial style, product photography aesthetic"
    ),
    "Vibrant & Bold": (
        "vivid saturated colors, high contrast, energetic composition, "
        "dynamic angles, bold typography space, lifestyle photography"
    ),
    "Dark & Moody": (
        "dark moody atmosphere, deep shadows, low-key lighting, "
        "chiaroscuro, dramatic, editorial fashion photography"
    ),
    "Natural & Authentic": (
        "natural golden hour lighting, candid lifestyle photography, "
        "warm tones, authentic moment, environmental portrait"
    ),
    "Futuristic / Tech": (
        "neon cyberpunk aesthetic, holographic UI elements, "
        "dark background with glowing accents, sci-fi atmosphere, "
        "highly detailed 3D render"
    ),
    "Luxury & Premium": (
        "luxury brand aesthetic, marble textures, gold accents, "
        "high-end product photography, soft bokeh, aspirational lifestyle"
    ),
