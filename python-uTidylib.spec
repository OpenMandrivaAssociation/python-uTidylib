%define module	uTidylib

Name:           python-%{module}
Version:        0.2
Release:        11
Summary:        Wrapper for HTML Tidy at http://tidy.sourceforge.net


Group:          Development/Python
License:        MIT
URL:            https://utidylib.berlios.de/
Source0:        http://download.berlios.de/utidylib/%{module}-%{version}.tar.bz2
BuildArch:      noarch
BuildRequires:  python-devel
Requires:	tidy python-ctypes

%description
The Tidy wrapper. I am the main interface to TidyLib. This package supports
processing HTML with Tidy, with all the options that the tidy command line
supports.

%prep
%setup -n %{module}-%{version} -q


%build
CFLAGS="%{optflags}" python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

%clean

%files
%defattr(-,root,root,-)
%{py_puresitedir}/tidy
%{py_puresitedir}/*.egg-info
%doc *.txt LICENSE


