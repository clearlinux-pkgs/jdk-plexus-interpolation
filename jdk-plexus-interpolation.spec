#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : jdk-plexus-interpolation
Version  : 1.22
Release  : 2
URL      : https://github.com/sonatype/plexus-interpolation/archive/plexus-interpolation-1.22.tar.gz
Source0  : https://github.com/sonatype/plexus-interpolation/archive/plexus-interpolation-1.22.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: jdk-plexus-interpolation-data
BuildRequires : apache-maven
BuildRequires : apache-maven2
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-collections
BuildRequires : jdk-commons-compress
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-doxia
BuildRequires : jdk-doxia-sitetools
BuildRequires : jdk-forge-parent
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-hamcrest
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jdom
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-junit4
BuildRequires : jdk-log4j
BuildRequires : jdk-maven-archiver
BuildRequires : jdk-maven-common-artifact-filters
BuildRequires : jdk-maven-compiler-plugin
BuildRequires : jdk-maven-filtering
BuildRequires : jdk-maven-invoker
BuildRequires : jdk-maven-jar-plugin
BuildRequires : jdk-maven-javadoc-plugin
BuildRequires : jdk-maven-plugin-tools
BuildRequires : jdk-maven-reporting-api
BuildRequires : jdk-maven-resources-plugin
BuildRequires : jdk-maven-shared-incremental
BuildRequires : jdk-maven-shared-utils
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus
BuildRequires : jdk-plexus-archiver
BuildRequires : jdk-plexus-build-api
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-cli
BuildRequires : jdk-plexus-compiler
BuildRequires : jdk-plexus-components
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-i18n
BuildRequires : jdk-plexus-interactivity
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-io
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-plexus-velocity
BuildRequires : jdk-qdox
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-snappy-java
BuildRequires : jdk-surefire
BuildRequires : jdk-velocity
BuildRequires : jdk-wagon
BuildRequires : jdk-xbean
BuildRequires : jdk-xmlunit
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn

%description
No detailed description available

%package data
Summary: data components for the jdk-plexus-interpolation package.
Group: Data

%description data
data components for the jdk-plexus-interpolation package.


%prep
%setup -q -n plexus-interpolation-plexus-interpolation-1.22

python3 /usr/share/java-utils/pom_editor.py pom_remove_plugin  :maven-release-plugin
python3 /usr/share/java-utils/mvn_file.py : plexus/interpolation

%build
python3 /usr/share/java-utils/mvn_build.py

%install
xmvn-install  -R .xmvn-reactor -n plexus-interpolation -d %{buildroot}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/plexus/interpolation.jar
/usr/share/maven-metadata/plexus-interpolation.xml
/usr/share/maven-poms/plexus/interpolation.pom
