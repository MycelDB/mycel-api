# Security Policy

## Reporting a vulnerability

Please report suspected security vulnerabilities privately through GitHub Security Advisories / private vulnerability reporting for this repository.

Use the repository's **Security** tab and choose **Report a vulnerability**. Do not open a public issue with vulnerability details.

If private vulnerability reporting is not visible, open a public issue that says only that you need a private security reporting channel. Do not include exploit details, affected secrets, proof-of-concept code, or other sensitive information in the public issue.

## What to include

When possible, include:

- The affected API package, service, RPC, message, or field.
- The affected repository version, commit, or release tag.
- A description of the vulnerability and expected impact.
- Reproduction steps or proof-of-concept details.
- Any known mitigations or workarounds.

## Scope

This repository contains protobuf and gRPC API definitions. Security reports may still apply here when the API contract creates or exposes a security issue, such as unsafe authorization semantics, credential handling, privacy leaks, missing capability checks, unsafe defaults, or compatibility behavior that could lead to data exposure.

Implementation vulnerabilities in the daemon, SDKs, or console may be redirected to the corresponding repository after initial triage.
