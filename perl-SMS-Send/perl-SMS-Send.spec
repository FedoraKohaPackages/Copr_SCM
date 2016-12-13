Name:           perl-SMS-Send
Version:        1.06
Release:        1%{?dist}
Summary:        Driver-based API for sending SMS messages
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/SMS-Send/
Source0:        http://www.cpan.org/authors/id/A/AD/ADAMK/SMS-Send-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl >= 1:5.6.0
BuildRequires:  perl(Class::Adapter) >= 1.05
BuildRequires:  perl(Class::Adapter::Builder) >= 1.05
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec) >= 0.80
BuildRequires:  perl(Module::Pluggable) >= 3.7
BuildRequires:  perl(Params::Util) >= 1.00
BuildRequires:  perl(Test::More) >= 0.47
Requires:       perl(Class::Adapter) >= 1.05
Requires:       perl(Class::Adapter::Builder) >= 1.05
Requires:       perl(Module::Pluggable) >= 3.7
Requires:       perl(Params::Util) >= 1.00
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
SMS::Send is intended to provide a driver-based single API for sending SMS
and MMS messages. The intent is to provide a single API against which to
write the code to send an SMS message.

%prep
%setup -q -n SMS-Send-%{version}

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
%doc Changes LICENSE MYMETA.json README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Thu Aug 13 2015 Nicholas van Oudtshoorn - <vanoudt@gmail.com> 1.06-1
- Specfile autogenerated by cpanspec 1.78.
