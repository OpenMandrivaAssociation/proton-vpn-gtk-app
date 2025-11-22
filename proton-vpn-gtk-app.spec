%define logo_filename proton-vpn-logo.svg
%define desktop_entry_filename proton.vpn.app.gtk.desktop
%define upstream_version {upstream_version}
%define _unpackaged_files_terminate_build 0

Prefix:	%{_prefix}

Name:		proton-vpn-gtk-app
Version:	4.12.0
Release:	1
Source0:	https://github.com/ProtonVPN/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	The Proton VPN GTK app is intended for every Proton VPN service user, it provides full access to all functionalities available to authenticated users, with the user signup process handled on the website.
URL:		https://github.com/ProtonVPN/proton-vpn-gtk-app
License:	GPL
Group:		Networking
BuildRequires:	desktop-file-utils
BuildRequires:	lib64python-devel
BuildRequires:	python-setuptools
BuildRequires:	gtk+3.0
BuildRequires:	lib64notify4
BuildRequires:	python-gobject3
BuildRequires:	python-dbus
BuildRequires:	python-proton-vpn-api-core
BuildRequires:	librsvg
BuildRequires:	python-packaging

Requires:	gtk+3.0
Requires:	lib64gdkx11-gir3.0
Requires:	lib64notify-gir0.7
Requires:	lib64notify4
Requires:	python-gobject3
Requires:	python-dbus
Requires:	python-proton-vpn-api-core
Requires:	librsvg
Requires:	python-packaging
Requires:	python-proton-vpn-network-manager

Suggests:	lib64appindicator

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot


%description
Package: %{name}

%global debug_package %{nil}

%prep
%setup -n %{name}-%{version}

%build
python3 setup.py build

%install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications rpmbuild/SOURCES/%{desktop_entry_filename}
desktop-file-validate %{buildroot}%{_datadir}/applications/%{desktop_entry_filename}
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp rpmbuild/SOURCES/%{logo_filename} %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{logo_filename}
python3 setup.py install --single-version-externally-managed -O1 --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files
/%{py_sitedir}/proton
/%{py_sitedir}/proton_vpn_gtk_app-*.egg-info
%{_bindir}/protonvpn-app
%{_datadir}/applications/%{desktop_entry_filename}
%{_datadir}/icons/hicolor/scalable/apps/%{logo_filename}
