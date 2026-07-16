# Transit Project

A Python project for managing and analyzing bus route performance data.

## Features

- Route management with CRUD operations
- Performance analytics and leaderboard
- Live weather API integration
- ISS crew tracker
- Rich terminal table rendering

## Setup

1. Clone the repo
2. Create a virtual environment: `python3 -m venv venv`
3. Activate it: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Create a `.env` file with your API keys:
6. Run any module: `python3 main.py`

## Project Structure

- `route.py` — Route class with validation
- `registry.py` — RouteRegistry CRUD operations
- `analytics.py` — Performance analytics
- `main.py` — Rich table display
- `weather.py` — OpenWeatherMap API integration
- `astronauts.py` — ISS crew tracker
- `get.py` — JSONPlaceholder POST/GET demo
