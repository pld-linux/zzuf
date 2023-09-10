Summary:	Multi-purpose fuzzer
Summary(pl.UTF-8):	Narzędzie zniekształcające o wielu zastosowaniach
Name:		zzuf
Version:	0.15
Release:	1
License:	WTFPL v2
Group:		Development/Tools
#Source0Download: https://github.com/samhocevar/zzuf/releases
Source0:	https://github.com/samhocevar/zzuf/releases/download/v%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	a6cd6caabd8e803857783f83bc4e29bd
URL:		http://caca.zoy.org/wiki/zzuf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# Filter GLIBC_PRIVATE Requires
%define		_noautoreq	(GLIBC_PRIVATE)

%description
zzuf is a transparent application input fuzzer. It works by
intercepting file operations and changing random bits in the program's
input. zzuf's behaviour is deterministic, making it easy to reproduce
bugs.

%description -l pl.UTF-8
zzuf to działające w sposób przezroczysty narzędzie zniekształcające
wejście aplikacji. Działa poprzez przechwytywanie operacji na plikach
i zmianę losowych bitów w wejściu programu. Zachowanie zzufa jest
deterministyczne, dzięki czemu reprodukcja błędów jest łatwa.

%prep
%setup -q

%build
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# preloadable library
%{__rm} $RPM_BUILD_ROOT%{_libdir}/zzuf/libzzuf.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING TODO
%attr(755,root,root) %{_bindir}/zzat
%attr(755,root,root) %{_bindir}/zzuf
%dir %{_libdir}/zzuf
%attr(755,root,root) %{_libdir}/zzuf/libzzuf.so
%{_mandir}/man1/zzat.1*
%{_mandir}/man1/zzuf.1*
%{_mandir}/man3/libzzuf.3*
