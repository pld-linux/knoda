# TODO:
#   - Add docs part
#   - Consider packaging hk_kdeclasses separately if any other app would use hk_kdeclasses
#   - Add icon 
#   - Place in proper place in menu.

Summary:	knoda - MySQL/PostgreSQL/any ODBC DB  GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.5.5
Release:	0.9
License:	GPL
Group:		X11/Applications/Databases
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
URL:		http://knoda.sourceforge.net/
BuildRequires:  hk_classes-devel >= %{version}
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
KDE-based frontend for MySQL/PostgreSQL/ODBC DB.

%description -l pl
Graficzny interfejs do baz MySQL/PostgreSQL/ODBC dla KDE.

%description -l ru
клиент MySQL/PostgreSQL для KDE.

%prep
%setup -q

%build
#%%{__autoconf}
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install
#mv $RPM_BUILD_ROOT/usr/share/* $RPM_BUILD_ROOT/usr/X11R6/share/

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda
%attr(755,root,root) %{_libdir}/libhk_kdeclasses.so.*.*
%{_datadir}/apps/hk_kdeclasses
%{_datadir}/apps/knoda
%{_datadir}/services/*.desktop
%{_applnkdir}/Office/*.desktop
%{_pixmapsdir}/*/*/apps/knoda.png

# hk_kdeclasses-devel?
# %attr(755,root,root) %{_libdir}/libhk_kdeclasses.so
# %{_libdir}/libhk_kdeclasses.la
# %{_includedir}/hk_kde*.h
