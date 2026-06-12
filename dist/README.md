# Distribution Packages

`dist/` contains distribution manifests and build notes only. It is not the source of truth and does not contain a ready-to-publish package by default. Generated packages should be built from source files and should not replace the source directories.

## Package builder

Dry-run by default:

```bash
python3 scripts/build_platform_packages.py --platform coze --locale zh-CN
```

Write a package:

```bash
python3 scripts/build_platform_packages.py --platform coze --locale zh-CN --execute
```

The builder refuses to overwrite existing files.

## Supported platforms

- `coze`
- `workbuddy`
- `trae`
- `codebuddy`
- `chat-only`

## Package destination

Generated packages are written to:

`dist/packages/{platform}-{locale}/`

Each package includes a generated `PACKAGE.md` with the file list and copied source documents.

Low-code packages are beta / experimental outputs. Validate them in the target platform before sharing them with users.
