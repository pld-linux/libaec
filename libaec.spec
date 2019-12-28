#
# Conditional build:
%bcond_without	static_libs	# static libraries
#
Summary:	Adaptive Entropy Coding library
Summary(pl.UTF-8):	Biblioteka Adaptive Entropy Coding
Name:		libaec
Version:	0.3.2
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://www.dkrz.de/redmine/projects/aec/wiki/Downloads
Source0:	https://www.dkrz.de/redmine/attachments/download/453/%{name}-%{version}.tar.gz
# Source0-md5:	19c1211935d82d8b0bf581329634a6d7
URL:		https://www.dkrz.de/redmine/projects/aec/wiki
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libaec provides fast lossless compression of 1 up to 32 bit wide
signed or unsigned integers (samples). The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations. While floating point representations are not directly
supported, they can also be efficiently coded by grouping exponents
and mantissa.

Libaec also includes a free drop-in replacement for the SZIP library.

%description -l pl.UTF-8
Libaec zapewnia szybką, bezstratną kompresję liczb całkowitych
(próbek) z lub bez znaku o rozmiarze od 1 do 32 bitów. Biblioteka
osiąga najlepsze wyniki dla danych o małej entropii, zwykle
spotykanych w danych z przyrządów pomiarowych albo modeli numerycznych
symulacji pogody lub klimatu. Mimo że reprezentacje zmiennoprzecinkowe
nie są bezpośrednio obsługiwane, mogą być wydajnie kodowane poprzez
grupowanie wykładników i mantys.

Libaec zawiera także wolnodostępny zamiennik biblioteki SZIP.

%package devel
Summary:	Header files for libaec library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libaec
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libaec library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libaec.

%package static
Summary:	Static libaec library
Summary(pl.UTF-8):	Statyczna biblioteka libaec
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libaec library.

%description static -l pl.UTF-8
Statyczna biblioteka libaec.

%package szip
Summary:	Free SZIP library replacement based on libaec
Summary(pl.UTF-8):	Wolnodostępny zamiennik biblioteki SZIP oparty na libaec
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	szip = 2.0.0
Obsoletes:	szip < 2.2

%description szip
Free SZIP compression library replacement based on libaec.

%description szip -l pl.UTF-8
Wolnodostępny zamiennik biblioteki kompresji SZIP oparty na libaec.

%package szip-devel
Summary:	Free SZIP library replacement based on libaec - header file
Summary(pl.UTF-8):	Wolnodostępny zamiennik biblioteki SZIP oparty na libaec - plik nagłówkowy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-szip = %{version}-%{release}
Provides:	szip-devel = 2.0.0
Obsoletes:	szip-devel < 2.2

%description szip-devel
Free SZIP compression library replacement based on libaec - header
file.

%description szip-devel -l pl.UTF-8
Wolnodostępny zamiennik biblioteki kompresji SZIP oparty na libaec -
plik nagłówkowy.

%package szip-static
Summary:	Free SZIP library replacement based on libaec - static library
Summary(pl.UTF-8):	Wolnodostępny zamiennik biblioteki SZIP oparty na libaec - biblioteka statyczna
Group:		Development/Libraries
Requires:	%{name}-szip-devel = %{version}-%{release}
Provides:	szip-static = 2.0.0
Obsoletes:	szip-static < 2.2

%description szip-static
Free SZIP compression library replacement based on libaec - static
library.

%description szip-static -l pl.UTF-8
Wolnodostępny zamiennik biblioteki kompresji SZIP oparty na libaec -
biblioteka statyczna.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	szip -p /sbin/ldconfig
%postun	szip -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog README README.SZIP doc/license.txt
%attr(755,root,root) %{_bindir}/aec
%attr(755,root,root) %{_libdir}/libaec.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libaec.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libaec.so
%{_libdir}/libaec.la
%{_includedir}/libaec.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libaec.a
%endif

%files szip
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsz.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsz.so.2

%files szip-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsz.so
%{_libdir}/libsz.la
%{_includedir}/szlib.h

%if %{with static_libs}
%files szip-static
%defattr(644,root,root,755)
%{_libdir}/libsz.a
%endif
