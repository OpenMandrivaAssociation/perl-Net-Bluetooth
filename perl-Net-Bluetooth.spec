%define upstream_name    Net-Bluetooth
%define upstream_version 0.40

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Net::Bluetooth - Perl Bluetooth Interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Bluetooth-%{upstream_version}.tar.bz2

BuildRequires: bluez-devel
BuildRequires: perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
Requires(pre):  bluez

%description
Net::Bluetooth - Perl Bluetooth Interface
This module creates a Bluetooth interface for Perl.

%prep
%setup -q -n Net-Bluetooth-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/*
%{perl_vendorarch}/auto/Net/*
%dir %{perl_vendorarch}/auto/Net/Bluetooth
%{perl_vendorarch}/auto/Net/Bluetooth/*
%{_mandir}/man3/*
