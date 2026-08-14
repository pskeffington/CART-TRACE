# CART-TRACE Local Mapping Review Sheet

## Purpose

This template supports controlled review of institution-specific source labels inside an approved governed environment. The public repository defines only the review structure; local labels, identifiers, counts, and restricted descriptions remain governed.

## Mapping status vocabulary

- `approved`
- `needs_review`
- `unmapped`
- `excluded_from_mapping`

## Review table

| Local source label | Source domain/system | Local description | Candidate canonical state | Mapping status | Source authority/priority | Rationale | Reviewer | Review date | Mapping version | Notes/limitations |
|---|---|---|---|---|---|---|---|---|---|---|
| [governed] | [governed] | [governed] |  | needs_review |  |  |  |  |  |  |

## Review requirements

1. Candidate canonical states are limited to the frozen CART-TRACE vocabulary.
2. Source priority represents evidence authority, not physiologic or toxicity severity.
3. Equal-priority incompatible evidence follows the frozen conflict behavior and may produce `unknown`.
4. Unmapped labels remain explicit and are never silently coerced to a canonical state.
5. Every approved mapping records rationale, reviewer, review date, and mapping version.
6. Mapping changes require version increment and impact review across affected episodes.
7. A request for a new canonical state or changed precedence/conflict rule is not a local mapping edit; it requires formal gate-impact review.

## Mapping coverage summary

Inside the governed environment, summarize:

- unique local labels reviewed;
- approved labels;
- labels needing review;
- unmapped labels;
- excluded labels;
- record-level mapping coverage;
- episode-level mapping coverage;
- episodes materially affected by unmapped or disputed labels.

Only approved non-identifying aggregate summaries may enter public scholarly outputs.

## Completion criterion

Local mapping review is complete when all observed source labels relevant to trajectory reconstruction have an explicit status, approved mappings are versioned and attributable, disputed mappings are unresolved rather than silently forced, and coverage consequences are documented.
