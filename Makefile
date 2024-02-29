#!/usr/bin/make

.PHONY: watch

watch:
	@docker compose -f compose.dev.yml watch
