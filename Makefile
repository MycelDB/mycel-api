.PHONY: lint test

BUF ?= buf

lint:
	$(BUF) lint

test: lint
