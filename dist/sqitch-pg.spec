Name:           sqitch-pg
Version:        0.911
Release:        1%{?dist}
Summary:        Sane PostgreSQL database change management
License:        MIT
Group:          Development/Libraries
URL:            http://sqitch.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:       sqitch >= 0.911
Requires:       postgresql91
Requires:       perl(DBI)
Requires:       perl(DBD::Pg)

%description
Sqitch provides a simple yet robust interface for database change
management. The philosophy and functionality is inspired by Git. This
package bundles the Sqith PostgreSQL support.

%prep

%build

%install

%check

%clean

%files

%changelog
* Wed Aug 23 2012 David E. Wheeler <david.wheeler@iovation.com> 0.911-1
- Upgrade to v0.911.

* Wed Aug 22 2012 David E. Wheeler <david.wheeler@iovation.com> 0.91-1
- Upgrade to v0.91.

* Mon Aug 20 2012 David E. Wheeler <david.wheeler@iovation.com> 0.902-1
- Upgrade to v0.902.

* Mon Aug 20 2012 David E. Wheeler <david.wheeler@iovation.com> 0.901-1
- Upgrade to v0.901.

* Sat Aug 04 2012 David E. Wheeler <david.wheeler@iovation.com> 0.82-1
- First release.
