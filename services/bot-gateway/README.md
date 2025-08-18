# bot-gateway

**Пользовательский Telegram-бот взаимодействия с системой Gift Flipper**

## 🎯 Цель сервиса

Обеспечить удобное взаимодействие пользователей с системой:

- Регистрация и авторизация в боте.
- Настройка фильтров поиска подарков.
- Получение уведомлений о найденных выгодных подарках.
- Просмотр деталей сделок и аналитики (админка)

## 🔍 Функционал (план)

- Обработка команд и сообщений пользователей.
- Формирование и отправка уведомлений на основе данных от других сервисов.
- Поддержка гибкой фильтрации (по цене, активности, редкости и т.д.).
- Возможность управления настройками прямо из бота.

## 🛠 TODO

### bot-gateway/T1 — Инициализация & скелет (минимальный живой бот)

- [x] `pyproject.toml` с зависимостями: `aiogram`, `pydantic-settings`, `httpx`, `uvloop`, `pytest`, `pytest-asyncio`, `mypy`, `ruff`
- [x] `bot_gateway/config.py`: ~~Pydantic Settings (+ загрузка `.env`)~~ Dynaconf (+загрузка `settings.toml` + `.secrets.toml` + `.example`)
- [ ] `bot_gateway/logging.py`: корневой логгер, формат JSON/console, поле `request_id`
- [x] `bot_gateway/bot/factory.py`: сборка `Bot`, `Dispatcher`, регистрация роутеров
- [ ] `bot_gateway/bot/routers/`: регистрация роутеров
- [ ] `bot_gateway/bot/routers/start.py`: хендлер `/start` (пока **без** API) → “Привет! Меню: /menu”
- [ ] `bot_gateway/bot/routers/menu.py`: клавиатура (“Профиль”, “Фильтры” — пока заглушки)
- [ ] `bot_gateway/main.py`: запуск polling
- [ ] `tests/test_start.py`: smoke-тест `/start`
- [ ] `Makefile`: `run`, `fmt`, `lint`, `test`, `ci`

### bot-gateway/T2 — Корреляция и контекст пользователя

- [ ] `middlewares/correlation.py`: прокидка/генерация `X-Request-Id`
- [ ] `middlewares/userctx.py`: извлекаем `tg_id`, `username`, `lang` → контекст
- [ ] Подключить middlewares в `factory.py`
- [ ] Логи с `request_id`, `tg_id`

### bot-gateway/T3 — Клиент к control-api + идемпотентный /start

- [ ] `clients/schemas.py`: DTO для `/start` и ответов
- [ ] `clients/control_api.py`: httpx-клиент с таймаутами и ретраями
- [ ] `routers/start.py`: `POST /start` → меню (`created=true/false`)
- [ ] Ошибки 4xx/5xx → “техническая ошибка” + POST `/log`
- [ ] `tests/test_control_api_client.py`: мок клиента

### bot-gateway/T4 — Клавиатура и профиль (чтение)

- [ ] `keyboards/common.py`: кнопки “Профиль”, “Фильтры”, “Назад”
- [ ] `clients/control_api.py`: `GET /users/{tg_id}`, `GET /users/{tg_id}/filters`
- [ ] `menu.py`: профиль и фильтры
- [ ] Тесты рендера

### bot-gateway/T5 — FSM “Фильтры” (минимум: clean: bool)

- [ ] `states/filters.py`: FSM для clean
- [ ] `routers/filters.py`: `PUT /users/{tg_id}/filters`
- [ ] Ответ 200 → показать новое значение
- [ ] Ошибки → “техническая ошибка” + `POST /log`

### bot-gateway/T6 — Глобальный обработчик ошибок + /log

- [ ] `routers/errors.py`: глобальный handler
- [ ] `clients/control_api.py`: `POST /log`
- [ ] Дублирование событий в `/log`

### bot-gateway/T7 — Полировка устойчивости

- [ ] Таймауты/ретраи в http-клиенте
- [ ] Локализация RU/EN
- [ ] Конфигурируемые логи (json/plain)
- [ ] Метрика в логах

### bot-gateway/T8 — Тесты и качество

- [ ] Unit-тесты на все ветки
- [ ] `ruff` + `mypy` чисто
- [ ] `make ci` — lint + test

### bot-gateway/T9 — Docker & локальный compose

- [ ] `Dockerfile` (slim, uv build)
- [ ] `make docker`
- [ ] Пример `docker run` в README w
- [ ] bot-gateway/T10 — CI/CD
- [ ] **CI**: GitHub Actions → lint + tests
- [ ] **CD**: build & push Docker image по тегу

**Пример коммита**:
`bot-gateway/T1: scaffold package and minimal /start, /menu`

## 🖥 Стек

- Python 3.10+
- aiogram (v3+)
- pydantic
- pytest, pytest-asyncio
- pre-commit, ruff, mypy
- Docker
