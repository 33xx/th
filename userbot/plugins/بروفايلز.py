import asyncio
import base64
import os
import shutil
import time
from datetime import datetime

from PIL import Image, ImageDraw, ImageFont
from pySmartDL import SmartDL
from telethon.errors import FloodWaitError
from telethon.tl import functions

from ..Config import Config
from ..helpers.utils import _format
from ..sql_helper.globals import addgvar, delgvar, gvarstatus
from . import AUTONAME, DEFAULT_BIO, edit_delete, jmthon, logging

plugin_category = "tools"

DEFAULTUSERBIO = DEFAULT_BIO or " π»ππ π½ππΎπΊππ ππΊππΎ πππΊππ π»πΎππππππππ β° "
DEFAULTUSER = AUTONAME or Config.ALIVE_NAME
LOGS = logging.getLogger(__name__)

FONT_FILE_TO_USE = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"

autopic_path = os.path.join(os.getcwd(), "userbot", "original_pic.png")
digitalpic_path = os.path.join(os.getcwd(), "userbot", "digital_pic.png")
autophoto_path = os.path.join(os.getcwd(), "userbot", "photo_pfp.png")

digitalpfp = Config.DIGITAL_PIC or "https://telegra.ph/file/3efc6f3494afa987cefcf.jpg"
RR7PP = Config.TIME_JM or "β°"

normzltext = "1234567890"
namerzfont = [
    "π",  # ΩΩΨ― Ψ±ΩΩΩ Ψ­Ψ΅Ψ±ΩΨ§  !!
    "π",
    "π",
    "π",
    "π",
    "π",
    "π",
    "π",
    "π",
    "π",
]


async def digitalpicloop():
    DIGITALPICSTART = gvarstatus("digitalpic") == "true"
    i = 0
    while DIGITALPICSTART:
        if not os.path.exists(digitalpic_path):
            downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
            downloader.start(blocking=False)
            while not downloader.isFinished():
                pass
        shutil.copy(digitalpic_path, autophoto_path)
        Image.open(autophoto_path)
        current_time = datetime.now().strftime("%I:%M")
        img = Image.open(autophoto_path)
        drawn_text = ImageDraw.Draw(img)
        roz = str(base64.b64decode("dXNlcmJvdC9oZWxwZXJzL3N0eWxlcy9QYXliQWNrLnR0Zg=="))[
            2:36
        ]
        fnt = ImageFont.truetype(roz, 65)
        drawn_text.text((300, 400), current_time, font=fnt, fill=(280, 280, 280))
        img.save(autophoto_path)
        file = await jmthon.upload_file(autophoto_path)
        try:
            if i > 0:
                await jmthon(
                    functions.photos.DeletePhotosRequest(
                        await jmthon.get_profile_photos("me", limit=1)
                    )
                )
            i += 1
            await jmthon(functions.photos.UploadProfilePhotoRequest(file))
            os.remove(autophoto_path)
            await asyncio.sleep(60)
        except BaseException:
            return
        DIGITALPICSTART = gvarstatus("digitalpic") == "true"


