default:
	@just --list

build:
	uv build

test:
	uv run pytest -v

check-licenses:
	reuse lint

publish: (build)
	uvx twine upload -u $(op read "op://Private/PyPI/username") -p $(op read "op://Private/PyPI/Tokens/Armadillo") dist/*  
