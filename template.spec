Name: ${name}
BuildArch: noarch
Version: ${version}
Release: ${release}
Summary: ${name}
Epoch: 0
License: Apache License version 2, http://www.apache.org/licenses
Group: apache.org
Source0: ${name}-${version}.tgz
Source1: ${name}
Requires: jdk >= 1.7


%description
Installs ${name} into /usr/${name}
	
	
%pre
getent group groovy > /dev/null || groupadd -r groovy
getent passwd groovy > /dev/null || useradd -r -g groovy groovy


%post
ln -s /usr/${name}/bin/grape /usr/bin/grape
ln -s /usr/${name}/bin/groovy /usr/bin/groovy
ln -s /usr/${name}/bin/groovyc /usr/bin/groovyc
ln -s /usr/${name}/bin/groovyConsole /usr/bin/groovyConsole
ln -s /usr/${name}/bin/groovyDoc /usr/bin/groovyDoc
ln -s /usr/${name}/bin/groovysh /usr/bin/groovysh
ln -s /usr/${name}/bin/java2groovy /usr/bin/java2groovy
ln -s /usr/${name}/bin/startGroovy /usr/bin/startGroovy 

%postun
rm /usr/bin/grape
rm /usr/bin/groovy
rm /usr/bin/groovyc
rm /usr/bin/groovyConsole
rm /usr/bin/groovyDoc
rm /usr/bin/groovysh
rm /usr/bin/java2groovy
rm /usr/bin/startGroovy
	
#Uncompress files to BUILD
%prep
%setup -c -q


#Configure/Compile files in BUILD
%install
rm -rf %{buildroot}
install --directory %{buildroot}/usr/${name}


cp -rf ${name}-${version}/* %{buildroot}/usr/${name}/


#This will clean up after the software is packaged
%clean
#rm -rf %{buildroot}


#Specify files to be added to the RPM
%files
%defattr(-,groovy,groovy,-)
/usr/${name}



#Specify the changes made since the last version
%changelog
* ${date} <${user}> ${version}
- Installs JDK 1.7+ 
- Installs ${name} into /usr/${name}
- Adds all ${name} binaries as symbolic links into /usr/bin