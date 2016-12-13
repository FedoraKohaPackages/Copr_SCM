Name:           perl-MARC-Parser-RAW
Version:        0.03
Release:        1%{?dist}
Summary:        Parser for ISO 2709 encoded MARC records
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/MARC-Parser-RAW/
Source0:        http://www.cpan.org/authors/id/J/JO/JOROL/MARC-Parser-RAW-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(Module::Build::Tiny)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Readonly) >= 1.0
BuildRequires:  perl(Test::More) >= 0.96
Requires:       perl(Readonly) >= 1.0
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
MARC::Parser::RAW is a lightweight, fault tolerant parser for ISO 2709
encoded MARC records. Tags, indicators and subfield codes are not validated
against the MARC standard. Record length from leader and field lengths from
the directory are ignored. Records with a faulty structure will be skipped
with a warning. The resulting data structure is optimized for usage with
the Catmandu data tool kit.

%prep
%setup -q -n MARC-Parser-RAW-%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build

%install
rm -rf $RPM_BUILD_ROOT
./Build install --destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
rm $RPM_BUILD_ROOT/usr/lib64/perl5/vendor_perl/auto/MARC/Parser/RAW/.packlist

#%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes cpanfile dist.ini LICENSE META.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Thu Jun 30 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.