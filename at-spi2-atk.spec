Summary:	A GTK+ module that bridges ATK to D-Bus at-spi
Name:		at-spi2-atk
Version:	2.8.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/at-spi2-atk/2.8/%{name}-%{version}.tar.xz
# Source0-md5:	90b617bd811f8dbc3e138e87294b22d4
URL:		http://www.linuxfoundation.org/en/AT-SPI_on_D-Bus
BuildRequires:	at-spi2-core-devel
BuildRequires:	atk-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-devel
BuildRequires:	gettext-devel
BuildRequires:	glib-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
Requires:	%{name}-libs = %{version}-%{release}
Requires:	at-spi2-core
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a GTK+ module that bridges ATK to the new D-Bus
based at-spi.

%package libs
Summary:	atk-bridge library
Group:          Libraries

%description libs
atk-bridge library.

%package devel
Summary:	Header files for atk-bridge library
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files for atk-bridge library.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/gtk-*/modules/libatk-bridge.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/gtk-2.0/modules/libatk-bridge.so
%{_libdir}/gnome-settings-daemon-3.0/gtk-modules/at-spi2-atk.desktop

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libatk-bridge-2.0.so.?
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libatk-bridge-2.0.so
%{_includedir}/at-spi2-atk
%{_pkgconfigdir}/atk-bridge-2.0.pc

