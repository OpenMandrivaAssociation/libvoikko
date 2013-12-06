%define major	1
%define libname	%mklibname voikko %{major}
%define devname	%mklibname voikko -d

Summary:	A spellchecker/hyphenator library using Malaga
Name:		libvoikko
Version:	3.5
Release:	5
License:	GPLv2+
Group:		Text tools
Url:		http://voikko.sourceforge.net/
Source0:	http://downloads.sourceforge.net/voikko/%{name}-%{version}.tar.gz

BuildRequires:	python
BuildRequires:	pkgconfig(glib-2.0)

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

%package -n %{devname}
Summary:	Headers and development library for libvoikko development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	voikko-devel = %{version}-%{release}

%description -n %{devname}
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
%{_libdir}/libvoikko.so.%{major}*

%files -n %{devname}
%{_libdir}/*.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files -n python-%{name}
%doc README
%{python_sitelib}/libvoikko.py

