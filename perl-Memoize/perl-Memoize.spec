Name:           perl-Memoize
Version:        1.03
Release:        1%{?dist}
Summary:        Make functions faster by trading space for time
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Memoize/
Source0:        http://www.cpan.org/authors/id/M/MJ/MJD/Memoize-%{version}.tgz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Test::More)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
`Memoizing' a function makes it faster by trading space for time. It does
this by caching the return values of the function in a table. If you call
the function again with the same arguments, memoize jumps in and gives you
the value out of the table, instead of letting the function compute the
value all over again.

%prep
%setup -q -n Memoize-%{version}

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
%doc article.html Changes README TODO
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Apr 12 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 1.03-1
- Specfile autogenerated by cpanspec 1.78.
