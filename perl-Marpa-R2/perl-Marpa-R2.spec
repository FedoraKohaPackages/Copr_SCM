Name:           perl-Marpa-R2
Version:        3.000000
Release:        3.git.0.d3b1565%{?dist}
Summary:        Marpa::R2 Perl module
License:        GPL3+
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Marpa-R2/
Source0: perl-Marpa-R2-git-0.d3b1565.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(Carp) >= 1.08
BuildRequires:  perl-PathTools
BuildRequires:  perl(Data::Dumper) >= 2.125
BuildRequires:  perl(Exporter) >= 5.62
BuildRequires:  perl(ExtUtils::CBuilder) >= 0.27
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.42
BuildRequires:  perl(ExtUtils::Manifest) >= 1.51_01
BuildRequires:  perl(ExtUtils::Mkbootstrap) >= 6.42
BuildRequires:  perl(Fatal) >= 1.05
BuildRequires:  perl(HTML::Entities) >= 3.68
BuildRequires:  perl(HTML::Parser) >= 3.69
BuildRequires:  perl(IPC::Cmd) >= 0.40_1
BuildRequires:  perl(List::Util) >= 1.21
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(PPI) >= 1.206
BuildRequires:  perl(Scalar::Util) >= 1.21
BuildRequires:  perl(Test::More) >= 0.94
BuildRequires:  perl(Time::Piece) >= 1.12
BuildRequires:  perl(XSLoader) >= 0.08
BuildRequires:  perl(open)
BuildRequires:  perl(CPAN::Version)
BuildRequires:  perl(Config::AutoConf)
Requires:       perl-PathTools
Requires:       perl(Data::Dumper) >= 2.125
Requires:       perl(Exporter) >= 5.62
Requires:       perl(ExtUtils::CBuilder) >= 0.27
Requires:       perl(ExtUtils::MakeMaker) >= 6.42
Requires:       perl(ExtUtils::Manifest) >= 1.51_01
Requires:       perl(ExtUtils::Mkbootstrap) >= 6.42
Requires:       perl(Fatal) >= 1.05
Requires:       perl-PathTools
Requires:       perl(HTML::Entities) >= 3.68
Requires:       perl(HTML::Parser) >= 3.69
Requires:       perl(IPC::Cmd) >= 0.40_1
Requires:       perl(List::Util) >= 1.21
Requires:       perl(PPI) >= 1.206
Requires:       perl(Scalar::Util) >= 1.21
Requires:       perl(Test::More) >= 0.94
Requires:       perl(Time::Piece) >= 1.12
Requires:       perl(XSLoader) >= 0.08
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Marpa::R2::HTML::Config::Core)
Provides:       perl(Marpa::R2::License)
Provides:       perl(Marpa::R2::Perl::Version)
Provides:       perl(Marpa::R2::SLG)
Provides:       perl(Marpa::R2::SLR)
Provides:       perl(Marpa::R2::Version)

%description
This is the R2 version of the Marpa module. Installation is discussed in
the INSTALL document. Licensing is discussed in the LICENSE document.

%prep
%setup -q -n perl-Marpa-R2-git-0.d3b1565
cp -R cpan/* .

%build
%{__perl} Build.PL installdirs=vendor optimize="$RPM_OPT_FLAGS"
./Build

%install
rm -rf $RPM_BUILD_ROOT
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc author.t Changes COPYING.LESSER engine etc g html LICENSE meta META.json pod pperl README xs
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Marpa*
%{_mandir}/man3/*
%{_bindir}/marpa*


%changelog
* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 3.000000-3
- Add in missing Provides and BuildRequires
* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 3.000000-2
- Change File::Spec to PathTool
- Note that this provides something it does!
* Thu Jun 02 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 3.000000-1
- Specfile autogenerated by cpanspec 1.78.
