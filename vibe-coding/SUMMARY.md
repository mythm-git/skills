# Vibe Coding: Quick Orientation

`vibe-coding` is a portable Agent Skills package for disciplined software development. It helps agents select an appropriate development mode, classify risk, load only relevant guidance, implement incrementally, and report verified—not assumed—results.

Use it for new projects, existing-project work, fixes, refactors, reviews, security work, testing, deployment preparation, and documentation. Its main entrypoint stays short; detailed security, testing, and delivery guidance lives in `references/`.

Run the repository checks with:

```powershell
python scripts/validate_skill.py
python scripts/validate_references.py
python scripts/check_secrets.py
python scripts/security_audit.py
python -m unittest discover -s tests -v
```

Read [README.md](README.md) for installation and operational guidance. See [docs/compatibility.md](docs/compatibility.md) for evidence-based platform status.
