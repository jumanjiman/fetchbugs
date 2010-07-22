%define MANDIR /usr/share/man/man1/
Name: fetchbugs
Version: 0.3
Release: 6
BuildArch: noarch
License: GPL v2
Group: Applications/Publishing
Group: Administration
Packager: Paul Morgan <jumanjiman@gmail.com>
Summary: Command-line utility to fetch bug descriptions from a Bugzilla web site
Source: %{name}-%{version}.tgz
BuildRoot: /tmp/%{name}-%{version}-%{release}
BuildRequires: elinks, gzip
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
gzip src/fetchbugs.1

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}%{MANDIR}
install -m755 src/fetchbugs %{buildroot}/usr/local/bin
install -m644 src/fetchbugs.1.gz %{buildroot}%{MANDIR}

%files
%defattr(-,root,root)
/usr/local/bin/fetchbugs
%doc src/README
%doc src/COPYING
%doc %{MANDIR}/fetchbugs.1.gz

%changelog
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
