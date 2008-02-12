%define realname   Net-Bluetooth

Name:		perl-%{realname}
Version:        0.40
Release:        %mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
Summary:        Net::Bluetooth - Perl Bluetooth Interface
Source0:        ftp://ftp.perl.org/pub/CPAN/modules/by-module/Net/Net-Bluetooth-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: bluez-devel
BuildRequires: perl-devel
Requires(pre):  bluez

%description
Net::Bluetooth - Perl Bluetooth Interface
This module creates a Bluetooth interface for Perl.

%prep
%setup -q -n Net-Bluetooth-%{version} 

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
