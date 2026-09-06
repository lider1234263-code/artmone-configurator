# ArtMone configurator: короткий handoff

Джерело істини: GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`.

Актуальний `main` перед цією зміною — `49c35f7553ab429a8498ee89183e56eedcebc284`; pull request #1 зі скиданням метражу об’єднано, Vercel deployment завершено, live-переходи 500 → 100 м перевірено через палітру й каталог. Поточна окрема правка робить видиме головне фото клікабельним на desktop і mobile: фото та кнопка «+» використовують один обробник lightbox; для фото додано клавіатурне керування Enter/Space.

Cleanup виконано окремо без зміни `index.html` і бізнес-логіки: прибрано ZIP/chunks, усі мертві import- та одноразові patch-workflows, два пов’язані patch-скрипти, а також застарілі `manifest.json`, `_headers`, `README_TECH_ONLY_UA.txt`. Актуальний importer — `scripts/import_gallery.py`; cache headers визначає `vercel.json`.

Готові AM1, AM5, AM6, AM8, AM009, AM850: кожна має 11 WebP 1600×1600 і 11 thumbnails 320×320. Після успішного головного фото решта завантажуються у фоні, максимум три запити одночасно.

AM567 досі має сім legacy-файлів і не має канонічного комплекту. Не генерувати фото й не змінювати галереї в межах поточної правки.

Точний наступний крок: переглянути й об’єднати pull request із клікабельним головним фото, дочекатися автоматичного Vercel deployment з `main`, а потім перевірити live на desktop і mobile: відкриття lightbox через фото, кнопку «+» і клавіші Enter/Space та коректне закриття.

На старті наступної сесії прочитати `AGENTS.md`, `PROJECT_CHECKPOINT.md`, цей файл і весь `index.html`; звірити SHA `main`, clean/dirty status та live. Не повідомляти про завершення етапу без commit/push, Vercel deployment і live-перевірки.
