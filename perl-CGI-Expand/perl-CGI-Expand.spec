Name:           perl-CGI-Expand
Version:        2.7
Release:        1.git.0.8f96848%{?dist}
Summary:        Convert flat hash to nested data using TT2's dot convention
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/CGI-Expand/
Source0: perl-CGI-Expand-git-0.8f96848.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::Exception)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Converts a CGI query into structured data using a dotted name convention
similar to TT2.

%prep
%setup -q -n perl-CGI-Expand-git-0.8f96848

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
* Thu Jun 02 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 2.7-1
- New update for COPR 

* Thu Jun 02 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 2.6-1
- new package built with tito

* Thu Jun 02 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 2.05-1
- Specfile autogenerated by cpanspec 1.78.
