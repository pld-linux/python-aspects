
# TODO:
#	- check if %%{py_sitescriptdir} used here doesn't break other
#	  python-logilab packages

%define	module	aspects
%include	/usr/lib/rpm/macros.python
Summary:	Aspect Oriented Programming in Python
Name:		python-aspects
Version:	0.1.2
Release:	1
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	26bc8e8a0a8992ecbda8b8d56d2d4b12
URL:		http://www.logilab.org/projects/%{module}/view
BuildRequires:	python-modules >= 2.2.1
BuildRequires:	rpm-pythonprov
Requires:	python-logilab-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module that enables Aspect Oriented Programming in Python. For now,
it provides a set of ready-to-use aspects and an easy way to create your
own aspects. The current possibilities are still a bit limited, but it will
soon provide a more exhaustive way to define and use more complex aspects.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitescriptdir} -name \*.py -exec rm -f {} \;

# see install section of python-logilab-common for explanation
rm -f $RPM_BUILD_ROOT%{py_sitescriptdir}/logilab/__init__.*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO doc/*en.txt
%{py_sitescriptdir}/*
