# TODO:
#   - Make /usr/lib/hk_classes/drivers as default driver dir.
#   - Check if linking with libXrender.la is OK - I'm not sure.
#   - Check/fix Patch0

Summary:	knoda - MySQL/PostgreSQL/any ODBC DB GUI for KDE
Summary(pl):	knoda - Graficzny interejs do baz MySQL/PostgreSQL/ODBC dla KDE
Name:		knoda
Version:	0.7.3
Release:	1
License:	GPL
Group:		Applications/Databases
Source0:	http://dl.sourceforge.net/knoda/%{name}-%{version}.tar.bz2
# Source0-md5:	035790b0ff64451cc6ed2ba71aff0c5d
# Patch0:		%{name}-desktop.patch
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
ÀÃ…≈Œ‘ MySQL/PostgreSQL ƒÃ— KDE.

#%%package -n python-hk_kdeclasses
#Summary:        Python interface to knoda 
#Summary(pl):    Interfejs do knoda dla jÍzyka Python
#Group:          Development/Libraries
#Requires:       %{name} = %{version}-%{release}
#%pyrequires_eq	python-libs

#%%description -n python-hk_kdeclasses
# Python inteface to knoda and hk_kdeclasses used by knoda.

#%%description -n python-hk_kdeclasses -l pl
#Pythonowy interfejs do programu knoda i uøywanych przez niego
#klass hk_kdeclasses.

%prep
%setup -q
# %%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
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
%{_datadir}/mimelnk/application/*.desktop
%{_desktopdir}/kde/*.desktop
%{_iconsdir}/hicolor/*/*/*.png

# hk_kdeclasses-devel
# %{_includedir}/hk_kde*.h

#%%files -n python-hk_kdeclasses
#%%defattr(644,root,root,755)
#%%{py_sitedir}/hk_kdeclasses.py[co]
#%%attr(755,root,root) %{py_sitedir}/_hk_kdeclasses.so
