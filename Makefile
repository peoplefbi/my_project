install:
	uv sync

VD-games:
	uv run python3 my_project_markov/VD_games/scripts/VD_main.py

build:
	uv build

package-install:
	uv tool install ../dist/*.whl

