Name:           perl-Convert-BaseN
Version:        0.01
Release:        1%{?dist}
Summary:        Convert::BaseN Perl module
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Convert-BaseN/
Source0:        http://www.cpan.org/authors/id/D/DA/DANKOGAI/Convert-BaseN-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SYNOPSIS      use Convert::BaseN;
# by name
my $cb = Convert::BaseN->new('base64'); my $cb = Convert::BaseN->new( name
=> 'base64' );
# or base
my $cb = Convert::BaseN->new( base => 64 ); my $cb_url = Convert::BaseN-
>new(  base  => 64,   chars => '0-9A-Za-z\-_=' );
# encode and decode
$encoded = $cb->encode($data); $decoded = $cb->decode($encoded);

%prep
%setup -q -n Convert-BaseN-%{version}

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
* Thu Aug 13 2015 Nicholas van Oudtshoorn - <vanoudt@gmail.com> 0.01-1
- Specfile autogenerated by cpanspec 1.78.
