%define api_version		1.0

Summary:	OpenGL Extension to GTK
Name:		gtkglext
Version:	1.2.0
Release:	11%{?dist}

License:	LGPLv2+ or GPLv2+
Group:		System Environment/Libraries
URL:		http://gtkglext.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/gtkglext/gtkglext/%{version}/gtkglext-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gtk2-devel
BuildRequires:	libGLU-devel
BuildRequires:	libGL-devel
# Conditional build feature
BuildRequires:	libXmu-devel
# The configure script checks for X11/Intrinsic.h
BuildRequires:	libXt-devel

Requires(postun):	/sbin/ldconfig
Requires(post):		/sbin/ldconfig

%description
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package libs
Summary:	OpenGL Extension to GTK
Group:		System Environment/Libraries
License:	LGPLv2+

Obsoletes:	gtkglext < %{version}-%{release}
Provides:	gtkglext = %{version}-%{release}

%description libs
GtkGLExt is an OpenGL extension to GTK. It provides the GDK objects
which support OpenGL rendering in GTK, and GtkWidget API add-ons to
make GTK+ widgets OpenGL-capable.

%package devel
Summary:	Development tools for GTK-based OpenGL applications
Group:		Development/Libraries
License:	LGPLv2+

Requires:	%{name} = %{version}
Requires:	gtk2-devel
Requires:	libGL-devel
Requires:	libGLU-devel
Requires:	libXmu-devel
Requires:	pkgconfig

%description devel
The gtkglext-devel package contains the header files, static libraries,
and developer docs for GtkGLExt.

%prep
%setup -q -n gtkglext-%{version}

%build
%configure --disable-gtk-doc --disable-static
make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
%if 0%{?fedora} >= 8 || 0%{?rhel} >= 6
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post libs
/sbin/ldconfig

%postun libs
/sbin/ldconfig

%files libs
%defattr(-,root,root,-)

%doc AUTHORS COPYING COPYING.LIB ChangeLog README TODO
%{_libdir}/libgdkglext-x11-%{api_version}.so.*
%{_libdir}/libgtkglext-x11-%{api_version}.so.*

%files devel
%defattr(-,root,root,-)

%{_includedir}/*
%{_libdir}/gtkglext-%{api_version}
%{_libdir}/lib*.so
%if 0%{?fedora} < 8 && 0%{?rhel} < 6
%{_libdir}/lib*.a
%endif
%{_libdir}/pkgconfig/*
%{_datadir}/aclocal/*
%doc %{_datadir}/gtk-doc/html/*

%changelog
* Fri Jan 29 2010 Ray Strode <rstrode@redhat.com> 1.2.0-11
Resolves: #560006
- Spec file clean up

* Fri Nov 13 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.2.0-10.1
- Update conditionals for RHEL

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Dec 08 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.2.0-8
- Rebuild for pkgconfig provides

* Tue Jun 03 2008 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-7
- Use 0%%{?fedora} conditionals instead of "%%{fedora}" (BZ 449635).

* Sun Feb 10 2008 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-6
- Rebuild for gcc43.

* Wed Aug 22 2007 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-5
- Don't install *.la's for fedora >= 8.
- Update license tags.
- Split out *-libs.

* Tue Sep 05 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-4
- Mass rebuild.

* Mon Aug 14 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-3
- BR: libXmu-devel (Braden McDaniel).
- *-devel: R: libXmu-devel. 
- *-devel: R: pkgconfig.

* Tue Feb 14 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-2
- Require: libGLU-devel (PR 181018)

* Mon Feb 06 2006 Ralf Corsépius <rc040203@freenet.de> - 1.2.0-1
- Upstream update.
- Spec file cleanup.
- Disable static libs.

* Thu Jan 05 2006 Ralf Corsepius <ralf@links2linux.de> - 1.0.6-3
- Add %%dist.
- Adaptations to modular X .
- Remove gcc-c++ (Already in default deps).

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Fri Jun 07 2004 Ralf Corsepius <ralf@links2linux.de> - 1.0.6-0.fdr.1
- Spec cleanups.

* Fri Jun 04 2004 Ralf Corsepius <ralf@links2linux.de> - 1.0.6-0.fdr.0
- Initial fedora rpm spec, loosely derived from the version shipped
  with gtkglext.
