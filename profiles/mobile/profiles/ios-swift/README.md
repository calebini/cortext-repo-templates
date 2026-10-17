# iOS Swift profile

Create the Xcode project with current Apple tooling, then use:

```text
app/ios/{{App Name}}/          application target
app/ios/{{App Name}}Tests/     unit and integration tests
app/ios/{{App Name}}UITests/   UI tests
core/                          Swift packages for domain behavior
```

Commit shared schemes deliberately. Do not commit signing identities, provisioning
profiles, or `xcuserdata`.
