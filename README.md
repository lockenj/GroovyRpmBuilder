GroovyRpmBuilder
==============

Groovy has for some reason decided to neglect the RPM world so this project is targeted to allow people to build RPM packaged versions of Groovy.
Gradle is our choice for build tools so with that in mind, we have a first pass at an rpm builder.

##Usage
1. from the root of the project run "gradle assemble"
2. A tarball can then be found in "build/distributions"
3. The rpm file can be found in "build/RPMS"

##Requirements
1. Java
2. Gradle
3. rpmbuild

##Future Enhancements
- Add auto download of latest groovy
- Add runline arg support for different versions of groovy
