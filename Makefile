# ==== PHONY ТАРГЕТЫ ====
.PHONY: sync hooks dev-install setup fmt lint type test all clean

# Синхронизация зависимостей по корневому pyproject.toml
sync:
	@uv sync  # подтянуть зависимости и создать/обновить venv

# Установка pre-commit хуков (локально)
hooks: sync
	@uv run pre-commit install
	@echo "[+] pre-commit hook установлен"

# Прогоняем все проверки pre-commit сразу на всех файлах в проекте
pre-commit: hooks
	@uv run pre-commit run --all-files

# Полная подготовка окружения
setup: pre-commit
	@echo "[✓] Проект готов к разработке"

# Линтинг
lint:
	@uv run ruff check .

# Форматирование
fmt:
	@uv run ruff format .

# Проверка типов
type:
# Как-нибудь в другой раз, устаю и не понимаю
#	@uv run mypy .

# Запуск тестов
test:
	@uv run pytest -q

# Полный прогон проверок
ci: fmt lint type test

# Очистка кешей и окружения
clean:
	@rm -rf .pytest_cache .mypy_cache .ruff_cache .venv uv.lock
