Name:           perl-UUID-Random
Version:        0.04
Release:        1%{?dist}
Summary:        Generate random uuid strings
License:        CHECK(GPL+ or Artistic)
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/UUID-Random/
Source0:        http://www.cpan.org/authors/id/P/PE/PERLER/UUID-Random-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This module generates random uuid strings. It does not satisfy any of the
points listed in RFC 4122 (http://tools.ietf.org/html/rfc4122) but the
default format.

%prep
%setup -q -n UUID-Random-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Sep 29 2015 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.04-1
- Specfile autogenerated by cpanspec 1.78.
