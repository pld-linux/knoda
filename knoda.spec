# TODO:
# - Bails out with message:
# Fatal error: File 'knodaui.rc' could not be located. Probably Knoda is installed incorrectly
# Are you sure you have used
# ./configure --prefix=/your_KDE_directory ? 
# See the documentation for details. 

Name:		knoda
Summary:	knoda -- MySQL GUI for KDE
Summary(pl):knoda - Graficzny interejs do baz MySQL/Postgersql dla KDE  
Version:	0.5.4
Release:	1.1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz

# Currently hk_classes contains all in one.
BuildRequires:  hk_classes >= 0.5.4

BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE-based frontend for MySQL


%description -l ru
клиент MySQL для KDE

%description -l pl
Graficzny interejs do baz MySQL/Postgersql dla KDE

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
#%{__autoconf}
%configure
#./configure --prefix=%{_prefix} --with-hk_classes-dir=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install
# find . -type f -o -type l | sed 's|^\.||' > $RPM_BUILD_ROOT/master.list

%clean
rm -rf $RPM_BUILD_ROOT

# %files -f %{_tmppath}/%{name}-buildroot/master.list
%files
%defattr(644,root,root,755)

%attr (-,root,root) /*
