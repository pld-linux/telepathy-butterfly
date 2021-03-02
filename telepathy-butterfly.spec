Summary:	A Telepathy connection manager for MSN
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla MSN
Name:		telepathy-butterfly
Version:	0.5.15
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	https://telepathy.freedesktop.org/releases/telepathy-butterfly/%{name}-%{version}.tar.gz
# Source0-md5:	4baa6337822f01d817c4b9d8fd406e82
URL:		https://telepathy.freedesktop.org/
BuildRequires:	python >= 1:2.5
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
Requires:	python-dbus
Requires:	python-pygobject >= 2
Requires:	python-papyon >= 0.5.3
Requires:	python-telepathy >= 0.15.19
Suggests:	python-libproxy
Conflicts:	empathy < 2.29.92
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to MSN.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z MSN.

%prep
%setup -q

%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' telepathy-butterfly

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/telepathy-butterfly
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
