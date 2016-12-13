Name:           perl-Template-Plugin-HtmlToText
Version:        0.03
Release:        1%{?dist}
Summary:        Plugin interface to HTML::FormatText
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Template-Plugin-HtmlToText/
Source0:        http://www.cpan.org/authors/id/F/FA/FAYLAND/Template-Plugin-HtmlToText-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
BuildRequires:  perl(HTML::FormatText)
BuildRequires:  perl(HTML::TreeBuilder)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
This plugin provides an interface to the HTML::FormatText module which
format HTML as plaintext.

%prep
%setup -q -n Template-Plugin-HtmlToText-%{version}

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
* Thu Aug 13 2015 Nicholas van Oudtshoorn - <vanoudt@gmail.com> 0.03-1
- Specfile autogenerated by cpanspec 1.78.
