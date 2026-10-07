# Authentication and Repository Security

## Important distinction

This repository is a film-development project, not an authentication application. The repository itself is protected by GitHub account authentication and repository permissions. There is currently no application login system in this codebase.

## Repository access flow

Developer -> GitHub account authentication -> repository permission check -> movie0001 -> read/write repository content as permitted.

## Credentials

Never store GitHub passwords, personal access tokens, API keys, cloud credentials, private keys, or database passwords in tracked files.

For future automation, credentials should be supplied through the execution environment or an appropriate secret-management system.

## Tokens

If future software uses bearer tokens or JWTs, document where tokens are issued, transmitted, stored, validated, expired, refreshed, and revoked, and which routes require them.

Do not describe a token flow as implemented until the corresponding code exists.

## Current implementation

There are no application authentication components, login endpoints, session handlers, JWT handlers, OAuth callbacks, password hashing modules, or authentication middleware in the repository at this milestone.
