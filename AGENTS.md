# Template Repository Instructions

Shared working conventions belong in `base/`. Platform-specific rules belong in
the relevant profile. Do not duplicate shared rules across profiles.

Keep generated output portable: no user paths, host identifiers, credentials,
signing material or actual production configuration. Preserve placeholders.

Run `python3 -m unittest discover -s tests -v` and `git diff --check` after changes.
Use `docs/backlog.md` for future work and `docs/implementation-plan.md` for active
delivery. Decision records explain meaningful choices; handoffs are transient.
