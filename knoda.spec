# TODO:
# - Bails out with message:
# Fatal error: File 'knodaui.rc' could not be located. Probably Knoda is installed incorrectly
# Are you sure you have used
# ./configure --prefix=/your_KDE_directory ? 
# See the documentation for details. 

Summary:	knoda - MySQL/PostgreSQL GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL dla KDE
Name:		knoda
Version:	0.5.4
Release:	1.1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  hk_classes-devel >= 0.5.4
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE-based frontend for MySQL/PostgreSQL.

%description -l pl
Graficzny interejs do baz MySQL/PostgreSQL dla KDE.

%description -l ru
клиент MySQL/PostgreSQL для KDE.

%prep
%setup -q

%build
#%{__autoconf}
%configure
#./configure --prefix=%{_prefix} --with-hk_classes-dir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# TODO
