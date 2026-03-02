# Получение токена Яндекс Музыки

Своё OAuth приложение создать нельзя. Единственный вариант это использовать приложения официальных клиентов Яндекс.Музыка.

Существует основные варианты получения токена:

[Вебсайт](https://music-yandex-bot.ru/)(работает не для всех аккаунтов)

Расширение для [Google Chrome](https://chrome.google.com/webstore/detail/yandex-music-token/lcbjeookjibfhjjopieifgjnhlegmkib)

Расширение для [Mozilla Firefox](https://addons.mozilla.org/en-US/firefox/addon/yandex-music-token/)

Затем, переименуйте файл .env.example в .env и добавьте в строку ya_token ваш токен

# Запуск скрипта

## Для тех кто использует uv

```bash
uv sync

uv run export.py
```

## Для тех кто использует pip

```bash
python -m venv .venv

source .venv/bin/activate
    
pip install -r requirements.txt

python export.py
```

# Итог: все песни будут по пути output/songs.txt