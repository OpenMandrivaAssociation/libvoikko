%define major	1
%define libname	%mklibname voikko %{major}
%define develname	%mklibname voikko -d

Summary:	A spellchecker/hyphenator library using Malaga
Name:		libvoikko
Version:	3.5
Release:	1
License:	GPLv2+
Group:		Text tools
URL:		http://voikko.sourceforge.net/
Source0:	http://downloads.sourceforge.net/voikko/%{name}-%{version}.tar.gz

BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	python

%description
This is libvoikko, library for spellcheckers and hyphenators using
Malaga natural language grammar development tool. The library is
written in C.

Currently only Finnish is supported, but adding support for other
languages should not be too hard.

%package -n voikko-tools
Summary:	Test programs for libvoikko
Group:		Text tools
Requires:	voikko-dictionary

%description -n voikko-tools
This is libvoikko, library for spellcheckers and hyphenators using
Malaga natural language grammar development tool.

This package contains the voikkospell and voikkohyphenate programs.

%package -n %{libname}
Summary:	Shared library of libvoikko
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with libvoikko.

%package -n %{develname}
Summary:	Headers and development library for libvoikko development
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	voikko-devel = %{version}-%{release}
Obsoletes:	%{_lib}voikko1-devel

%description -n %{develname}
This package contains the headers and development library that
programmers will need to develop applications which will use
libvoikko.

%package -n python-%{name}
Summary:	Python bindings for libvoikko
Group:		Development/Python
Requires:	%{libname}
Requires:	voikko-dictionary

%description -n python-%{name}
This is libvoikko, library for spellcheckers and hyphenators using
Malaga natural language grammar development tool. The library is
written in C.

This package contains the Python bindings for libvoikko.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m644 python/libvoikko.py %{buildroot}%{python_sitelib}/libvoikko.py

%files -n voikko-tools
%doc README
%{_bindir}/voikkogc
%{_bindir}/voikkospell
%{_bindir}/voikkohyphenate
%{_bindir}/voikkovfstc
%{_mandir}/man1/voikkogc.1*
%{_mandir}/man1/voikkospell.1*
%{_mandir}/man1/voikkohyphenate.1*
%{_mandir}/man1/voikkovfstc.1*

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%{name}
%doc README
%{python_sitelib}/libvoikko.py



%changelog
* Thu Dec 08 2011 Matthew Dawkins <mattydaw@mandriva.org> 3.3.1-1
+ Revision: 738835
- new version 3.3.1
- cleaned up spec
- disabled static build
- removed .la files
- removed mkrel, clean section, BuildRoot, defattr
- removed pre 200900 scriptlets

* Fri Apr 22 2011 Anssi Hannula <anssi@mandriva.org> 3.2-1
+ Revision: 656760
- new version

* Tue Jan 18 2011 Funda Wang <fwang@mandriva.org> 3.1-1
+ Revision: 631482
- new version 3.1

* Mon Nov 01 2010 Anssi Hannula <anssi@mandriva.org> 3.0-2mdv2011.0
+ Revision: 591574
- rebuild for new python
- drop the now unneeded use of py_requires macro

* Sat Jul 10 2010 Anssi Hannula <anssi@mandriva.org> 3.0-1mdv2011.0
+ Revision: 549975
- new version

* Wed Apr 28 2010 Anssi Hannula <anssi@mandriva.org> 2.3.1-1mdv2010.1
+ Revision: 540547
- new version

* Sat Feb 06 2010 Anssi Hannula <anssi@mandriva.org> 2.2.2-3mdv2010.1
+ Revision: 501392
- package python bindings in subpackage python-libvoikko

* Mon Jan 18 2010 Funda Wang <fwang@mandriva.org> 2.2.2-2mdv2010.1
+ Revision: 492933
- BR python

* Sun Dec 20 2009 Funda Wang <fwang@mandriva.org> 2.2.2-1mdv2010.1
+ Revision: 480387
- new version 2.2.2

* Fri Oct 09 2009 Anssi Hannula <anssi@mandriva.org> 2.2.1-1mdv2010.0
+ Revision: 456310
- new bugfix release

* Thu Oct 01 2009 Anssi Hannula <anssi@mandriva.org> 2.2-1mdv2010.0
+ Revision: 452159
- new version (no changes since 2.2rc2)

* Sat Sep 19 2009 Anssi Hannula <anssi@mandriva.org> 2.2-0.rc2.1mdv2010.0
+ Revision: 444708
- new testing release 2.2rc2
- libmalaga is no longer used, dependency is replaced with glib2

* Mon May 25 2009 Funda Wang <fwang@mandriva.org> 2.1-1mdv2010.0
+ Revision: 379488
- New version 2.1

* Sun Sep 07 2008 Anssi Hannula <anssi@mandriva.org> 2.0-1mdv2009.0
+ Revision: 282088
- new version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Thu May 29 2008 Anssi Hannula <anssi@mandriva.org> 1.7-1mdv2009.0
+ Revision: 212851
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Dec 26 2007 Anssi Hannula <anssi@mandriva.org> 1.6-1mdv2008.1
+ Revision: 137921
- 1.6

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Anssi Hannula <anssi@mandriva.org> 1.5-1mdv2008.0
+ Revision: 77040
- 1.5
- more specific license tag
- migrate to the new devel policy

* Tue May 15 2007 Anssi Hannula <anssi@mandriva.org> 1.4.1-1mdv2008.0
+ Revision: 27049
- 1.4.1

* Mon Apr 30 2007 Anssi Hannula <anssi@mandriva.org> 1.4-1mdv2008.0
+ Revision: 19487
- 1.4


* Mon Feb 12 2007 Anssi Hannula <anssi@mandriva.org> 1.3.1-1mdv2007.0
+ Revision: 119046
- 1.3.1

* Mon Feb 05 2007 Anssi Hannula <anssi@mandriva.org> 1.3-1mdv2007.1
+ Revision: 116226
- 1.3
- update URL

* Sat Nov 11 2006 Anssi Hannula <anssi@mandriva.org> 1.2-1mdv2007.1
+ Revision: 83087
- 1.2

* Sun Oct 29 2006 Anssi Hannula <anssi@mandriva.org> 1.1-1mdv2007.1
+ Revision: 73611
- 1.1
- drop patch0, fixed upstream
- Import libvoikko

* Sun Sep 10 2006 Anssi Hannula <anssi@mandriva.org> 1.0-4mdv2007.0
- patch0: lower the char count limit and apply it to ucs4 functions too

* Tue Aug 22 2006 Anssi Hannula <anssi@mandriva.org> 1.0-3mdv2007.0
- fix provides of -devel package
- require dictionary by tools, not by library
- use upstream dictionary path

* Wed Aug 16 2006 Anssi Hannula <anssi@mandriva.org> 1.0-2mdv2007.0
- update dictionary path

* Mon Aug 14 2006 Anssi Hannula <anssi@mandriva.org> 1.0-1mdv2007.0
- initial Mandriva release

