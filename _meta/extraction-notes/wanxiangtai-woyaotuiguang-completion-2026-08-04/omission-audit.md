# Omission audit

## Accounted omissions

- 30 of 431 `alidoc` nodes did not yield a structured document body.
- These nodes are directory containers, application/registration forms, rights-application pages, lists, or otherwise unsupported dynamic content.
- Their IDs and official parent paths remain in `document-tree.json`; module-level counts are in `coverage-matrix.md`.
- No formal page was generated from a title alone.

## Intentional compression

- Historical campaigns are summarized as reusable mechanisms and explicitly marked time-sensitive.
- Repeated UI steps were merged into stable operating sequences.
- Repeated FAQ answers were merged into diagnostic and boundary sections.
- Numerical thresholds, prices, dates and gray-release scope are retained only where needed for historical interpretation and carry a current-backend caveat.

## Not omitted

- Official module hierarchy and branch ownership.
- Product definitions, decision boundaries, operating steps, data definitions, risk rules and troubleshooting logic.
- Images and image manifests from captured packages.
