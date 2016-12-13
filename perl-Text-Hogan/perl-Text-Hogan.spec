Name:           perl-Text-Hogan
Version:        1.03
Release:        1.git.0.499f81f%{?dist}
Summary:        Mustache templating engine statement-for-statement cloned from hogan.js
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Text-Hogan/
Source0: perl-Text-Hogan-git-0.499f81f.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 0:5.006
BuildRequires:  perl(Clone) >= 0.37
BuildRequires:  perl(Data::Visitor::Callback) >= 0.30
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Path::Tiny) >= 0.059
BuildRequires:  perl(Scalar::Util) >= 1.41
BuildRequires:  perl(Test::More) >= 1.001008
BuildRequires:  perl(Text::Trim) >= 1.02
BuildRequires:  perl(Try::Tiny) >= 0.22
BuildRequires:  perl(YAML) >= 1.13
Requires:       perl(Clone) >= 0.37
Requires:       perl(Scalar::Util) >= 1.41
Requires:       perl(Text::Trim) >= 1.02
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Text::Hogan is a statement-for-statement rewrite of hogan.js in Perl.

%prep
%setup -q -n perl-Text-Hogan-git-0.499f81f

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
%doc Changes dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 1.03-1
- Specfile autogenerated by cpanspec 1.78.
