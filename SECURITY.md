# Security Policy

## Supported Versions

The first public release is `v0.1.0`. Security fixes are handled on the latest
public release line unless a maintainer announces otherwise.

## Reporting a Vulnerability

Please report security issues privately by opening a GitHub Security Advisory
for this repository when available. If advisory reporting is unavailable, open a
minimal public issue that says a private security report is needed, without
including exploit details, tokens, private documents, or personal data.

Do not include real API keys, private learning materials, unpublished PDFs,
slide decks, personal notes, or user data in an issue, pull request, screenshot,
or test fixture.

## Scope

Security reports may include:

- accidental exposure of secrets or private files
- unsafe handling of user-provided learning materials
- prompt or template behavior that encourages credential disclosure
- release packaging that includes caches, logs, generated reports, or private
  data

This project is a prompt and workflow package. It cannot guarantee that every
agent platform will enforce the same security boundaries. Users should review
platform permissions before uploading private materials or enabling web access.
