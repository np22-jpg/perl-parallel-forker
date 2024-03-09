Name:           perl-parallel-forker
Version:        1.260
Release:        %autorelease
Summary:        A perl library for managing parallel processes.
License:        LGPL-3.0-only AND Artistic-2.0
URL:            https://www.veripool.org/parallel-forker
Source:         https://github.com/veripool/parallel-forker/archive/refs/tags/v%{version}/parallel-forker-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl
BuildRequires:  perl(Proc::ProcessTable)
Buildrequires:  perl-generators
BuildRequires:  perl-interpreter

%description
Parallel::Forker is a Perl package to manage parallel 
processes that are either subroutines or system commands. 
Parallel::Forker supports being able to specify complicated
expressions to determine which processes run after others, 
or processes that run when processes others fail.

# No debug package required
%global debug_package %{nil}

%prep
%autosetup -n parallel-forker-%{version}

# tests fail without README
touch README

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1 OPTIMIZE="$RPM_OPT_FLAGS"
%make_build 

%check
make test 

%install
%make_install
%{_fixperms} %{buildroot}

%files
%license README.pod
%{perl_vendorlib}/*
%{_mandir}/man3/Parallel::Forker*

%changelog
%autochangelog
