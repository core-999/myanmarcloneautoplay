
import asyncio
import os

import aiohttp
from PIL import Image, ImageDraw, ImageEnhance, ImageFilter, ImageFont, ImageOps

from KartikMusic import config
from KartikMusic.helpers import Track


class Thumbnail:
    def __init__(self):
    
        self.session: aiohttp.ClientSession | None = None

    async def start(self) -> None:
        self.session = aiohttp.ClientSession()

    async def close(self) -> None:
        if self.session:
            await self.session.close()

    async def save_thumb(self, output_path: str, url: str) -> str:
        async with self.session.get(url) as resp:
            with open(output_path, "wb") as f:
                f.write(await resp.read())
        return output_path

    
    def _draw_image(self, temp, output, size=(1280, 720)):
        
        thumb = Image.open(temp).convert("RGB").resize(size, Image.Resampling.LANCZOS)

        

        
        thumb.save(output)
        return output

    async def generate(self, song: Track, size=(1280, 720)) -> str:
        try:
            
            output = f"cache/{song.id}.png"

            if os.path.exists(output):
                return output

             
            custom_image_url = "https://files.catbox.moe/cal5f4.jpg"

            
            temp_filename = f"cache/temp_{song.id}.jpg"

            
            await self.save_thumb(temp_filename, custom_image_url)

            
            await asyncio.to_thread(self._draw_image, temp_filename, output, size)

            
            try:
                os.remove(temp_filename)
            except Exception:
                pass
            return output
        except Exception:
            
            return config.DEFAULT_THUMB
