Name:           atk
Version:        2.38.1
Release:        1%{?dist}
Summary:        ATK - Accessibility Toolkit

License:        LGPL-2.0-or-later
URL:            https://wiki.gnome.org/Accessibility
Source0:        https://download.gnome.org/sources/atk/2.38/atk-%{version}.tar.xz

BuildRequires:  pkgconfig
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  gettext-devel
BuildRequires:  pkgconfig(python3)

BuildRequires:  pkgconfig(glib-2.0) >= 2.56
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gio-2.0)

# Introspection disabled for now (turn on once GI tooling is solid)
#BuildRequires:  pkgconfig(gobject-introspection-1.0)

%description
ATK (Accessibility Toolkit) provides a set of interfaces for accessibility tools
such as screen readers.

%package devel
Summary:        Development files for ATK
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
Headers and development files for ATK.

%prep
%autosetup -n %{name}-%{version}/upstream
%build
%meson --wipe \
  --buildtype=release \
  --prefix=%{_prefix} \
  --libdir=%{_libdir} \
  -Dintrospection=false

%meson_build

%install
%meson_install

find %{buildroot}%{_libdir} -name "*.a" -delete || true

%find_lang atk10

%files -f atk10.lang
%license COPYING*
%doc NEWS* README*
%{_libdir}/libatk-1.0.so.*

%files devel
%{_includedir}/atk-1.0
%{_libdir}/libatk-1.0.so
%{_libdir}/pkgconfig/atk.pc

