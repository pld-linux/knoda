# TODO:
#   - Check if linking with libXrender.la is OK - I'm not sure.
#   - Check/fix Patch0
#
Summary:	knoda - MySQL/PostgreSQL/any ODBC DB GUI for KDE
Summary(pl.UTF-8):   knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/knoda/%{name}-%{version}.tar.gz
# Source0-md5:	c5cef874a0d3edf8af8b74f577b88dcb
Patch0:		%{name}-desktop.patch
URL:		http://knoda.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	hk_classes-devel >= %{version}
BuildRequires:	libtool
BuildRequires:	kdelibs-devel
# withdrawn?
BuildRequires:	xrender-devel
BuildRequires:	rpmbuild(macros) >= 1.129
# NOTE: knoda 0.7 has link errors when used with hk_classes 0.7.2  
Requires:	hk_classes = %{version}
Requires:	%{name}-common = %{version}-%{release}
Obsoletes:	python-hk_kdeclasses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE-based frontend for MySQL/PostgreSQL/ODBC DB.

%description -l pl.UTF-8
Graficzny interfejs do baz MySQL/PostgreSQL/ODBC dla KDE.

%description -l ru.UTF-8
клиент MySQL/PostgreSQL для KDE.

%package rt
Summary:	Knoda locked down database front end for corp use
Summary(pl.UTF-8):   Knoda - zablokowany frontend bazy danych dla użytku korporacyjnego
Group:		Applications/Databases
Requires:	%{name}-common = %{version}-%{release}

%description rt
Knoda locked down database front end for corp use.

%description rt -l pl.UTF-8
Knoda - zablokowany frontend bazy danych do użytku korporacyjnego.

%package common
Summary:	Knoda - common part for knoda and knoda-rt
Summary(pl.UTF-8):   Knoda - wspólna część dla knoda i knoda-rt
Group:		Applications/Databases

%description common
Knoda - common part for knoda and knoda-rt.

%description common -l pl.UTF-8
Knoda - wspólna część dla knoda i knoda-rt.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir} \
        kdelnkdir=%{_desktopdir}/kde

rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post   common -p /sbin/ldconfig
%postun common -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda
%{_desktopdir}/kde/knoda.desktop

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda-rt

%files common -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhk_kde*.so
%attr(755,root,root) %{_libdir}/kde3/libhk_*.so
%{_libdir}/kde3/libhk_*.la
%{_datadir}/apps/hk_kdeclasses
%{_datadir}/apps/knoda
%{_datadir}/services/*.desktop
%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
