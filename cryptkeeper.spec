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
BuildRequires:  gtk+2-devel
Requires:       encfs
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Cryptkeeper is a Linux system tray applet that manages EncFS encrypted folders. 
%prep
%setup -q

%build
%configure2_5x
%__make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/cryptkeeper
%{_datadir}/applications/cryptkeeper.desktop
%{_datadir}/pixmaps/cryptkeeper.png

