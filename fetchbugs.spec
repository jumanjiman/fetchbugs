Name: fetchbugs
Version: 0.5
Release: 1%{?dist}
License: GPL v2
Group: Applications/Productivity
Summary: Command-line utility to fetch bug descriptions from a Bugzilla web site
Source: %{name}-%{version}.tar.gz

BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
buildarch: noarch

BuildRequires: elinks
buildrequires: gzip
buildrequires: asciidoc
buildrequires: redhat-rpm-config

Requires: elinks

%description
fetchbugs is a command-line utility to retrieve detailed
bug descriptions from a Bugzilla instance. It provides
several options to tailor your query.

%prep
%setup -q


%clean
%{__rm} -rf %{buildroot}


%build
# convert manpage
/usr/bin/a2x -d manpage -f manpage doc/fetchbugs.1.asciidoc



%install
%{__rm} -rf %{buildroot}

# executable
%{__mkdir_p} %{buildroot}/%{_bindir}
%{__install} -p  -m755 src/fetchbugs %{buildroot}/%{_bindir}

# manpage
%{__mkdir_p} %{buildroot}%{_mandir}/man1
%{__gzip} -c doc/fetchbugs.1 > %{buildroot}/%{_mandir}/man1/fetchbugs.1.gz




%files
%defattr(-,root,root)

# executable
%{_bindir}/fetchbugs

# documentation
%doc README.asciidoc
%doc doc/COPYING
%doc %{_mandir}/man1/fetchbugs.1.gz




%changelog
* Sun Oct 03 2010 Paul Morgan <jumanjiman@gmail.com> 0.5-1
- clean up spec (jumanjiman@gmail.com)
- changed default_tagger to VersionTagger (jumanjiman@gmail.com)
- removed bogus changelog entries from spec (jumanjiman@gmail.com)

* Mon Aug 30 2010 Paul Morgan <jumanjiman@gmail.com> 0.3-17
- cleanup spec file

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
