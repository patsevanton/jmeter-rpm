%define name jmeter
%define jdk %{_prefix}/lib/jvm/java-openjdk

Summary:	JMeter for testing Web Applications
Name:		apache-%{name}
Version:	3.0
Release:	1
License:	ASL2.0
Group:		Development/Other
Url:		http://jmeter.apache.org/
Source:		https://archive.apache.org/dist/jmeter/source/%{name}-%{version}_src.tgz
BuildRequires:	ant
BuildRequires:	java-devel
Requires:	java >= 1.6
BuildArch:	noarch

%description
Apache JMeter may be used to test performance both
on static and dynamic resources (Webservices (SOAP/REST),
Web dynamic languages - PHP, Java, ASP.NET, Files, etc. -,
Java Objects, Data Bases and Queries, FTP Servers and more).
It can be used to simulate a heavy load on a server,
group of servers, network or object to test its strength
or to analyze overall performance under different load types.
You can use it to make a graphical analysis of performance
or to test your server/script/object behavior under
heavy concurrent load.

%files
%doc README LICENSE
%{_bindir}/%{name}
%{_datadir}/%{name}/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build
ant download_jars
JAVA_HOME=%{jdk} ant

%install
#ant install
mkdir -p %{buildroot}%{_datadir}/%{name}/lib
mkdir -p %{buildroot}%{_datadir}/%{name}/bin
mkdir -p %{buildroot}%{_datadir}/%{name}/bin/examples
mkdir -p %{buildroot}%{_datadir}/%{name}/bin/templates
mkdir -p %{buildroot}%{_datadir}/%{name}/bin/testfiles

cp -r lib/* %{buildroot}%{_datadir}/%{name}/lib

install -Dm0755 bin/%{name}		%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0755 bin/*server		%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0755 bin/*.sh		%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0644 bin/*.properties	%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0644 bin/*.conf		%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0644 bin/ApacheJMeter.jar	%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0644 bin/*.xml		%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0644 bin/*.parameters	%{buildroot}%{_datadir}/%{name}/bin/
install -Dm0644 bin/*.bshrc		%{buildroot}%{_datadir}/%{name}/bin/

cp -r bin/examples/*			%{buildroot}%{_datadir}/%{name}/bin/examples/
cp -r bin/templates/*			%{buildroot}%{_datadir}/%{name}/bin/templates/
cp -r bin/testfiles/*			%{buildroot}%{_datadir}/%{name}/bin/testfiles/

mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf ../..%{_datadir}/%{name}/bin/%{name} %{name}
popd
