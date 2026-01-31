%global debug_package %{nil}

%define logo_filename proton-vpn-logo.svg
%define desktop_entry_filename proton.vpn.app.gtk.desktop
%define _unpackaged_files_terminate_build 0

Prefix:	%{_prefix}

Name:		proton-vpn-gtk-app
Version:	4.14.0
Release:	1
Source0:	https://github.com/ProtonVPN/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Official ProtonVPN Linux app
URL:		https://github.com/ProtonVPN/proton-vpn-gtk-app
License:	GPL
Group:		Networking
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	python-gobject3
BuildRequires:	python%{pyver}dist(pygobject)
BuildRequires:	python%{pyver}dist(dbus-python)
BuildRequires:	python%{pyver}dist(packaging)
BuildRequires:	python%{pyver}dist(proton-core)
BuildRequires:	python%{pyver}dist(proton-vpn-api-core)
BuildRequires:	python%{pyver}dist(setuptools)

Requires:	pkgconfig(gtk+-3.0)
Requires:	pkgconfig(libnotify)
Requires:	pkgconfig(librsvg-2.0)
Requires:	lib64gdkx11-gir3.0
Requires:	lib64notify-gir0.7
Requires:	python-gobject3
Requires:	python%{pyver}dist(dbus-python)
Requires:	python%{pyver}dist(proton-vpn-api-core)
Requires:	python%{pyver}dist(packaging)

%description
Official ProtonVPN Linux app.

The Proton VPN GTK app is intended for every Proton VPN service user,
it provides full access to all functionalities available to authenticated
users, with the user signup process handled on the website.


%prep
%autosetup -n %{name}-%{version} -p1

%build
%py_build

%install
%py_install

install -Dm0644 rpmbuild/SOURCES/%{logo_filename} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{logo_filename}
desktop-file-install --dir=%{buildroot}%{_datadir}/applications rpmbuild/SOURCES/%{desktop_entry_filename}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{desktop_entry_filename}

%files
%{py_sitedir}/proton
%{py_sitedir}/proton_vpn_gtk_app-*.egg-info
%{_bindir}/protonvpn-app
%{_datadir}/applications/%{desktop_entry_filename}
%{_datadir}/icons/hicolor/scalable/apps/%{logo_filename}
