Name:           perl-PDF-Writer
Version:        0.06
Release:        1%{?dist}
Summary:        PDF writer abstraction layer
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/PDF-Writer/
Source0:        http://www.cpan.org/authors/id/R/RK/RKINYON/PDF-Writer-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.0
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This is a generalized API that allows a module that generates PDFs to
transparently target multiple backends without changing its code. The
currently supported backends are:

%prep
%setup -q -n PDF-Writer-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf $RPM_BUILD_ROOT

./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Aug 13 2015 Nicholas van Oudtshoorn - <vanoudt@gmail.com> 0.06-1
- Specfile autogenerated by cpanspec 1.78.
