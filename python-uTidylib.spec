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


%changelog
* Thu Nov 04 2010 Funda Wang <fwang@mandriva.org> 0.2-10mdv2011.0
+ Revision: 593151
- rebuild for py 2.7

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.2-9mdv2010.0
+ Revision: 442539
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 0.2-8mdv2009.1
+ Revision: 323411
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.2-7mdv2009.0
+ Revision: 259858
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.2-6mdv2009.0
+ Revision: 247707
- rebuild

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2-4mdv2008.1
+ Revision: 140738
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 27 2007 Funda Wang <fwang@mandriva.org> 0.2-4mdv2008.0
+ Revision: 71753
- add egg-info
- Rebuild for python 2.5

* Sun Aug 26 2007 Gaëtan Lehmann <glehmann@mandriva.org> 0.2-3mdv2008.0
+ Revision: 71553
- rebuild


* Fri Feb 03 2006 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-2mdk
- use mkrel and py_puresitedir

* Thu Jan 27 2005 Gaetan Lehmann <gaetan.lehmann@jouy.inra.fr> 0.2-1mdk
- mandrake contrib

