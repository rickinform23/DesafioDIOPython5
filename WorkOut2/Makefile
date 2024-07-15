run:
	@ouvicon store.main:app --reload

precommit-install:
	@poetry run pre-commit install

test:
	@poetry run pytest

testmatching:
	@poetry run pytest -s -rx -k $(K) --pdb store ./test/