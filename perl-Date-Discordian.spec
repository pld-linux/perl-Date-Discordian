#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"

%define		pdir	Date
%define		pnam	Discordian
Summary:	Date::Discordian - calculate the Discordian date of a particular day
Summary(pl.UTF-8):	Date::Discordian - obliczanie daty diskordiańskiej dla określonego dnia
Name:		perl-Date-Discordian
Version:	1.36
Release:	1
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	11aa1fce9f801d7d247542abc5a0fcc3
URL:		http://search.cpan.org/dist/Date-Discordian/
BuildRequires:	perl-Date-ICal >= 1.54
BuildRequires:	perl-Date-Leapyear
BuildRequires:	perl-Memoize
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
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

%description -l pl.UTF-8
Moduł perla obliczający diskordiańską datę dla danej "prawdziwej"
daty.

Date::Discordian udostępnia dwie funkcje - discordian() oraz
inverse_discordian(). discordian() po podaniu wartości czasu zwraca
stringa zawierającego datę diskordiańską. inverse_discordian() po
podaniu daty w tym samym formacie, jaki produkuje discordian(), zwraca
wartość czasu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Date/Discordian.pm
%{_mandir}/man3/*
