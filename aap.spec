Summary:	A-A-P - tool to locate, download, build and install software
Summary(pl):	A-A-P - narzêdzie do ¶ci±gania, budowania i instalowania oprogramowania
Name:		aap
Version:	1.088
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/a-a-p/%{name}-%{version}.zip
# Source0-md5:	11ae7f4a6f77f03ab319a17e7728efdc
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

%description -l pl
A-A-P u³atwia odnajdowanie, ¶ci±ganie, budowanie i instalowanie
oprogramowania. Wspiera tak¿e przegl±danie kodu ¼ród³owego, tworzenie
programów, zarz±dzanie ró¿nymi wersjami oraz dystrybucjê
oprogramowania i dokumentacji. Oznacza to, ¿e A-A-P jest przydatny
zarówno dla u¿ytkowników, jak i programistów.

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
