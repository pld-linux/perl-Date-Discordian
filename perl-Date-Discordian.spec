%include	/usr/lib/rpm/macros.perl
%define	pdir	Date
%define	pnam	Discordian
Summary:	Date::Discordian
Summary(pl):	Modu� perla Date::Discordian
Name:		perl-Date-Discordian
Version:	1.35
Release:	6
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Date-Leapyear
BuildRequires:	perl-Date-ICal >= 1.54
BuildRequires:	perl-Memoize
BuildRequires:	perl-Test-Simple
BuildRequires:	rpm-perlprov >= 4.0.2-104
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Calculate the Discordian date of a particular 'real' date.

Date::Discordian exports two functions - discordian(), and
inverse_discordian. "discordian()", when given a time value, returns a
string, giving the Discordian date for the given day.
- *inverse_discordian()*, given a Discordian date in the same format
  that "discordian()" emits, returns an epoch time value. It is pretty
  picky about time format. Pity.

%description -l pl
Modu� perla obliczaj�cy diskordia�sk� dat� dla danej "prawdziwej"
daty.

Date::Discordian udost�pnia dwie funkcje - discordian() oraz
inverse_discordian(). discordian() po podaniu warto�ci czasu zwraca
stringa zawieraj�cego dat� diskordia�sk�. inverse_discordian() po
podaniu daty w tym samym formacie, jaki produkuje discordian(), zwraca
warto�� czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Date/Discordian.pm
%{_mandir}/man3/*
