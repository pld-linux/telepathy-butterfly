Summary:	A Telepathy connection manager for MSN
Summary(pl.UTF-8):	Zarządca połączeń Telepathy dla MSN
Name:		telepathy-butterfly
Version:	0.1.4
Release:	1
License:	LGPL
Group:		Libraries
Source0:	http://telepathy.freedesktop.org/releases/telepathy-butterfly/%{name}-%{version}.tar.gz
# Source0-md5:	1f7cdbbdd45a85695931839b33bd6863
URL:		http://telepathy.freedesktop.org/wiki/
BuildRequires:	python
BuildRequires:	rpm-pythonprov
Requires:	python-pymsn
Requires:	telepathy-python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A connection manager to connect Telepathy to MSN.

%description -l pl.UTF-8
Zarządca połączeń pozwalający połączyć się Telepathy z MSN.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
        --root=$RPM_BUILD_ROOT \
        --optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/telepathy-butterfly
%{_datadir}/telepathy/managers/butterfly.manager
%{_datadir}/dbus-1/services/org.freedesktop.Telepathy.ConnectionManager.butterfly.service
%dir %{py_sitescriptdir}/TelepathyButterfly
%{py_sitescriptdir}/TelepathyButterfly/*.py[co]
