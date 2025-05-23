#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v22
# autospec commit: 247c192
#
Name     : perl-Module-List
Version  : 0.005
Release  : 31
URL      : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-List-0.005.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-List-0.005.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libm/libmodule-find-perl/libmodule-find-perl_0.13-1.debian.tar.xz
Summary  : "module `directory' listing"
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Module-List-license = %{version}-%{release}
Requires: perl-Module-List-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This Perl module will find all modules available locally that match
a namespace. It can provide some information about the identified
modules, depending on what parameters you pass.

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


%package perl
Summary: perl components for the perl-Module-List package.
Group: Default
Requires: perl-Module-List = %{version}-%{release}

%description perl
perl components for the perl-Module-List package.


%prep
%setup -q -n Module-List-0.005
cd %{_builddir}
tar xf %{_sourcedir}/libmodule-find-perl_0.13-1.debian.tar.xz
cd %{_builddir}/Module-List-0.005
mkdir -p deblicense/
cp -r %{_builddir}/debian/. %{_builddir}/Module-List-0.005/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Module-List
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-Module-List/4ee2088ae1960a0c01daaec40141bafcb4a3408a || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Module::List.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Module-List/4ee2088ae1960a0c01daaec40141bafcb4a3408a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
