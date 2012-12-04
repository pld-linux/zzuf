Summary:	Multi-purpose fuzzer
Summary(pl.UTF-8):	Narzędzie zniekształcające o wielu zastosowaniach
Name:		zzuf
Version:	0.13
Release:	1
License:	WTFPL v2
Group:		Development/Tools
Source0:	http://caca.zoy.org/files/zzuf/%{name}-%{version}.tar.gz
# Source0-md5:	74579c429f9691f641a14f408997d42d
URL:		http://caca.zoy.org/wiki/zzuf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

# rename due to conflict with zziplib
%{__sed} -i -e 's/zzcat/zzufcat/' doc/zzcat.1.in doc/zzuf.1.in

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

# rename due to conflict with zziplib
%{__mv} $RPM_BUILD_ROOT%{_bindir}/{zzcat,zzufcat}
%{__mv} $RPM_BUILD_ROOT%{_mandir}/man1/{zzcat,zzufcat}.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/zzuf
%attr(755,root,root) %{_bindir}/zzufcat
%dir %{_libdir}/zzuf
%attr(755,root,root) %{_libdir}/zzuf/libzzuf.so
%{_mandir}/man1/zzuf.1*
%{_mandir}/man1/zzufcat.1*
%{_mandir}/man3/libzzuf.3*
