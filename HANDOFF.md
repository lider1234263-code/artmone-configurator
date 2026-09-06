# ArtMone configurator: короткий handoff

Джерело істини: GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`.

Робоча гілка перед цією зміною була чистою на `952aed7050ee7dc92c15b76c90f43d636ad97f0b`. Коміт `c7f34b2f340dcca1fbc2d69b509fc0e35ddbef2a` змінює єдиний обробник вибору кольору: вибір через палітру або каталог встановлює для активної позиції 100 м і синхронізує поле метражу. Початкове завантаження autosave та конфігурації з `cfg` не проходить через цей обробник, тому явно збережений метраж не скидається.

Cleanup виконано окремо без зміни `index.html` і бізнес-логіки: прибрано ZIP/chunks, усі мертві import- та одноразові patch-workflows, два пов’язані patch-скрипти, а також застарілі `manifest.json`, `_headers`, `README_TECH_ONLY_UA.txt`. Актуальний importer — `scripts/import_gallery.py`; cache headers визначає `vercel.json`.

Готові AM1, AM5, AM6, AM8, AM009, AM850: кожна має 11 WebP 1600×1600 і 11 thumbnails 320×320. Після успішного головного фото решта завантажуються у фоні, максимум три запити одночасно.

AM567 досі має сім legacy-файлів і не має канонічного комплекту. Не генерувати фото й не змінювати галереї в межах поточної правки.

Точний наступний крок: переглянути й об’єднати pull request зі скиданням метражу, дочекатися автоматичного Vercel deployment з `main`, а потім перевірити live-вибір кольору через палітру й каталог та збереження явного метражу з autosave і `cfg`.

На старті наступної сесії прочитати `AGENTS.md`, `PROJECT_CHECKPOINT.md`, цей файл і весь `index.html`; звірити SHA `main`, clean/dirty status та live. Не повідомляти про завершення етапу без commit/push, Vercel deployment і live-перевірки.
