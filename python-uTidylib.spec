%define module	uTidylib

Name:           python-%{module}
Version:        0.2
Release:        %mkrel 10
Summary:        Wrapper for HTML Tidy at http://tidy.sourceforge.net

Group:          Development/Python
License:        MIT
URL:            http://utidylib.berlios.de/
Source0:        http://download.berlios.de/utidylib/%{module}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
%py_requires -d
Requires:	tidy python-ctypes

%description
The Tidy wrapper. I am the main interface to TidyLib. This package supports
processing HTML with Tidy, with all the options that the tidy command line
supports.

%prep
%setup -n %{module}-%{version} -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/tidy
%{python_sitelib}/*.egg-info
%doc *.txt LICENSE
