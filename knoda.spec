# TODO:
#   - Check if mkdir/mv over *.desktop is OK 
#   - Make /usr/lib/hk_classes/drivers as default driver dir.

Summary:	knoda - MySQL/PostgreSQL/any ODBC DB  GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications/Databases
Source0:	http://dl.sourceforge.net/sourceforge/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	64d1fca69163da6b2df24d64f720ffb7
URL:		http://knoda.sourceforge.net/
BuildRequires:  hk_classes-devel >= %{version}
BuildRequires:	kdelibs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KDE-based frontend for MySQL/PostgreSQL/ODBC DB.

%description -l pl
Graficzny interfejs do baz MySQL/PostgreSQL/ODBC dla KDE.

%description -l ru
клиент MySQL/PostgreSQL для KDE.

%prep
%setup -q

%build

%define         _prefix         /usr/X11R6

kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

# TODO: Check if below can be done in simpler way.
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/Databases
mv $RPM_BUILD_ROOT%{_applnkdir}/Office/*.desktop $RPM_BUILD_ROOT/%{_applnkdir}/Office/Databases/

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda
%attr(755,root,root) %{_libdir}/libhk_kde*.so
# *.la _needed_. Empirically tested when trying to open table view (segfault)
%attr(755,root,root) %{_libdir}/libhk_kde*.la
%{_datadir}/apps/hk_kdeclasses
%{_datadir}/apps/knoda
%{_datadir}/services/*.desktop
%{_applnkdir}/Office/Databases/*.desktop
%{_pixmapsdir}/*/*/apps/knoda.png

# hk_kdeclasses-devel?
# %attr(755,root,root) %{_libdir}/libhk_kdeclasses.so
# %{_libdir}/libhk_kdeclasses.la
# %{_includedir}/hk_kde*.h
