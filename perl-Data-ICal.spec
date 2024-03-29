#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Data
%define	pnam	ICal
Summary:	Data::ICal.pm - Generates iCalendar (RFC 2445) calendar files
Name:		perl-Data-ICal
Version:	0.24
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
# Source0:	http://search.cpan.org/CPAN/authors/id/A/AL/ALEXMV/%{pdir}-%{pnam}-%{version}.tar.gz
Source0:        https://cpan.metacpan.org/authors/id/B/BP/BPS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f90c55d07a03172f5f5ef516e8d45d3d
URL:		http://search.cpan.org/dist/Data-ICal/
BuildRequires:	perl-Class-ReturnValue
BuildRequires:  perl-Module-Install
BuildRequires:	perl-Test-LongString
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Test-Warn
BuildRequires:	perl-Text-vFile-asData
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Data::ICal object represents a VCALENDAR object as defined in the
iCalendar protocol (RFC 2445, MIME type "text/calendar"), as
implemented in many popular calendaring programs such as Apple's iCal.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor < /dev/null
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
%doc Changes
%{perl_vendorlib}/Data/ICal
%{perl_vendorlib}/Data/*.pm
%{_mandir}/man3/*
