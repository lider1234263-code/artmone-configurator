# ArtMone configurator: короткий handoff

Продовжуй з GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`. Спочатку прочитай `AGENTS.md`, `PROJECT_CHECKPOINT.md`, `HANDOFF.md` і весь актуальний `index.html`; потім звір SHA GitHub `main`, clean/dirty status та live.

Стан перед новою контрольною точкою: `main` був `8eeed5403513b614278a35c9fca3417c868e392f`. Останній робочий функціональний коміт: `2c9aa70f1a8d1e1709f856b6fa3d3068df83cb17` (`Preload gallery photos in the background`). Джерело оригіналів: Google Drive `https://drive.google.com/drive/folders/12RJaeKrmLchaJoqVuvmczhb7DavVJqU4`.

Проєкт статичний: один `index.html`, 47 кольорів стрічки, 34 кольори друку, без backend/build/package manager. GitHub `main` автоматично деплоїться на Vercel. На live готові `AM1`, `AM5`, `AM6`, `AM8`, `AM009`, `AM850`: по 11 WebP 1600x1600 і 11 thumbs 320x320, разом 132 файли. Галерея формує універсальні шляхи `AMCODE_01.webp` ... `AMCODE_11.webp`; після успішного першого фото підвантажує решту у фоні, максимум три запити одночасно. Імпортер: `scripts/import_gallery.py`.

AM567 має лише сім legacy-файлів, не відповідає стандарту і показує placeholder для нових canonical paths. Не генерувати відсутні фото. Ще 41 колір не має повного canonical-комплекту. Кнопки замовлення/контакту ще не передають заявку менеджеру.

Бізнес-правила не змінювати: 100-10 000 м із кроком 100 м і нижчою прайсовою сходинкою, чорний друк без доплати, інші кольори +4 грн/м, терміново +20%, AM814 40 мм за прайсом 30 мм, до 20 позицій, autosave/share, логотип лише локально у браузері.

Точний наступний крок: окремим cleanup-комітом без зміни `index.html` прибрати `assets/import/bundle.zip`, чотири `chunk_*.txt`, мертві workflows `import-gallery-zips.yml` і `unpack-am1-gallery.yml`; перевірити решту одноразових workflows; узгодити або прибрати застарілі `manifest.json`, `_headers`, `README_TECH_ONLY_UA.txt`; зробити commit/push, дочекатися Vercel і перевірити live. Після цього отримати 11 квадратних оригіналів AM567 та нормалізувати їх importer-ом.

Не використовувати ZIP/chunks або старі `recolor/studio` назви. Не змінювати Drive-оригінали. Не комітити логотипи клієнтів. Не повідомляти про завершення без commit/push, Vercel deployment і live-перевірки.
