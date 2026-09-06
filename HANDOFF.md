# ArtMone configurator: короткий handoff

Джерело істини: GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`.

Pull request #2 з функціональним комітом `2519d30296170b2ae09210f71d29c6bbef64ef6e` об’єднано в `main` merge-комітом `49b07245d39be3a8beadcb17520e814298c5e309`; production Vercel deployment успішний. Видиме головне фото та кнопка «+» використовують один lightbox-обробник; для фото додано `zoom-in`, доступну роль кнопки та керування Enter/Space. На live desktop перевірено відкриття через фото, «+», Enter і Space та закриття; той самий DOM і обробник використовуються в mobile layout без окремої media-query логіки.

Cleanup виконано окремо без зміни `index.html` і бізнес-логіки: прибрано ZIP/chunks, усі мертві import- та одноразові patch-workflows, два пов’язані patch-скрипти, а також застарілі `manifest.json`, `_headers`, `README_TECH_ONLY_UA.txt`. Актуальний importer — `scripts/import_gallery.py`; cache headers визначає `vercel.json`.

Готові AM1, AM5, AM6, AM8, AM009, AM850: кожна має 11 WebP 1600×1600 і 11 thumbnails 320×320. Після успішного головного фото решта завантажуються у фоні, максимум три запити одночасно.

AM567 досі має сім legacy-файлів і не має канонічного комплекту. Не генерувати фото й не змінювати галереї в межах поточної правки.

Точний наступний крок: отримати від користувача наступну пріоритетну UI/UX правку. AM567 не змінювати, доки в Google Drive не буде 11 канонічних квадратних оригіналів.

На старті наступної сесії прочитати `AGENTS.md`, `PROJECT_CHECKPOINT.md`, цей файл і весь `index.html`; звірити SHA `main`, clean/dirty status та live. Не повідомляти про завершення етапу без commit/push, Vercel deployment і live-перевірки.
