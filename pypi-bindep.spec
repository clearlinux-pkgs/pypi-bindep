#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
# autospec version: v3
# autospec commit: 750e50d
#
Name     : pypi-bindep
Version  : 2.11.0
Release  : 12
URL      : https://files.pythonhosted.org/packages/8e/89/689d7f17c559dea2849d27365f53bd40f134056392db9e88a2590eb3dc29/bindep-2.11.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/8e/89/689d7f17c559dea2849d27365f53bd40f134056392db9e88a2590eb3dc29/bindep-2.11.0.tar.gz
Summary  : Binary dependency utility
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-bindep-bin = %{version}-%{release}
Requires: pypi-bindep-license = %{version}-%{release}
Requires: pypi-bindep-python = %{version}-%{release}
Requires: pypi-bindep-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(parsley)
BuildRequires : pypi(pbr)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
============
        
        Bindep is a tool for checking the presence of binary packages needed to
        use an application / library. It started life as a way to make it easier to set
        up a development environment for OpenStack projects. While OpenStack depends
        heavily on `pip` for installation of Python dependencies, some dependencies are
        not Python based, and particularly for testing, some dependencies have to be
        installed before `pip` can be used - such as `virtualenv` and `pip` itself.
        
        Basics
        ------
        
        Create a file called ``bindep.txt`` and in that list any
        requirements your application / library has. In your README or INSTALL or
        other documentation you can tell users to run `bindep` to report on missing
        dependencies. Users without `bindep` installed can consult the
        ``bindep.txt`` file by hand if they choose, or install `bindep`
        first and then use it.
        
        If no ``bindep.txt`` file exists, `bindep` will look at the
        old location ``other-requirements.txt``.
        
        The output from bindep is fairly verbose normally, but passing an option of
        -b/--brief outputs just the missing packages one per line, suitable for feeding
        to your package management tool of choice.
        
        If you need to maintain multiple requirements list files you can pass a
        specific filename with the -f/--file command line option. If you want to read
        the list from standard input in a pipeline instead, use a filename of "-".
        
        When bindep runs, its exit code is ``0`` if no described packages are missing,
        but ``1`` if there are packages which it believes need to be installed.
        
        Profiles
        --------
        
        Profiles can be used to describe different scenarios. For instance, you might
        have a profile for using PostgreSQL which requires the PostgreSQL client
        library, a profile for MySQL needing that client library, and a profile for
        testing which requires both libraries as well as the servers. To select a

%package bin
Summary: bin components for the pypi-bindep package.
Group: Binaries
Requires: pypi-bindep-license = %{version}-%{release}

%description bin
bin components for the pypi-bindep package.


%package license
Summary: license components for the pypi-bindep package.
Group: Default

%description license
license components for the pypi-bindep package.


%package python
Summary: python components for the pypi-bindep package.
Group: Default
Requires: pypi-bindep-python3 = %{version}-%{release}

%description python
python components for the pypi-bindep package.


%package python3
Summary: python3 components for the pypi-bindep package.
Group: Default
Requires: python3-core
Provides: pypi(bindep)
Requires: pypi(distro)
Requires: pypi(packaging)
Requires: pypi(parsley)
Requires: pypi(pbr)

%description python3
python3 components for the pypi-bindep package.


%prep
%setup -q -n bindep-2.11.0
cd %{_builddir}/bindep-2.11.0
pushd ..
cp -a bindep-2.11.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707112613
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 setup.py build

popd
%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-bindep
cp %{_builddir}/bindep-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-bindep/294b43b2cec9919063be1a3b49e8722648424779 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/bindep

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-bindep/294b43b2cec9919063be1a3b49e8722648424779

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
