%include	/usr/lib/rpm/macros.perl
Summary:	proFXP - a command line FXP client
Name:		profxp
Version:	3.0
Release:	0.1
License:	distributable
Group:		Applications/Networking
Source0:	http://duncanthrax.net/profxp/%{name}-v3-pre2-src.tar.gz
# Source0-md5:	66bc8de435ee02378eecdf129d7695dd
Patch0:		%{name}-perl.patch
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
proFXP is a FXP (server-to-server FTP) client written in Perl. It
features TAB completion, site management, idle timers, SOCKS support,
active and passive mode, different listing modes and a very powerful
"down-to-the protocol metal" 2-char-command command line interface,
pleasing newbies and hardcore hackers alike.


%prep
%setup -q -n profxp
%patch0 -p1

%{__perl} Makefile.PL \
        INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} \
	install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/profxp/*.pm
%attr(755,root,root) %{_bindir}/profxpv3.pl