async def autoname_loop():
    AUTONAMESTART = gvarstatus("autoname") == "true"
    while AUTONAMESTART:
        time.strftime("%Y/%m/%d")
        HM = time.strftime("%I:%M")
        for normal in HM:
            if normal in normzltext:
                namefont = namerzfont[normzltext.index(normal)]
                HM = HM.replace(normal, namefont)
        name = f"{RR7PP} {HM}"
        LOGS.info(name)
        try:
            await jmthon(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTONAMESTART = gvarstatus("autoname") == "true"


async def autobio_loop():
    AUTOBIOSTART = gvarstatus("autobio") == "true"
    while AUTOBIOSTART:
        time.strftime("%d.%m.%Y")
        HI = time.strftime("%I:%M")
        bio = f"{DEFAULTUSERBIO} {HI}"
        LOGS.info(bio)
        try:
            await jmthon(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            LOGS.warning(str(ex))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(Config.CHANGE_TIME)
        AUTOBIOSTART = gvarstatus("autobio") == "true"


@jmthon.ar_cmd(
    pattern="Ψ§ΩΨ΅ΩΨ±Ψ© Ψ§ΩΩΩΨͺΩΨ©$",
    command=("Ψ§ΩΨ΅ΩΨ±Ψ© Ψ§ΩΩΩΨͺΩΨ©", plugin_category),
)
async def _(event):
    "To set random colour pic with time to profile pic"
    downloader = SmartDL(digitalpfp, digitalpic_path, progress_bar=False)
    downloader.start(blocking=False)
    while not downloader.isFinished():
        pass
    if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
        return await edit_delete(event, "**Ψ§ΩΨ΅ΩΩΨ±Ψ© Ψ§ΩΩΩΩΨͺΩΨ© Ψ΄ΨΊΩΨ§ΩΨ© Ψ¨Ψ§ΩΨ£Ψ΅ΩΩ β°**")
    addgvar("digitalpic", True)
    await edit_delete(event, "**ΨͺΩ ΨͺΩΩΨΉΩΩ Ψ§ΩΨ΅ΩΩΨ±Ψ© Ψ§ΩΩΩΩΨͺΩΨ© Ψ¨ΩΨ¬ΩΨ§Ψ­ β°**")
    await digitalpicloop()


@jmthon.ar_cmd(
    pattern="Ψ§Ψ³Ω ΩΩΨͺΩ$",
    command=("Ψ§Ψ³Ω ΩΩΨͺΩ", plugin_category),
)
async def _(event):
    "To set your display name along with time"
    if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
        return await edit_delete(event, "**Ψ§ΩΨ§Ψ³ΩΩ Ψ§ΩΩΩΩΨͺΩ Ψ΄ΨΊΩΨ§Ω Ψ¨Ψ§ΩΨ£Ψ΅ΩΩ β°**")
    addgvar("autoname", True)
    await edit_delete(event, "**ΨͺΩ ΨͺΩΩΨΉΩΩ Ψ§ΩΨ§Ψ³ΩΩ Ψ§ΩΩΩΩΨͺΩ Ψ¨ΩΨ¬ΩΨ§Ψ­ β°**")
    await autoname_loop()


@jmthon.ar_cmd(
    pattern="Ψ¨Ψ§ΩΩ ΩΩΨͺΩ$",
    command=("Ψ¨Ψ§ΩΩ ΩΩΨͺΩ", plugin_category),
)
async def _(event):
    "To update your bio along with time"
    if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
        return await edit_delete(event, "**Ψ§ΩΩΨ¨Ψ§ΩΩ Ψ§ΩΩΩΩΨͺΩ Ψ΄ΨΊΩΨ§Ω Ψ¨Ψ§ΩΨ£Ψ΅ΩΩ β°**")
    addgvar("autobio", True)
    await edit_delete(event, "**ΨͺΩ ΨͺΩΩΨΉΩΩ Ψ§ΩΨ¨ΩΨ§ΩΩ Ψ§ΩΩΩΩΨͺΩ Ψ¨ΩΨ¬ΩΨ§Ψ­ β°**")
    await autobio_loop()


@jmthon.ar_cmd(
    pattern="Ψ§ΩΩΨ§Ψ‘ ([\s\S]*)",
    command=("Ψ§ΩΩΨ§Ψ‘", plugin_category),
)
async def _(event):  # sourcery no-metrics
    "To stop the functions of autoprofile plugin"
    input_str = event.pattern_match.group(1)
    if input_str == "Ψ§ΩΨ΅ΩΨ±Ψ© Ψ§ΩΩΩΨͺΩΨ©":
        if gvarstatus("digitalpic") is not None and gvarstatus("digitalpic") == "true":
            delgvar("digitalpic")
            await event.client(
                functions.photos.DeletePhotosRequest(
                    await event.client.get_profile_photos("me", limit=1)
                )
            )
            return await edit_delete(event, "**ΨͺΩ Ψ§ΩΩΨ§Ω Ψ§ΩΨ΅ΩΨ±Ψ© Ψ§ΩΩΩΨͺΩΨ© Ψ¨ΩΩΨ¬Ψ§Ψ­ β°**")
        return await edit_delete(event, "**ΩΩ ΩΨͺΩ ΨͺΩΨΉΩΩ Ψ§ΩΨ΅ΩΨ±Ψ© Ψ§ΩΩΩΨͺΩΨ© Ψ¨Ψ§ΩΨ£Ψ΅Ω β°**")
    if input_str == "Ψ§Ψ³Ω ΩΩΨͺΩ":
        if gvarstatus("autoname") is not None and gvarstatus("autoname") == "true":
            delgvar("autoname")
            await event.client(
                functions.account.UpdateProfileRequest(first_name=DEFAULTUSER)
            )
            return await edit_delete(event, "**ΨͺΩ Ψ§ΩΩΨ§Ω  Ψ§ΩΨ§Ψ³Ω Ψ§ΩΩΩΨͺΩ Ψ¨ΩΩΨ¬Ψ§Ψ­ β°**")
        return await edit_delete(event, "**ΩΩ ΩΨͺΩ ΨͺΩΨΉΩΩ Ψ§ΩΨ§Ψ³Ω Ψ§ΩΩΩΨͺΩ Ψ¨Ψ§ΩΨ£Ψ΅Ω β°**")
    if input_str == "Ψ¨Ψ§ΩΩ ΩΩΨͺΩ":
        if gvarstatus("autobio") is not None and gvarstatus("autobio") == "true":
            delgvar("autobio")
            await event.client(
                functions.account.UpdateProfileRequest(about=DEFAULTUSERBIO)
            )
            return await edit_delete(event, "**  ΨͺΩ Ψ§ΩΩΨ§Ω Ψ§ΩΨ¨Ψ§ΩΩ Ψ§ΩΩΩΩΨͺΩ Ψ¨ΩΩΨ¬Ψ§Ψ­ β°**")
        return await edit_delete(event, "**ΩΩ ΩΨͺΩ ΨͺΩΨΉΩΩ Ψ§ΩΨ¨Ψ§ΩΩ Ψ§ΩΩΩΨͺΩ β°**")
    END_CMDS = [
        "Ψ§ΩΨ΅ΩΨ±Ψ© Ψ§ΩΩΩΨͺΩΨ©",
        "Ψ§Ψ³Ω ΩΩΨͺΩ",
        "Ψ¨Ψ§ΩΩ ΩΩΨͺΩ",
    ]
    if input_str not in END_CMDS:
        await edit_delete(
            event,
            f"ΨΉΩΨ°Ψ±Ψ§ ΩΨ¬ΩΨ¨ Ψ§Ψ³ΨͺΩΨ?Ψ―Ψ§Ω Ψ§ΩΨ§ΩΩΨ± Ψ¨Ψ΄ΩΩΩ Ψ΅Ψ­ΩΩΨ­ β°",
            parse_mode=_format.parse_pre,
        )


jmthon.loop.create_task(digitalpicloop())
jmthon.loop.create_task(autoname_loop())
jmthon.loop.create_task(autobio_loop())
