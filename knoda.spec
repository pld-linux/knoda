# TODO:
#   - Make /usr/lib/hk_classes/drivers as default driver dir.
#   - Check if linking with libXrender.la is OK - I'm not sure.
#   - Check/fix Patch0
#
Summary:	knoda - MySQL/PostgreSQL/any ODBC DB GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.7.4
Release:	2
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/knoda/%{name}-%{version}.tar.bz2
# Source0-md5:	048c550d6749fcf8f980883af87e9ec4
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
Obsoletes:	python-hk_kdeclasses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE-based frontend for MySQL/PostgreSQL/ODBC DB.

%description -l pl
Graficzny interfejs do baz MySQL/PostgreSQL/ODBC dla KDE.

%description -l ru
клиент MySQL/PostgreSQL для KDE.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir} \
        kdelnkdir=%{_desktopdir}/kde

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
%{_datadir}/mimelnk/application/*.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/*/*.png
