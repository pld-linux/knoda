# TODO:
#   - Make /usr/lib/hk_classes/drivers as default driver dir.
#   - Fix build with python, module seems to be build but configure:
#     checking for Python2.3... header /usr/include/python2.3 library 
#         /usr/lib modules no
#     (...)
#     no Python support

Summary:	knoda - MySQL/PostgreSQL/any ODBC DB GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.6.3
Release:	2
License:	GPL
Group:		X11/Applications/Databases
Source0:	http://dl.sourceforge.net/knoda/%{name}-%{version}.tar.bz2
# Source0-md5:	afa3e8739e6629fbaf0ae63fae2fa08a
Patch0:		%{name}-desktop.patch
URL:		http://knoda.sourceforge.net/
BuildRequires:	automake
BuildRequires:	hk_classes-devel >= %{version}
BuildRequires:	kdelibs-devel
# withdrawn?
Obsoletes:	python-hk_kdeclasses
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KDE-based frontend for MySQL/PostgreSQL/ODBC DB.

%description -l pl
Graficzny interfejs do baz MySQL/PostgreSQL/ODBC dla KDE.

%description -l ru
ÀÃ…≈Œ‘ MySQL/PostgreSQL ƒÃ— KDE.

#%%package -n python-hk_kdeclasses
#Summary:        Python interface to knoda 
#Summary(pl):    Interfejs do knoda dla jÍzyka Python
#Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}

#%%description -n python-hk_kdeclasses
# Python inteface to knoda and hk_kdeclasses used by knoda.

#%%description -n python-hk_kdeclasses -l pl
#Pythonowy interfejs do programu knoda i uøywanych przez niego
#klass hk_kdeclasses.

%prep
%setup -q
%patch0 -p1

%build
cp -f /usr/share/automake/config.* admin
%configure
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
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/*/*.png

# hk_kdeclasses-devel?
# %{_includedir}/hk_kde*.h

#%%files -n python-hk_kdeclasses
#%%defattr(644,root,root,755)
#%%{py_sitedir}/hk_kdeclasses.py[co]
#%%attr(755,root,root) %{py_sitedir}/_hk_kdeclasses.so
