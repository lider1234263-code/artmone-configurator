# ArtMone configurator: короткий handoff

Продовжуй з GitHub `lider1234263-code/artmone-configurator`, гілка `main`. Live: `https://artmone-configurator-na4n.vercel.app/`. Спочатку прочитай `AGENTS.md`, `PROJECT_CHECKPOINT.md`, `HANDOFF.md` та актуальний `index.html`, потім звір SHA GitHub `main` і live.

Перевірений функціональний коміт: `2c9aa70f1a8d1e1709f856b6fa3d3068df83cb17` (`Preload gallery photos in the background`). Джерело оригіналів: Google Drive `https://drive.google.com/drive/folders/12RJaeKrmLchaJoqVuvmczhb7DavVJqU4`.

Остання повна контрольна перевірка виконана на GitHub `main` `8eeed5403513b614278a35c9fca3417c868e392f`. Live `index.html` точно збігся з репозиторієм, SHA-256: `aba78ed1231837821b5251fc772298da1efe83a69a2356ea1951b11717ba2b83`.

На live готові шість комплектів: `AM1`, `AM5`, `AM6`, `AM8`, `AM009`, `AM850`. Кожен має 11 WebP 1600x1600 і 11 thumbnails 320x320. Разом 132 файли; усі live-адреси перевірено і побайтно зіставлено з репозиторієм.

Універсальна назва: `AMCODE_01.webp` ... `AMCODE_11.webp`. Повні фото лежать у `assets/mockups/am-<код>/`, мініатюри у `assets/mockups/am-<код>/thumbs/`. `index.html` автоматично формує ці шляхи для всіх 47 кольорів. Імпортер: `scripts/import_gallery.py`; залежність: `scripts/requirements-gallery.txt`.

Після відкриття кольору і успішного показу головного фото сайт у фоні підвантажує решту 10 повних фото, максимум по три одночасно. Найближчі фото мають пріоритет, дублікати запитів не створюються. Функція спільна для всіх 47 карток і автоматично застосовується до нових галерей.

Бізнес-правила не змінювати: 47 кольорів стрічки, 34 кольори друку, 100-10 000 м із нижчою прайсовою сходинкою, чорний друк без доплати, інші +4 грн/м, терміново +20%, AM814/40 мм за прайсом 30 мм, до 20 позицій, autosave/share, локальна візуалізація логотипа.

Точний наступний крок: коли користувач додасть наступні 11 PNG `AMCODE_01.png` ... `AMCODE_11.png` у цю саму Drive-папку, отримати лише цей комплект через Google Drive, прогнати importer, перевірити 11 full + 11 thumbs, закомітити в `main`, дочекатися Vercel і перевірити 22 live-адреси. Повторити для решти 41 кольору.

Не використовувати старі ZIP/chunks та `recolor/studio` назви. Не змінювати Drive-оригінали. Не генерувати фото. Не казати «готово», доки GitHub, Vercel і live не перевірені.
