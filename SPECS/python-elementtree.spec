%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

#python major version
%{expand: %%define pyver %(%{__python} -c 'import sys;print(sys.version[0:3])')}

# upsteams minor version
%define minor 20050316

Name:		python-elementtree
Version:	1.2.6
Release:	1.ius%{?dist}
Summary:	a light-weight XML object model for Python

Group:		Applicatons/System
License:	MIT
URL:		http://effbot.org/zone/element-index.htm
Source0:	http://effbot.org/media/downloads/elementtree-%{version}-%{minor}.tar.gz

BuildArch:	noarch
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires:	python, python-setuptools
Requires:	python,

%description
The Element type is a flexible container object, designed to store hierarchical data structures in memory. 
Element structures can be converted to and from XML.

%prep
%setup -q -n elementtree-%{version}-%{minor}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 \
		    --skip-build \
	     --root %{buildroot}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc PKG-INFO README

# EGG is not installed on EL5
%if (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{python_sitelib}/elementtree-%{version}_%{minor}-py%{pyver}.egg-info/
%endif

%{python_sitelib}/elementtree/

%changelog
* Fri Jun 10 2011 Jeffrey Ness <jeffrey.ness@rackspace.com> - 1.2.6-1.ius
- Initial spec
