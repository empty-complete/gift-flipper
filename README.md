 <p align="center">
  <img src="https://i.ibb.co/Jw5k4K4R/logo-kinesis-circle.png" alt="Kinesis Logo" width="100">
</p>
<h1 align="center">Gift Flipper <small>by kinesis</small></h1>
<p align="center">
  <i>Монорепозиторий сервисов для автоматизированного анализа и арбитража подарков между маркетплейсами <a href="https://market.tonnel.network">Tonnel</a> и <a href="https://portalsmarket.co">Portals</a>.</i>
</p>

<p align="center">
  <a href="https://github.com/empty-complete/gift-flipper/commits">
    <img src="https://img.shields.io/github/commit-activity/m/empty-complete/gift-flipper" alt="GitHub Release" />
  </a>
  <a href="https://github.com/empty-complete/gift-flipper/actions">
    <img alt="GitHub Actions Workflow Status" src="https://img.shields.io/github/actions/workflow/status/empty-complete/gift-flipper/ci.yml?logo=github&label=CI">
  </a>
  <a href="https://github.com/empty-complete/gift-flipper/blob/main/LICENSE">
    <img alt="MIT Licence" src="https://img.shields.io/badge/Licence-MIT-white?logo=keeweb&logoColor=white">
  </a>
  <a href="https://github.com/empty-complete/gift-flipper">
    <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/empty-complete/gift-flipper">
  </a>
</p>

<p align="center">
  <a href="https://boosty.to/kinesis_lab">
    <img alt="Boosty follow" src="https://img.shields.io/badge/boosty-follow-white?logo=boosty&labelColor=white&color=gray">
  </a>
  <a href="https://www.youtube.com/@kinesis_lab">
    <img alt="Youtube follow" src="https://img.shields.io/badge/youtube-follow-white?logo=youtube&logoColor=red&labelColor=white&color=gray">
  </a>
  <a href="https://t.me/kinesis_lab">
    <img alt="Telegram follow" src="https://img.shields.io/badge/telegram-follow-white?logo=telegram&logoColor=blue&labelColor=white&color=gray">
  </a>
</p>

## 🎯 Цель проекта

Создать систему, которая в реальном времени отслеживает рынок подарков на Tonnel и Portals, анализирует цены, историю сделок, редкость и активность продаж, выявляет выгодные для арбитража позиции и отправляет уведомления пользователям через Telegram-бота.

## 📦 Сервисы

- [**bot-gateway**](services/bot-gateway/README.md) — пользовательский Telegram-бот.
- _(в будущем)_ **api-gateway** — единая точка входа для CRUD-операций, брокера и внутреннего обмена данными между сервисами
- _(в будущем)_ **dispatcher** — маршрутизация событий и уведомлений.
- _(в будущем)_ **scraper-gifts** — парсинг источников (TONNEL, PORTALS).

## 🖥 Стек

- **Язык:** Python 3.10+
- **Пакетный менеджер:** [uv](https://docs.astral.sh/uv/)
- **Бот:** aiogram (план)
- **API** FastAPI (план)
- **Хранилища:** PostgreSQL, Redis (план)
- **Контейнеризация:** Docker, docker-compose (план)

## 🛠 TODO

- [ ] Настроить Docker и docker-compose для локальной разработки.
- [ ] Добавить RU/EN документацию по API сервисов.
- [ ] Настроить CI для публикации Docker-образов.
#

The project is actively developing, so you can offer your ideas for improvements and visit our [YouTube channel](https://youtube.com/@kinesis_lab) and [Telegram](https://t.me/kinesis_lab). Go to the `Projects` tab to keep track of current shell updates and future improvements.
