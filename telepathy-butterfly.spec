Summary:	A Telepathy connection manager for MSN
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla MSN
Name:		telepathy-butterfly
Version:	0.5.14
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-butterfly/%{name}-%{version}.tar.gz
# Source0-md5:	d7ef545a469a0b0fd87a0988ed7d9b13
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-papyon >= 0.4.2
Requires:	python-telepathy >= 0.15.17
Suggests:	python-libproxy
Conflicts:	empathy < 2.29.92
# we install to %{_libdir}, otherwise package could be noarch
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to MSN.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z MSN.

%prep
%setup -q

%build
%configure \
	--host=%{_target} \
	--build=%{_target}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_libdir}/telepathy-butterfly
%{_datadir}/telepathy/managers/butterfly.manager
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.butterfly.service
%dir %{py_sitescriptdir}/butterfly
%{py_sitescriptdir}/butterfly/*.py[co]
%dir %{py_sitescriptdir}/butterfly/channel
%{py_sitescriptdir}/butterfly/channel/*.py[co]
%dir %{py_sitescriptdir}/butterfly/util
%{py_sitescriptdir}/butterfly/util/*.py[co]
%dir %{py_sitescriptdir}/butterfly/media
%{py_sitescriptdir}/butterfly/media/*.py[co]
