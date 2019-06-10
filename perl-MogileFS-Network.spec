Name:           perl-MogileFS-Network
Version:        0.06
Release:        1%{?dist}
Summary:        Network zones rebalance for MogileFS
License:        GPL or Artistic
Group:          Development/Libraries
URL:            https://github.com/mogilefs/MogileFS-Network
Source0:        MogileFS-Network-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(MogileFS::Client)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
MogileFS Server class for representing networks based on host IPs

%prep
%setup -q -n MogileFS-Network-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{perl_vendorlib}/*
%{_mandir}/man3/MogileFS*
