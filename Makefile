.PHONY: setup api web test
setup:
	python -m venv .venv && . .venv/bin/activate && pip install -r services/api/requirements.txt
api:
	cd services/api && uvicorn app.main:app --reload --port 8080
web:
	cd apps/web && npm run dev
test:
	pytest services
