%include	/usr/lib/rpm/macros.perl
Summary:	Date-Discordian
Summary(pl):	Modu³ perla Date-Discordian
Name:		perl-Date-Discordian
Version:	1.35
Release:	0
License:	?
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Date/Date-Discordian-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calculate the Discordian date of a particular 'real' date.

Date::Discordian exports two functions - discordian(), and
inverse_discordian. "discordian()", when given a time value,
returns a string, giving the Discordian date for the given day.
*inverse_discordian()*, given a Discordian date in the same format that
"discordian()" emits, returns an epoch time value. It is pretty picky
about time format. Pity.

%prep
%setup -q -n Date-Discordian-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.gz
%{perl_sitelib}/Date/Discordian.pm
%{_mandir}/man3/*
