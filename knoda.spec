# TODO:
#   - Make /usr/lib/hk_classes/drivers as default driver dir.

Summary:	knoda - MySQL/PostgreSQL/any ODBC DB  GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.6.2a
Release:	1
License:	GPL
Group:		X11/Applications/Databases
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	057c28b007f84904a9f12b090af7b641
URL:		http://knoda.sourceforge.net/
BuildRequires:	hk_classes-devel >= %{version}
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel
BuildRequires:	libart_lgpl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_htmldir	/usr/share/doc/kde/HTML

%description
KDE-based frontend for MySQL/PostgreSQL/ODBC DB.

%description -l pl
Graficzny interfejs do baz MySQL/PostgreSQL/ODBC dla KDE.

%description -l ru
������ MySQL/PostgreSQL ��� KDE.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir
kde_appsdir="%{_applnkdir}"; export kde_appsdir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/Databases

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Office/*.desktop $RPM_BUILD_ROOT%{_applnkdir}/Office/Databases

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda
%attr(755,root,root) %{_libdir}/libhk_kde*.so
# *.la are needed (SEGV when trying to open table view without them)
%{_libdir}/libhk_kde*.la
%attr(755,root,root) %{_libdir}/kde3/libhk_*.so
%{_libdir}/kde3/libhk_*.la
%{_datadir}/apps/hk_kdeclasses
%{_datadir}/apps/knoda
%{_datadir}/services/*.desktop
%{_applnkdir}/Office/Databases/*.desktop
%{_pixmapsdir}/*/*/apps/knoda.png

# hk_kdeclasses-devel?
# %{_includedir}/hk_kde*.h

# python-hk_kdeclasses?
# %{py_sitedir}/hk_kdeclasses.py*
# %attr(755,root,root) %{py_sitedir}/_hk_kdeclasses.so
