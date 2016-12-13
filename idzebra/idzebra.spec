Name: idzebra
Version: 2.0.62
Release: 1%{?dist}
Summary: High performance structured text indexing and retrieval engine

Group: Applications/Databases	
License: GPLv2+
URL: http://www.indexdata.dk/zebra/	
Source0: http://ftp.indexdata.dk/pub/zebra/%{name}-%{version}.tar.gz
BuildRequires: libyaz-devel
BuildRequires: expat-devel
BuildRequires: bzip2-devel
BuildRequires: tcl
BuildRequires: zlib-devel
BuildRequires: libxslt-devel
BuildRequires: libicu-devel
BuildRequires: tcp_wrappers-devel
Requires: lib%{name}%{?_isa} = %{version}-%{release}

%description
Zebra is a high-performance, general-purpose structured text indexing
and retrieval engine. It reads structured records in a variety of input
formats (such as email, XML, and MARC) and allows access to them through
exact Boolean search expressions and relevance-ranked free-text queries.

%package -n lib%{name}
Summary: Zebra libraries
Group: Development/Libraries
%description -n lib%{name}
Libraries for the Zebra search engine.

%post -n lib%{name} -p /sbin/ldconfig
%postun -n lib%{name} -p /sbin/ldconfig

%package -n lib%{name}-modules
Summary: Zebra modules
Group: Development/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-modules
Modules for the Zebra search engine

%package -n lib%{name}-devel
Summary: Zebra development libraries
Group: Development/Libraries
Requires: lib%{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-devel
Development libraries for the Zebra search engine.

 
%prep
%setup -q -n %{name}-%{version}


%build
%configure --disable-static 
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?_smp_mflags}

%install
make install DESTDIR=${RPM_BUILD_ROOT}
rm ${RPM_BUILD_ROOT}/%{_libdir}/*.la
rm ${RPM_BUILD_ROOT}/%{_libdir}/%{name}-2.0/modules/*.la


%files
%{_datadir}/%{name}-2.0/tab
%{_bindir}/zebrasrv*
%{_bindir}/zebraidx*
%{_bindir}/idzebra-abs2dom
%{_defaultdocdir}/%{name}-2.0
%{_mandir}/*/%{name}*
%{_mandir}/*/zebra*
%{_datadir}/%{name}-2.0-examples

%files -n lib%{name}
%{_libdir}/*.so.*

%files -n lib%{name}-modules
%{_libdir}/%{name}-2.0/modules/*.so

%files -n lib%{name}-devel
%{_bindir}/idzebra-config-*
%{_includedir}/%{name}-2.0/*
%{_libdir}/*.so
%{_mandir}/*/idzebra-config-*
%{_datadir}/aclocal/*.m4

%changelog
* Thu Jul 21 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 2.0.62-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.58-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Oct 28 2015 David Tardon <dtardon@redhat.com> - 2.0.58-7
- rebuild for ICU 56.1

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.58-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 26 2015 David Tardon <dtardon@redhat.com> - 2.0.58-5
- rebuild for ICU 54.1

* Tue Aug 26 2014 David Tardon <dtardon@redhat.com> - 2.0.58-4
- rebuild for ICU 53.1

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.58-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.58-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Apr 3 2014 Nicholas van Oudtshoorn <vanoudt@gmail.com> - 2.0.58-1
- Update to latest upstream release
- Rebuild for new yaz

* Fri Feb 14 2014 David Tardon <dtardon@redhat.com> - 2.0.52-6
- rebuild for new ICU

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.52-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Petr Pisar <ppisar@redhat.com> - 2.0.52-4
- Perl 5.18 rebuild

* Fri Feb 01 2013 Parag Nemade <paragn AT fedoraproject DOT org> - 2.0.52-3
- Rebuild for icu 50

* Wed Oct 31 2012 Nicholas van Oudtshoorn <vanoudt at gmail.com> 2.0.52-2
- Minor spec file fixes
* Mon Oct 29 2012 Nicholas van Oudtshoorn <vanoudt at gmail.com> 2.0.52-1
- New version
- Spec file fixes
* Wed Apr 27 2011 Nicholas van Oudtshoorn <vanoudt at gmail.com> 2.0.46-1
- Initial spec file for Fedora
