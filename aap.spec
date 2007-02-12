Summary:	A-A-P - tool to locate, download, build and install software
Summary(pl.UTF-8):   A-A-P - narzędzie do ściągania, budowania i instalowania oprogramowania
Name:		aap
Version:	1.089
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/a-a-p/%{name}-%{version}.zip
# Source0-md5:	31774a075f08c7a363debedbf6fa6a39
URL:		http://www.a-a-p.org/
BuildRequires:	python >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	python >= 1:2.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A-A-P makes it easy to locate, download, build and install software.
It also supports browsing source code, developing programs, managing
different versions and distribution of software and documentation.
This means that A-A-P is useful both for users and for developers.

%description -l pl.UTF-8
A-A-P ułatwia odnajdowanie, ściąganie, budowanie i instalowanie
oprogramowania. Wspiera także przeglądanie kodu źródłowego, tworzenie
programów, zarządzanie różnymi wersjami oraz dystrybucję
oprogramowania i dokumentacji. Oznacza to, że A-A-P jest przydatny
zarówno dla użytkowników, jak i programistów.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/share

./aap install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

mv -f $RPM_BUILD_ROOT%{_prefix}/man $RPM_BUILD_ROOT%{_mandir}
ln -snf %{_prefix}/lib/aap/Exec-%{version}/aap $RPM_BUILD_ROOT%{_bindir}/aap

%py_ocomp $RPM_BUILD_ROOT%{_prefix}/lib/aap/Exec-%{version}
%py_ocomp $RPM_BUILD_ROOT%{_prefix}/lib/aap/Exec-%{version}/tools

rm -rf $RPM_BUILD_ROOT%{_prefix}/lib/aap/Exec-%{version}/{doc,README.txt,COPYING,*.py,tools/*.py,doc}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{*.html,*.pdf,images}
%attr(755,root,root) %{_bindir}/aap
%dir %{_prefix}/lib/aap
%dir %{_prefix}/lib/aap/Exec-%{version}
%attr(755,root,root) %{_prefix}/lib/aap/Exec-%{version}/aap
%{_prefix}/lib/aap/Exec-%{version}/*.py[co]
%{_prefix}/lib/aap/Exec-%{version}/default.aap
%{_prefix}/lib/aap/Exec-%{version}/modules
%dir %{_prefix}/lib/aap/Exec-%{version}/tools
%{_prefix}/lib/aap/Exec-%{version}/tools/*.py[co]
%{_mandir}/man1/aap.1*
