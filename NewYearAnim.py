__version__ = (1, 0, 0)

#             █ █ ▀ █▄▀ ▄▀█ █▀█ ▀
#             █▀█ █ █ █ █▀█ █▀▄ █
#              © Copyright 2024
#           https://t.me/apcecoc
#
# 🔒      Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# meta developer: @apcecoc
# scope: hikka_only
# scope: hikka_min 1.2.10
from .. import loader, utils
from telethon.tl.types import Message
from asyncio import sleep
import random

@loader.tds
class NewYearAnimMod(loader.Module):
    """Новогодняя анимация через inline"""
    strings = {'name': 'NewYearAnim'}
    
    async def nyacmd(self, message: Message):
        """Запускает новогоднюю анимацию"""
        
        frames = [
            "🎄\n\n",
            "   ⭐️\n  🎄\n\n", 
            "   ⭐️\n  🎄🎁\n\n",
            "   ⭐️\n 🎁🎄🎁\n\n",
            "   ⭐️\n🎁🎄🎁🎁\n\n",
            "   ⭐️\n🎁🎄🎁🎁\n❄️  ❄️  ❄️\n",
            "   ⭐️\n🎁🎄🎁🎁\n❄️ 🎅 ❄️\n",
            "   ⭐️\n🎁🎄🎁🎁\n❄️🎅❄️\n🎁 🎁 🎁\n",
            "✨  ⭐️  ✨\n🎁🎄🎁🎁\n❄️🎅❄️\n🎁 🎁 🎁\n",
            "✨  ⭐️  ✨\n🎁🎄🎁🎁\n❄️🎅❄️\n🎁 🎁 🎁\n\n❄️ С Новым Годом! ❄️"
        ]

        # Создаем конвертер для анимации
        async def create_animation():
            return await self.inline.form(
                message=message,
                text=frames[0],
                reply_markup={"text": "🎄 Запустить анимацию", "callback": self.animate},
                silent=True,
                ttl=1200,
            )

        await create_animation()

    async def animate(self, call):
        """Callback для анимации"""
        frames = [
            "🎄\n\n",
            "   ⭐️\n  🎄\n\n", 
            "   ⭐️\n  🎄🎁\n\n",
            "   ⭐️\n 🎁🎄🎁\n\n",
            "   ⭐️\n🎁🎄🎁🎁\n\n",
            "   ⭐️\n🎁🎄🎁🎁\n❄️  ❄️  ❄️\n",
            "   ⭐️\n🎁🎄🎁🎁\n❄️ 🎅 ❄️\n",
            "   ⭐️\n🎁🎄🎁🎁\n❄️🎅❄️\n🎁 🎁 🎁\n",
            "✨  ⭐️  ✨\n🎁🎄🎁🎁\n❄️🎅❄️\n🎁 🎁 🎁\n",
            "✨  ⭐️  ✨\n🎁🎄🎁🎁\n❄️🎅❄️\n🎁 🎁 🎁\n\n❄️ С Новым Годом! ❄️"
        ]

        # Анимация через редактирование
        for frame in frames:
            await call.edit(
                text=frame,
                reply_markup={"text": "🎄 Перезапустить", "callback": self.animate},
            )
            await sleep(0.8)

        # Падающий снег в конце
        final = frames[-1]
        for _ in range(5):
            snow = ""
            for _ in range(3):
                snow += "❄️" if random.random() > 0.5 else "✨"
            await call.edit(
                text=final + "\n" + snow,
                reply_markup={"text": "🎄 Перезапустить", "callback": self.animate},
            )
            await sleep(0.5)