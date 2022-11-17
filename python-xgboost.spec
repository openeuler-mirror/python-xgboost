%global pypi_name xgboost
%global vendor %{?_vendor:%{_vendor}}%{!?_vendor:openEuler}
%define _debugsource_template %{nil}

Name:           python-%{pypi_name}
Version:        0.90
Release:        5
Summary:        Scalable, Portable and Distributed Gradient Boosting Library
License:        Apache-2
URL:            https://github.com/dmlc/xgboost
Source0:        https://files.pythonhosted.org/packages/96/84/4e2cae6247f397f83d8adc5c2a2a0c5d7d790a14a4c7400ff6574586f589/%{pypi_name}-%{version}.tar.gz
BuildRequires:  python3-devel gcc-c++
Requires:       dejavu-fonts-common dejavu-sans-fonts libgfortran
Requires:       openblas openblas-serial openblas-threads
Requires:       python3-numpy python3-numpy-f2py python3-scipy
Requires:       fontconfig fontpackages-filesystem
Requires:       libX11 libXau libXft libXrender libxcb
Requires:       %{vendor}-rpm-config
Requires:       python3-devel python3-rpm-generators tk
Patch01:       disable-sse-for-riscv.patch

%global _description \
XGBoost is an optimized distributed gradient boosting library designed to be \
highly efficient, flexible and portable. It implements machine learning \
algorithms under the Gradient Boosting framework. XGBoost provides a parallel \
tree boosting (also known as GBDT, GBM) that solve many data science problems \
in a fast and accurate way. The same code runs on major distributed environment \
(Kubernetes, Hadoop, SGE, MPI, Dask) and can solve problems beyond billions of \
examples.

%description %{_description}

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{_description}

%prep
%autosetup -n %{pypi_name}-%{version} -p1

%build
pushd %{pypi_name}
%make_build
popd
%py3_build

%install
pushd %{pypi_name}
install -m 755 -d %{buildroot}%{_bindir}
install -m 755 xgboost %{buildroot}%{_bindir}
install -m 755 -d %{buildroot}/usr/xgboost
install lib/libxgboost.so %{buildroot}/usr/xgboost
popd
%py3_install
find %{buildroot} -name "*.py" -exec sed -i -r 's!/usr/bin/python(\s|$)!/usr/bin/python3\1!' {} \;

%check

%files -n python3-%{pypi_name}
%{_bindir}/xgboost
/usr/xgboost
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.egg-info/

%changelog
* Thu Nov 17 2022 caodongxia <caodongxia@h-partners.com> - 0.90-5
- Replace openEuler with vendor macro

* Mon Jan 24 2022 lvxiaoqian <xiaoqian@nj.iscas.ac.cn> - 0.90-4
- do not use sse for riscv

* Wed Jun 23 2021 wuchaochao <wuchaochao4@huawei.com> - 0.90-3
- add buildrequires: gcc-c++

* Thu Feb 27 2020 lijin Yang <yanglijin@huawei.com> - 0.90-2
- remove dependency of python2
* Thu Nov 7 2019 mengxian <mengxian@huawei.com> - 0.90-1
- Init package
