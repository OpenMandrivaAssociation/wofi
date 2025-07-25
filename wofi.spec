Name:		wofi
Summary:	A launcher/menu for wlroots based wayland compositors
Version:	1.4.1
Release:	1
License:	GPLv3
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:	%{URL}/archive/%{name}-v%{version}.tar.gz
 
BuildRequires:	meson
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(wayland-client)
 
%description
A launcher/menu for wlroots based wayland compositors.
 
%package devel
Summary: Development package for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}
 
%description devel
Files for development with %{name}.
 
%prep
%autosetup -n %{name}-v%{version} -p1
 
%build
%meson
%meson_build

%install
%meson_install

%files
%license COPYING.md
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/wofi.1*
%{_mandir}/man5/wofi.5*
%{_mandir}/man7/wofi-keys.7*
%{_mandir}/man7/wofi.7*
 
%files devel
%{_includedir}/wofi-1/*.h
%{_libdir}/pkgconfig/wofi.pc
%{_mandir}/man3/wofi-api.3*
%{_mandir}/man3/wofi-config.3*
%{_mandir}/man3/wofi-map.3*
%{_mandir}/man3/wofi-utils.3*
%{_mandir}/man3/wofi-widget-builder.3*
%{_mandir}/man3/wofi.3*
