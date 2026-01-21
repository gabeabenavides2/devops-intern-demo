# DevOps Intern Demo (FastAPI + CI)

Small FastAPI service used to demonstrate CI/CD fundamentals:
- GitHub Actions pipeline (YAML)
- Automated testing with pytest
- Simple health endpoint

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
