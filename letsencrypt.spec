Summary:	A free, automated certificate authority client
Name:		letsencrypt
Version:	0.4.1
Release:	1
License:	ASL 2.0
Group:		System/Base
URL:		https://letsencrypt.org/
Source0:	https://pypi.python.org/packages/source/l/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python2)
#Require for testing
BuildRequires:	python-nose-xcover
BuildRequires:	python-pep8
BuildRequires:	python-tox
BuildRequires:	python2-mock
BuildRequires:	python-configargparse >= 0.10.0
BuildRequires:	python-zope-interface
BuildRequires:	python-zope-component
BuildRequires:	python-requests
BuildRequires:	python2-dialog >= 3.3.0
BuildRequires:	python-psutil >= 2.1.0
BuildRequires:	python-parsedatetime
BuildRequires:	python-configobj
BuildRequires:	python2-configargparse >= 0.10.0
BuildRequires:	python2-acme = %{version}
BuildRequires:	python-werkzeug
BuildArch:	noarch
Requires:	python2-letsencrypt = %{EVRD}

%description
Let's Encrypt is a free, automated certificate authority that aims
to lower the barriers to entry for encrypting all HTTP traffic on the internet.

%package -n python2-letsencrypt
Summary:	Python 2 libraries used by %{name}
Group:		System/Base



Requires:	python2-mock
Requires:	python-zope-interface
Requires:	python-psutil >= 2.1.0
Requires:	python-configobj
# (tpg) these are missing
#Requires:	python2-acme = %{version}
#Requires:	python-zope-component
#Requires:	python-parsedatetime
#Requires:	python2-dialog >= 3.3.0
#Requires:	python2-configargparse >= 0.10.0

%description -n python2-letsencrypt
The python2 libraries to interface with %{name}.

%prep
%setup -q
# We are using letsencrypt and not supporting letsencrypt-auto
sed -i 's/letsencrypt-auto/letsencrypt/g' letsencrypt/cli.py

%build
CFLAGS="%{optflags}" %{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}}

%check
%{__python2} setup.py test

%files
%license LICENSE.txt
%doc README.rst CHANGES.rst CONTRIBUTING.md
%{_bindir}/letsencrypt
%ghost %dir %{_sysconfdir}/%{name}
%ghost %dir %{_sharedstatedir}/%{name}
%ghost %dir %{_var}/log/%{name}

%files -n python2-letsencrypt
%license LICENSE.txt
%{python2_sitelib}/%{name}
%{python2_sitelib}/%{name}-%{version}*.egg-info
