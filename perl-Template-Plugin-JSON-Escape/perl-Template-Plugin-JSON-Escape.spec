Name:           perl-Template-Plugin-JSON-Escape
Version:        0.02
Release:        1%{?dist}
Summary:        Adds a .json vmethod and a json filter
License:        Expat
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Template-Plugin-JSON-Escape/
Source0:        http://www.cpan.org/authors/id/N/NA/NANTO/Template-Plugin-JSON-Escape-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON) >= 2.12
BuildRequires:  perl(Template) >= 2.20
BuildRequires:  perl(Test::More)
Requires:       perl(JSON) >= 2.12
Requires:       perl(Template) >= 2.20
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This plugin allows you to embed JSON strings in HTML. In the output,
special characters such as < and & are escaped as \uxxxx to prevent
XSS attacks.

%prep
%setup -q -n Template-Plugin-JSON-Escape-%{version}

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
%doc Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Aug 13 2015 Nicholas van Oudtshoorn - <vanoudt@gmail.com> 0.02-1
- Specfile autogenerated by cpanspec 1.78.
