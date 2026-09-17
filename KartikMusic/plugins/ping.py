

import time

import psutil
from pyrogram import filters, types

from KartikMusic import Kartik, app, boot, config, lang
from KartikMusic.helpers import buttons


@app.on_message(filters.command(["alive", "ping"]) & ~app.bl_users)
@lang.language()
async def _ping(_, m: types.Message):
    start = time.time()
    sent = await m.reply_text(m.lang["pinging"])

    def get_time(s):
        return (
            lambda r: (
                (f"{r[-1]}, " if r[-1][:-4] != "0" else "") + ":".join(reversed(r[:-1]))
            )
        )(
            [
                f"{v}{u}"
                for v, u in zip(
                    [s % 60, (s // 60) % 60, (s // 3600) % 24, s // 86400],
                    ["s", "m", "h", "days"],
                )
            ]
        )

    uptime = get_time(int(time.time() - boot))
    latency = round((time.time() - start) * 1000, 2)
    
    
    ping_text = m.lang["ping_pong"].format(
        latency,
        uptime,
        psutil.cpu_percent(interval=0),
        psutil.virtual_memory().percent,
        psutil.disk_usage("/").percent,
        await Kartik.ping(),
    )
    
    
    ping_text = f'<a href="{config.PING_IMG}">\u200b</a>' + ping_text
    
    await sent.edit_text(
        text=ping_text,
        reply_markup=buttons.ping_markup(m.lang["support"]),
        link_preview_options=types.LinkPreviewOptions(
            url=config.PING_IMG,
            prefer_large_media=True,
            show_above_text=False,
        ),
    )
