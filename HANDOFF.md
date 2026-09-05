# ArtMone configurator — короткий handoff

Продовжуй проєкт із GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`. Не починай з ZIP і не переписуй сайт з пам’яті. Спочатку прочитай `AGENTS.md`, `PROJECT_CHECKPOINT.md`, `HANDOFF.md` та актуальний `index.html`, потім звір поточний SHA `main` із GitHub і live.

Перевірений функціональний baseline: `700b1fb80c4cf7940a10f14f07f55f9777d0cfa6` (`Add AM1 and AM850 live gallery images`). AM1 і AM850 мають по 11 реальних WebP 1600×1600 і знаходяться на live. Калькулятор: 47 кольорів стрічки, 34 кольори друку, 100–10 000 м із нижчою прайсовою сходинкою, чорний друк без доплати, інші +4 грн/м, терміново +20%, AM814/40 мм за прайсом 30 мм, до 20 позицій, autosave/share, локальна візуалізація логотипа.

Головна невирішена проблема: default AM567 має 7 legacy-файлів зі старими назвами, тому нова 11-карткова галерея показує placeholders. Пошкоджені `assets/import/*`, `assets/mockups/am-1/am1_gallery_webp.zip` і два старі import-workflows не використовувати.

Точний наступний крок: створити валідований idempotent importer для 11 WebP 1600×1600, першим прогоном нормалізувати AM567, після цього прибрати старий chunk/ZIP-механізм і підключити масовий pipeline `Pletor → Google Drive → GitHub → Vercel`. Не запускати генерацію зображень без прямої команди користувача. Не говорити «готово», доки зміни не закомічені, Vercel не завершив deploy і live не перевірений.

