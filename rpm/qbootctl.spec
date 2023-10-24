Name:          qbootctl
Version:       0.2.0
Release:       1
Summary:       Qualcomm bootctl HAL for Linux
URL:           https://gitlab.com/sdm845-mainline/qbootctl
Source0:       %{name}-%{version}.tar.gz
Source1:       %{name}.service
Source2:       scsi_bsg_ufs.h
License:       GPLv3 and GPLv2
BuildRequires: meson
BuildRequires: pkgconfig(systemd)
BuildRequires: pkgconfig(zlib)

%description
Trivial File Transfer Protocol server over AF_QIPCRTR.

%prep
%autosetup -n %{name}-%{version}/%{name}
mkdir -p scsi
cp %{SOURCE2} scsi/

%build
%meson
%meson_build

%install
%meson_install

mkdir -p %{buildroot}/%{_unitdir}/actdead.target.wants
mkdir -p %{buildroot}/%{_unitdir}/graphical.target.wants
install -D -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.service
ln -s ../%{name}.service %{buildroot}/%{_unitdir}/actdead.target.wants/%{name}.service
ln -s ../%{name}.service %{buildroot}/%{_unitdir}/graphical.target.wants/%{name}.service

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_unitdir}/actdead.target.wants/%{name}.service
%{_unitdir}/graphical.target.wants/%{name}.service
%{_unitdir}/%{name}.service
