import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "8228197550:AAEAbnaXdCLR2qARF37ah4bDERyOk-Q0kcY" 
# Включаем логирование
logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


# Функция для шифрования/дешифрования (шифр Цезаря)
def caesar_cipher(text: str, shift: int) -> str:
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply(
        "Привет! Я бот для шифрования и дешифрования 🔐\n\n"
        "Используй команды:\n"
        "`/encrypt <текст> <сдвиг>` — зашифровать\n"
        "`/decrypt <текст> <сдвиг>` — расшифровать",
        parse_mode="Markdown"
    )


@dp.message_handler(commands=['encrypt'])
async def encrypt_text(message: types.Message):
    try:
        _, text, shift = message.text.split(" ", 2)
        shift = int(shift)
        encrypted = caesar_cipher(text, shift)
        await message.reply(f"🔒 Зашифрованный текст:\n`{encrypted}`", parse_mode="Markdown")
    except Exception:
        await message.reply("❌ Использование: `/encrypt текст сдвиг`", parse_mode="Markdown")


@dp.message_handler(commands=['decrypt'])
async def decrypt_text(message: types.Message):
    try:
        _, text, shift = message.text.split(" ", 2)
        shift = int(shift)
        decrypted = caesar_cipher(text, -shift)
        await message.reply(f"🔓 Расшифрованный текст:\n`{decrypted}`", parse_mode="Markdown")
    except Exception:
        await message.reply("❌ Использование: `/decrypt текст сдвиг`", parse_mode="Markdown")


if name == '__main__':
    executor.start_polling(dp, skip_updates=True)