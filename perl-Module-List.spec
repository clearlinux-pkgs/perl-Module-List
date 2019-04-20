#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Module-List
Version  : 0.004
Release  : 13
URL      : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Module-List-0.004.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/Z/ZE/ZEFRAM/Module-List-0.004.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-find-perl/libmodule-find-perl_0.13-1.debian.tar.xz
Summary  : "module `directory' listing"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-List-license = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
Module::List - module `directory' listing
DESCRIPTION
This module deals with the examination of the namespace of Perl modules.
The contents of the module namespace is split across several physical
directory trees, but this module hides that detail, providing instead
a view of the abstract namespace.

%package dev
Summary: dev components for the perl-Module-List package.
Group: Development
Provides: perl-Module-List-devel = %{version}-%{release}
Requires: perl-Module-List = %{version}-%{release}

%description dev
dev components for the perl-Module-List package.


%package license
Summary: license components for the perl-Module-List package.
Group: Default

%description license
license components for the perl-Module-List package.


%prep
%setup -q -n Module-List-0.004
cd ..
%setup -q -T -D -n Module-List-0.004 -b 1
mkdir -p deblicense/
cp -r %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Module-List-0.004/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-List
cp deblicense/copyright %{buildroot}/usr/share/package-licenses/perl-Module-List/deblicense_copyright
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/Module/List.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::List.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-List/deblicense_copyright
