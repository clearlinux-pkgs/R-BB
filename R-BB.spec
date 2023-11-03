#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-BB
Version  : 2019.10.1
Release  : 41
URL      : https://cran.r-project.org/src/contrib/BB_2019.10-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/BB_2019.10-1.tar.gz
Summary  : Solving and Optimizing Large-Scale Nonlinear Systems
Group    : Development/Tools
License  : GPL-3.0
Requires: R-quadprog
BuildRequires : R-Hmisc
BuildRequires : R-numDeriv
BuildRequires : R-quadprog
BuildRequires : R-setRNG
BuildRequires : buildreq-R

%description
system of equations, and for optimizing nonlinear objective
        functions subject to simple constraints. A tutorial style
        introduction to this package is available in a vignette on the
        CRAN download page or, when the package is loaded in an R
        session, with vignette("BB").

%prep
%setup -q -c -n BB
cd %{_builddir}/BB

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1640977293

%install
export SOURCE_DATE_EPOCH=1640977293
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BB
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BB
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library BB
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc BB || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/BB/CITATION
/usr/lib64/R/library/BB/DESCRIPTION
/usr/lib64/R/library/BB/INDEX
/usr/lib64/R/library/BB/Meta/Rd.rds
/usr/lib64/R/library/BB/Meta/demo.rds
/usr/lib64/R/library/BB/Meta/features.rds
/usr/lib64/R/library/BB/Meta/hsearch.rds
/usr/lib64/R/library/BB/Meta/links.rds
/usr/lib64/R/library/BB/Meta/nsInfo.rds
/usr/lib64/R/library/BB/Meta/package.rds
/usr/lib64/R/library/BB/Meta/vignette.rds
/usr/lib64/R/library/BB/NAMESPACE
/usr/lib64/R/library/BB/NEWS
/usr/lib64/R/library/BB/R/BB
/usr/lib64/R/library/BB/R/BB.rdb
/usr/lib64/R/library/BB/R/BB.rdx
/usr/lib64/R/library/BB/demo/multiStart.R
/usr/lib64/R/library/BB/demo/nlmin.R
/usr/lib64/R/library/BB/demo/nlsolve.R
/usr/lib64/R/library/BB/doc/BB.R
/usr/lib64/R/library/BB/doc/BB.Stex
/usr/lib64/R/library/BB/doc/BB.pdf
/usr/lib64/R/library/BB/doc/BB_JSS.bib
/usr/lib64/R/library/BB/doc/BBvignetteJSS.R
/usr/lib64/R/library/BB/doc/BBvignetteJSS.Stex
/usr/lib64/R/library/BB/doc/BBvignetteJSS.pdf
/usr/lib64/R/library/BB/doc/index.html
/usr/lib64/R/library/BB/help/AnIndex
/usr/lib64/R/library/BB/help/BB.rdb
/usr/lib64/R/library/BB/help/BB.rdx
/usr/lib64/R/library/BB/help/aliases.rds
/usr/lib64/R/library/BB/help/paths.rds
/usr/lib64/R/library/BB/html/00Index.html
/usr/lib64/R/library/BB/html/R.css
/usr/lib64/R/library/BB/slowTests/LinearInequality_Gaussmix.R
/usr/lib64/R/library/BB/slowTests/lower-upper.R
/usr/lib64/R/library/BB/slowTests/spg_constraints.R
/usr/lib64/R/library/BB/tests/BBsolve.R
/usr/lib64/R/library/BB/tests/brown.R
/usr/lib64/R/library/BB/tests/broydt.R
/usr/lib64/R/library/BB/tests/chen.R
/usr/lib64/R/library/BB/tests/dfsane.R
/usr/lib64/R/library/BB/tests/extrosbk.R
/usr/lib64/R/library/BB/tests/froth.R
/usr/lib64/R/library/BB/tests/multiStartBrownln.R
/usr/lib64/R/library/BB/tests/multiStartHDP.R
/usr/lib64/R/library/BB/tests/multiStartTroesch.R
/usr/lib64/R/library/BB/tests/poissmix.R
/usr/lib64/R/library/BB/tests/projectLinear.R
/usr/lib64/R/library/BB/tests/rosbkext.R
/usr/lib64/R/library/BB/tests/sane.R
/usr/lib64/R/library/BB/tests/sc2.R
/usr/lib64/R/library/BB/tests/spgExact.R
/usr/lib64/R/library/BB/tests/trig.R
/usr/lib64/R/library/BB/tests/trigexp.R
/usr/lib64/R/library/BB/tests/troesch.R
/usr/lib64/R/library/BB/tests/uniroot.R
/usr/lib64/R/library/BB/tests/valley.R
/usr/lib64/R/library/BB/tests/vmmix.R
