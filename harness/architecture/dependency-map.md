# Dependency Map

## Rules

1. `SKILL.md` may reference prompts, templates, references, and scripts, but should not inline long content.
2. Prompts may reference templates and references.
3. Templates must not depend on platform adapters.
4. References must not depend on a specific platform.
5. Platform adapters may reference core, prompts, templates, and references; core must not depend on platform adapters.
6. Examples should depend on templates, but must not become template sources.
7. Evals should check core behavior, but must not become business logic sources.
8. Scripts may check structure, but must not silently modify content.
9. `dist/` packages are generated from source files and must not become source files.
10. `platforms/` must not break the native Codex Skill.

## Text dependency graph

```text
SKILL.md
  -> core/protocols
  -> core/prompts/{locale}
  -> prompts/{locale}
  -> templates/{locale}
  -> references/{locale}
  -> scripts

core/protocols
  -> references/{locale}
  -> templates/{locale}

prompts/{locale}
  -> templates/{locale}
  -> references/{locale}

templates/{locale}
  -> no platform dependency

references/{locale}
  -> no platform dependency

platforms/
  -> core/protocols
  -> prompts/{locale}
  -> templates/{locale}
  -> references/{locale}
  -/-> core/protocols

examples/
  -> templates/{locale}
  -> prompts/{locale}

evals/
  -> expected behavior
  -/-> production logic

scripts/
  -> repository files
  -/-> silent writes

dist/
  -> generated or packaging manifests
  -/-> source of truth
```

