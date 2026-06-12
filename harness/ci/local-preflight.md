# Local Preflight

No CI integration is configured in this harness pass.

Run locally before PR or release:

```bash
python harness/scripts/run_all_checks.py --root . --report
```

Use single checks while editing:

```bash
python harness/scripts/check_locale_parity.py --root .
python harness/scripts/check_platform_adapters.py --root .
python harness/scripts/check_release_readiness.py --root . --report
```

