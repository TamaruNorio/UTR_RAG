# Frontmatter Schema

## 1. Purpose

This schema defines metadata used by command cards, index documents, guides, result summaries, preflight documents, artifact README files, schema documents, and taxonomy documents.

## 2. Recommended command_card frontmatter

```yaml
---
title: ""
doc_type: "command_card"
package_scope: "UTR-S201"
manual: "TDR-MNL-PRC-UTR-S201-117"
manual_version: "1.17"
pdf_section: ""
command_group: ""
command_name: ""
command_byte: ""
detail_command: ""
subcommand: null
operation_stage: ""
operation_level: ""
rf_emission: false
write_operation: false
flash_operation: false
tag_memory_operation: false
requires_rom_check: true
requires_antenna: false
requires_tag: false
requires_access_password: false
requires_parameters: false
verification_status: ""
result_status: ""
related_docs: []
tags: []
---
```

## 3. Rules

- Boolean values must be `true` or `false`.
- Unknown values must not be guessed. Use `null` or `NEEDS_METADATA_CONFIRMATION`.
- `result_status` must not conflict with existing real-device verification results.
- `related_docs` uses standard Markdown relative paths.
- `tags` should use values defined in [Tag Taxonomy](TAG_TAXONOMY.md).
- A protocol-defined command must not be marked prohibited only because it is high impact.
- Protocol support and execution permission are separate layers.

## 4. doc_type guidance

| doc_type | Required keys | Recommended keys |
|---|---|---|
| command_card | title, doc_type, package_scope, manual, manual_version, pdf_section, command_name, result_status | command bytes, operation stage, impact flags, related_docs, tags |
| index | title, doc_type, package_scope | related_docs, tags |
| guide | title, doc_type, package_scope | verification_status, related_docs, tags |
| result_summary | title, doc_type, package_scope, result_status | verification_status, related_docs, tags |
| preflight | title, doc_type, package_scope | related_docs, tags |
| artifact_readme | title, doc_type, package_scope | result_status, related_docs, tags |
| schema | title, doc_type, package_scope | tags |
| taxonomy | title, doc_type, package_scope | tags |
