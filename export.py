from yandex_music import Client
import os
from dotenv import load_dotenv

load_dotenv()

# Инициализация клиента
client = Client(os.getenv("ya_token")).init()

# Получаем ВСЕ лайкнутые треки
liked_tracks = client.users_likes_tracks()
tracks_count = len(liked_tracks)


def save_to_file():
    os.mkdir("output")
    file = "output/songs.txt"

    with open(file, "w", encoding="utf-8") as f:
        for i in range(tracks_count):
            try:
                # Получаем полную информацию о каждом треке
                track = liked_tracks[i].fetch_track()

                # Исполнителей может быть несколько, объединяем всех через запятую
                artists_names = ", ".join([artist.name for artist in track.artists])

                f.write(f"{artists_names}, {track.title}\n")
                print(f"Обработан трек {i + 1} из {tracks_count}")

            except Exception as e:
                print(f"Ошибка при обработке трека {i + 1}: {e}")
                f.write(f"Ошибка при обработке трека {i + 1}\n")
                f.write("-" * 50 + "\n\n")
                continue

    print(f"Информация о треках сохранена в {file}")


save_to_file()
