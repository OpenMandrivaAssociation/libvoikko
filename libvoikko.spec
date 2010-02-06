
%define name	libvoikko
%define version	2.2.2
%define prever	0
%define rel	3

%define major	1
%define libname	%mklibname voikko %major
%define devname	%mklibname voikko -d

Summary:	A spellchecker/hyphenator library using Malaga
Name:		%name
Version:	%version
%if %prever
Release:	%mkrel 0.%prever.%rel
%else
Release:	%mkrel %rel
%endif
License:	GPLv2+
Group:		Text tools
URL:		http://voikko.sourceforge.net/
%if %prever
Source:		http://www.puimula.org/htp/testing/%name-%version%prever.tar.gz
%else
Source:		http://downloads.sourceforge.net/voikko/%name-%version.tar.gz
%endif
BuildRoot:	%{_tmppath}/%{name}-root
BuildRequires:	glib2-devel
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

%package -n %libname
Summary:	Shared library of libvoikko
Group:		System/Libraries
Provides:	%name = %version-%release

%description -n %libname
This is libvoikko, library for spellcheckers and hyphenators using
Malaga natural language grammar development tool. The library is
written in C.

This package contains the library needed to run programs dynamically
linked with libvoikko.

%package -n %devname
Summary:	Headers and static library for libvoikko development
Group:		Development/C
Requires:	%libname = %version
Provides:	libvoikko-devel = %version-%release
Provides:	voikko-devel = %version-%release
Obsoletes:	%{_lib}voikko1-devel

%description -n %devname
This is libvoikko, library for spellcheckers and hyphenators using
Malaga natural language grammar development tool. The library is
written in C.

This package contains the headers and static library that
programmers will need to develop applications which will use
libvoikko.

%package -n python-%name
Summary:	Python bindings for libvoikko
Group:		Development/Python
Requires:	%libname
Requires:	voikko-dictionary
%py_requires

%description -n python-%name
This is libvoikko, library for spellcheckers and hyphenators using
Malaga natural language grammar development tool. The library is
written in C.

This package contains the Python bindings for libvoikko.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -D -m644 python/libvoikko.py %{buildroot}%{python_sitelib}/libvoikko.py

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%files -n voikko-tools
%defattr(-,root,root)
%doc README
%{_bindir}/voikkogc
%{_bindir}/voikkospell
%{_bindir}/voikkohyphenate
%{_mandir}/man1/voikkogc.1*
%{_mandir}/man1/voikkospell.1*
%{_mandir}/man1/voikkohyphenate.1*

%files -n %libname
%doc README
%{_libdir}/*.so.%{major}*

%files -n %devname
%doc README
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%name
%doc README
%{python_sitelib}/libvoikko.py

