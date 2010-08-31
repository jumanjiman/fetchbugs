Name: fetchbugs
Version: 0.3
Release: 14
BuildArch: noarch
License: GPL v2
Group: Applications/Publishing
Group: Administration
Packager: Paul Morgan <jumanjiman@gmail.com>
Summary: Command-line utility to fetch bug descriptions from a Bugzilla web site
Source: %{name}-%{version}.tar.gz
BuildRoot: /tmp/%{name}-%{version}-%{release}

BuildRequires: elinks
buildrequires: gzip
buildrequires: asciidoc

Requires: elinks

%description
fetchbugs is a command-line utility to retrieve detailed
bug descriptions from a Bugzilla instance. It provides
several options to tailor your query.

%clean
if [ "%{buildroot}" = "/" ]; then
  /bin/echo 'Hey numskull. Fix your BUILDROOT!' >&2
  exit 3
else
  rm -fr "%{buildroot}"
fi

# -----------------------------------------------

%prep
if [ "%{buildroot}" = "/" ]; then
  /bin/echo 'Hey numskull. Fix your BUILDROOT!' >&2
  exit 3
else
  rm -fr "%{buildroot}"
fi
%setup -n %{name}-%{version}

# -----------------------------------------------

%build
# convert manpage
/usr/bin/a2x -d manpage -f manpage doc/fetchbugs.1.asciidoc


%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}%{_mandir}/man1
install -m755 src/fetchbugs %{buildroot}/usr/local/bin
%{__gzip} -c doc/fetchbugs.1 > %{buildroot}/%{_mandir}/man1/fetchbugs.1.gz


%files
%defattr(-,root,root)
/usr/local/bin/fetchbugs
%doc README.asciidoc
%doc doc/COPYING
%doc %{_mandir}/man1/fetchbugs.1.gz

%changelog
* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-14
- fix typo

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-13
- moved COPYING to doc/ in repo

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-12
- moved manpage to doc/ in repo
- clarification in man page
- minor cleanup and clarification of readme

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-11
- convert manpage source to asciidoc

* Thu Jul 22 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-10
- moved README from src to root of tree

* Thu Jul 22 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-9
- updated source spec for tito

* Thu Jul 22 2010 Paul Morgan 0.3-8
- fixed build section of spec to account for new src/ subdir

* Thu Jul 22 2010 Paul Morgan <pmorgan@redhat.com> 0.3-7
- new package built with tito

* Sat Oct 18 2008 Paul Morgan <jumanjiman@gmail.com>
- Cleaned up man page

* Wed Jan 16 2008 Paul Morgan <jumanjiman@gmail.com>
- Added a man page, but man page needs cleanup

* Mon Jan 14 2008 Paul Morgan <jumanjiman@gmail.com>
- Added a -p option for priority (bug_severity)

* Sun Jan 13 2008 Paul Morgan <jumanjiman@gmail.com>
- Updated to version 0.2
- now sorts by component plus new command-line options

* Sun Jan 13 2008 Paul Morgan <jumanjiman@gmail.com>
- Initial packaging
