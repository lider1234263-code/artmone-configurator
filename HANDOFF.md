# ArtMone configurator: короткий handoff

Джерело істини: GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`.

Перед cleanup локальна `main` і `origin/main` були чистими та збігалися на `9add08501401c69611664f5edc426cc3ef036686`. Попередня документальна контрольна точка — `e509d68433fcb04855e2a1aa85d84ef96cf2ecdc`; універсальне фонове завантаження галереї — `2c9aa70f1a8d1e1709f856b6fa3d3068df83cb17`. Коміт `9add085` після checkpoint зробив всю зону завантаження логотипа клікабельною.

Cleanup виконано окремо без зміни `index.html` і бізнес-логіки: прибрано ZIP/chunks, усі мертві import- та одноразові patch-workflows, два пов’язані patch-скрипти, а також застарілі `manifest.json`, `_headers`, `README_TECH_ONLY_UA.txt`. Актуальний importer — `scripts/import_gallery.py`; cache headers визначає `vercel.json`.

Готові AM1, AM5, AM6, AM8, AM009, AM850: кожна має 11 WebP 1600×1600 і 11 thumbnails 320×320. Після успішного головного фото решта завантажуються у фоні, максимум три запити одночасно.

AM567 досі має сім legacy-файлів і не має канонічного комплекту. Наступний крок: отримати 11 квадратних оригіналів `AM567_01` ... `AM567_11`, не змінювати Google Drive, нормалізувати через `scripts/import_gallery.py`, перевірити 11+11 файлів і лише тоді прибрати legacy AM567. Не генерувати фото.

На старті наступної сесії прочитати `AGENTS.md`, `PROJECT_CHECKPOINT.md`, цей файл і весь `index.html`; звірити SHA `main`, clean/dirty status та live. Не повідомляти про завершення етапу без commit/push, Vercel deployment і live-перевірки.
