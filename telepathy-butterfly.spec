# TODO
# - try system waf
Summary:	A Telepathy connection manager for MSN
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla MSN
Name:		telepathy-butterfly
Version:	0.5.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-butterfly/%{name}-%{version}.tar.gz
# Source0-md5:	3cedf582597ebe742fe7c05fc6ec8943
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-papyon >= 0.4.2
Requires:	python-telepathy >= 0.15.11
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to MSN.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z MSN.

%prep
%setup -q

%build
%ifarch %{x8664}
PYTHONDIR=%{py_sitedir} \
%endif
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir}
./waf build

%install
rm -rf $RPM_BUILD_ROOT

./waf --destdir=$RPM_BUILD_ROOT install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/telepathy-butterfly
%{_datadir}/telepathy/managers/butterfly.manager
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.butterfly.service
%dir %{py_sitedir}/butterfly
%{py_sitedir}/butterfly/*.py[co]
%dir %{py_sitedir}/butterfly/channel
%{py_sitedir}/butterfly/channel/*.py[co]
%dir %{py_sitedir}/butterfly/util
%{py_sitedir}/butterfly/util/*.py[co]
%dir %{py_sitedir}/butterfly/media
%{py_sitedir}/butterfly/media/*.py[co]
