build:
	uv build

publish: (build)
	uvx twine upload -u $(op read "op://Private/PyPI/username") -p $(op read "op://Private/PyPI/Tokens/Armadillo") dist/*  
