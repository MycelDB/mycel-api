.PHONY: breaking format format-check lint test

BUF ?= buf
BREAKING_AGAINST ?=

lint:
	$(BUF) lint

format:
	$(BUF) format -w

format-check:
	$(BUF) format --diff --exit-code

breaking:
ifndef BREAKING_AGAINST
	$(error set BREAKING_AGAINST=<baseline>, for example a release tag, branch, or Buf module reference)
endif
	$(BUF) breaking --against $(BREAKING_AGAINST)

test: lint format-check
