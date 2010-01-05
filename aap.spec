#
# Conditional build:
%bcond_without	doc		# don't build doc package

Summary:	A-A-P - tool to locate, download, build and install software
Summary(pl.UTF-8):	A-A-P - narzędzie do ściągania, budowania i instalowania oprogramowania
Name:		aap
Version:	1.091
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/a-a-p/%{name}-%{version}.zip
# Source0-md5:	6c7820e7596bd5be5cde29030d3cdf3b
Patch0:		%{name}-FHS.patch
URL:		http://www.a-a-p.org/
BuildRequires:	python >= 1:2.3
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	python >= 1:2.3
BuildArch:	noarch
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

%package doc
Summary:	HTML Documentation for A-A-P
Group:		Documentation

%description doc
HTML Documentation for A-A-P.

%prep
%setup -qc
%patch0 -p1
grep -r env.python -l . | xargs %{__sed} -i -e '1s,#!.*bin/env python,#!%{__python},'

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}

./aap install \
	PREFIX=$RPM_BUILD_ROOT%{_prefix}

ln -snf %{_datadir}/%{name}/aap $RPM_BUILD_ROOT%{_bindir}/aap

%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}}/%{name}/tools
%py_postclean %{_datadir}/%{name}

rm -rf $RPM_BUILD_ROOT%{_datadir}/%{name}/{doc,README.txt,COPYING}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/aap
%dir %{_datadir}/%{name}
%attr(755,root,root) %{_datadir}/%{name}/aap
%{_datadir}/%{name}/*.py[co]
%{_datadir}/%{name}/default.aap
%{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/tools
%{_datadir}/%{name}/tools/*.py[co]
%{_mandir}/man1/aap.1*

%if %{with doc}
%files doc
%defattr(644,root,root,755)
%doc doc/{*.html,*.pdf,images}
%endif
