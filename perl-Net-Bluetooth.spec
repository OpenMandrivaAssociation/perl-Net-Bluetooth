%define upstream_name Net-Bluetooth
%define upstream_version 0.40

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Net::Bluetooth - Perl Bluetooth Interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Bluetooth-%{upstream_version}.tar.bz2

BuildRequires:	bluez-devel
BuildRequires:	perl-devel
Requires(pre):	bluez

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
%makeinstall_std

%files
%doc Changes README
%{perl_vendorarch}/Net/Bluetooth.pm
%dir %{perl_vendorarch}/auto/Net/Bluetooth
%{perl_vendorarch}/auto/Net/Bluetooth/*
%{_mandir}/man3/*
