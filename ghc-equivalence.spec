# generated by cabal-rpm-2.1.0
# https://docs.fedoraproject.org/en-US/packaging-guidelines/Haskell/

%global pkg_name equivalence
%global pkgver %{pkg_name}-%{version}

%ifnarch riscv64
%bcond_without tests
%else
%bcond_with tests
%endif

Name:           ghc-%{pkg_name}
Version:        0.4.1
Release:        %autorelease -e 0.riscv64
Summary:        Maintaining an equivalence relation implemented as union-find using STT

License:        BSD-3-Clause
Url:            https://hackage.haskell.org/package/%{pkg_name}
# Begin cabal-rpm sources:
Source0:        https://hackage.haskell.org/package/%{pkgver}/%{pkgver}.tar.gz
# End cabal-rpm sources

# Begin cabal-rpm deps:
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-STMonadTrans-devel
BuildRequires:  ghc-base-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-mtl-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-transformers-compat-devel
%if %{with ghc_prof}
BuildRequires:  ghc-STMonadTrans-prof
BuildRequires:  ghc-base-prof
BuildRequires:  ghc-containers-prof
#BuildRequires:  ghc-fail-prof
BuildRequires:  ghc-mtl-prof
BuildRequires:  ghc-transformers-prof
BuildRequires:  ghc-transformers-compat-prof
%endif
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-template-haskell-devel
%endif
# End cabal-rpm deps

%description
This is an implementation of Tarjan's Union-Find algorithm (Robert E.
Tarjan. "Efficiency of a Good But Not Linear Set Union Algorithm", JACM 22(2),
1975) in order to maintain an equivalence relation. This implementation is a
port of the /union-find/ package using the ST monad transformer (instead of the
IO monad).


%package devel
Summary:        Haskell %{pkg_name} library development files
Provides:       %{name}-static = %{version}-%{release}
Provides:       %{name}-static%{?_isa} = %{version}-%{release}
%if %{defined ghc_version}
Requires:       ghc-compiler = %{ghc_version}
%endif
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides the Haskell %{pkg_name} library development files.


%if %{with haddock}
%package doc
Summary:        Haskell %{pkg_name} library documentation
BuildArch:      noarch
Requires:       ghc-filesystem

%description doc
This package provides the Haskell %{pkg_name} library documentation.
%endif


%if %{with ghc_prof}
%package prof
Summary:        Haskell %{pkg_name} profiling library
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}
Supplements:    (%{name}-devel and ghc-prof)

%description prof
This package provides the Haskell %{pkg_name} profiling library.
%endif


%prep
# Begin cabal-rpm setup:
%setup -q -n %{pkgver}
# End cabal-rpm setup
cabal-tweak-drop-dep 'build-depends: fail'


%build
# Begin cabal-rpm build:
%ghc_lib_build
# End cabal-rpm build


%install
# Begin cabal-rpm install
%ghc_lib_install
# End cabal-rpm install


%check
%if %{with tests}
%cabal_test
%endif


%files -f %{name}.files
# Begin cabal-rpm files:
%license LICENSE
# End cabal-rpm files


%files devel -f %{name}-devel.files
%doc CHANGES.md


%if %{with haddock}
%files doc -f %{name}-doc.files
%license LICENSE
%endif


%if %{with ghc_prof}
%files prof -f %{name}-prof.files
%endif


%changelog
%autochangelog
