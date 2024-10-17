%define upstream_name Net-Bluetooth
%define upstream_version 0.40

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	Net::Bluetooth - Perl Bluetooth Interface
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
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


%changelog
* Sun Feb 12 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.400.0-2
+ Revision: 773534
- clean out spec
- fix files listed twice
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.400.0-1mdv2010.0
+ Revision: 404062
- rebuild using %%perl_convert_version

* Sat Feb 28 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-6mdv2009.1
+ Revision: 345984
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.40-5mdv2009.0
+ Revision: 257951
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.40-4mdv2009.0
+ Revision: 246002
- rebuild
- fix spacing at top of description

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.40-2mdv2008.1
+ Revision: 152216
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Thu Aug 16 2007 Funda Wang <fwang@mandriva.org> 0.40-1mdv2008.0
+ Revision: 64131
- New version 0.40

* Wed May 23 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.39-1mdv2008.0
+ Revision: 30113
- Fix BR
- Import perl-Net-Bluetooth



* Wed May 23 2007 Nicolas L�cureuil <neoclust@mandriva.org> 0.39-1mdv2008.0
- First Mandriva package
