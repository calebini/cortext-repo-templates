# Android Kotlin profile

Create the Gradle project with current Android Studio tooling, then use:

```text
app/android/app/src/main/         application code and resources
app/android/app/src/test/         JVM tests
app/android/app/src/androidTest/  instrumented and UI tests
core/                             framework-light Kotlin modules
```

Use the Gradle wrapper. Keep release keystores and signing properties outside Git.
