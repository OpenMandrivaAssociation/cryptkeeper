%define name    cryptkeeper
%define version 0.9.5
%define release %mkrel 1

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    System tray applet that manages EncFS encrypted folders
License:    GPLv3
Group:      System/Kernel and hardware
URL:        http://tom.noflag.org.uk/cryptkeeper.html
Source0:    http://tom.noflag.org.uk/cryptkeeper/%name-%version.tar.gz
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gconf-2.0)
Requires:       encfs
Patch0:		cryptkeeper-0.9.5-add-unistd-header.patch
Patch1:		cryptkeeper-0.9.5-fix-linking.patch

%description
Cryptkeeper is a Linux system tray applet that manages EncFS encrypted folders. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/cryptkeeper
%{_datadir}/applications/cryptkeeper.desktop
%{_datadir}/pixmaps/cryptkeeper.png
