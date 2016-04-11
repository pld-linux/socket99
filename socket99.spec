Summary:	C99 wrapper library for the BSD sockets API
Summary(pl.UTF-8):	Biblioteka C99 obudowująca API gniazd BSD
Name:		socket99
Version:	0.2.0
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/silentbicycle/socket99/releases
Source0:	https://github.com/silentbicycle/socket99/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	8fd589f5f8e29a5178a79a019f660886
URL:		https://github.com/silentbicycle/socket99
BuildRequires:	gcc >= 5:3.0
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library trades the series of `getaddrinfo`, `socket`, `connect`,
`bind`, `listen`, etc. functions and their convoluted, casted
arguments for just one function that takes two structs (configuration
and output). By creatively using C99's "designated initializers", the
configuration struct works rather like a configuration key/value hash;
the output struct contains either the socket file descriptor or error
information.

%description -l pl.UTF-8
Ta biblioteka wymiania serię funkcji "getaddrinfo", "socket",
"connect", "bind", "listen" itp. oraz ich zawiłe, rzutowane argumenty
na pojedynczą funkcję przyjmującą dwie struktury (konfigurację oraz
wyjście). Poprzez kreatywne wykorzystanie "wyznaczonych
inicjalizatorów" dialektu C99 struktury konfiguracyjne działają
bardziej jak konfiguracyjna tablica asocjacyjna klucz-wartość;
struktura wyjściowa zawiera deskryptor pliku gniazda lub informację o
błędzie.

%package devel
Summary:	Header files for socket99 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki socket99
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for socket99 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki socket99.

%package static
Summary:	Static socket99 library
Summary(pl.UTF-8):	Statyczna biblioteka socket99
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static socket99 library.

%description static -l pl.UTF-8
Statyczna biblioteka socket99.

%prep
%setup -q

%build
libtool --mode=compile %{__cc} %{rpmcflags} %{rpmcppflags} -Wall -Wextra -std=c99 -D_GNU_SOURCE -c socket99.c
libtool --mode=link %{__cc} %{rpmldflags} %{rpmcflags} -o libsocket99.la socket99.lo -rpath %{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir}/socket99}

libtool --mode=install install libsocket99.la $RPM_BUILD_ROOT%{_libdir}
cp -p socket99.h $RPM_BUILD_ROOT%{_includedir}/socket99

# no external dependencies
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsocket99.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_libdir}/libsocket99.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsocket99.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsocket99.so
%{_includedir}/socket99

%files static
%defattr(644,root,root,755)
%{_libdir}/libsocket99.a
