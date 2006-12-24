# TODO:
#   - Check if linking with libXrender.la is OK - I'm not sure.
#   - Check/fix Patch0
#
Summary:	knoda - MySQL/PostgreSQL/any ODBC DB GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.8.2
Release:	0.1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/knoda/%{name}-%{version}.tar.gz
# Source0-md5:	32c2b95778c9ebc4ff212cf268d1e1c2
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
knoda is a KDE-database frontend based on the hk_classes library.

%description -l pl
knoda jest graficznym interfejsem KDE baz danych opartym
na bibliotece classes.

%description -l ru
ËÌÉÅÎÔ MySQL/PostgreSQL ÄÌÑ KDE.

%package rt
Summary:	Knoda locked down database front end for corp use
Summary(pl):	Knoda - zablokowany frontend bazy danych dla u¿ytku korporacyjnego
Group:		Applications/Databases
Requires:	%{name}-common = %{version}-%{release}

%description rt
Knoda locked down database front end for corp use.

%description rt -l pl
Knoda - zablokowany frontend bazy danych do u¿ytku korporacyjnego.

%package common
Summary:	Knoda - common part for knoda and knoda-rt
Summary(pl):	Knoda - wspólna czê¶æ dla knoda i knoda-rt
Group:		Applications/Databases
Requires:	hk_kdeclasses = %{version}-%{release}

%description common
Knoda - common part for knoda and knoda-rt.

%description common -l pl
Knoda - wspólna czê¶æ dla knoda i knoda-rt.

%package -n hk_kdeclasses
Summary:	hk_kdeclasses libraries
Summary(pl):	Biblioteki hk_kdeclasses
Group:		Development/Libraries

%description -n hk_kdeclasses
hk_kdeclasses libraries.

%description -n hk_kdeclasses -l pl
Biblioteki hk_kdeclasses.

%package -n hk_kdeclasses-devel
Summary:	hk_kdeclasses headers
Summary(pl):	Nag³ówki hk_kdeclasses
Group:		Development/Libraries
Requires:	hk_kdeclasses = %{version}-%{release}

%description -n hk_kdeclasses-devel
hk_kdeclasses headers.

%description -n hk_kdeclasses-devel -l pl
Nag³ówki hk_kdeclasses.

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

%post	-n hk_kdeclasses -p /sbin/ldconfig
%postun	-n hk_kdeclasses -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda
%{_desktopdir}/kde/knoda.desktop

%files rt
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knoda-rt

%files common -f %{name}.lang
%defattr(644,root,root,755)
%{_datadir}/apps/knoda
%{_datadir}/mimelnk/application/*.desktop
%{_iconsdir}/hicolor/*/*/*.png

%files -n hk_kdeclasses
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libhk_kde*.so
%attr(755,root,root) %{_libdir}/kde3/libhk_*.so
%{_libdir}/kde3/libhk_*.la
%{_datadir}/apps/hk_kdeclasses
%{_datadir}/services/*.desktop
#%%{_datadir}/config/magic/hk_classes.magic ???

%files -n hk_kdeclasses-devel
%defattr(644,root,root,755)
%{_includedir}/*
