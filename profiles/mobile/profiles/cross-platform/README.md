# Cross-platform profile

Select and record the actual framework before implementation. Put shared application
code beneath `app/shared/` and native host or bridge code beneath `app/ios/` and
`app/android/`.

Cross-platform code does not eliminate native ownership: signing, permissions,
privacy declarations, background execution, deep links, notifications, accessibility,
and store release must still be qualified independently on both platforms.
