
# TODO:
#	- check if %%{py_sitescriptdir} used here doesn't break other
#	  python-logilab packages

%define	module	aspects
Summary:	Aspect Oriented Programming in Python
Summary(pl.UTF-8):	Programowanie zorientowane aspektowo w Pythonie
Name:		python-aspects
Version:	0.1.4
Release:	2
License:	GPL
Group:		Development/Languages/Python
Source0:	ftp://ftp.logilab.fr/pub/%{module}/%{module}-%{version}.tar.gz
# Source0-md5:	b915eac498c16b365b3e83ffd5385a3a
Patch0:		%{name}-setup.patch
URL:		http://www.logilab.org/projects/aspects/view
BuildRequires:	python-modules >= 2.2.1
Requires:	python-logilab-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python module that enables Aspect Oriented Programming in Python. For
now, it provides a set of ready-to-use aspects and an easy way to
create your own aspects. The current possibilities are still a bit
limited, but it will soon provide a more exhaustive way to define and
use more complex aspects.

%description -l pl.UTF-8
To jest moduł Pythona umożliwiający programowanie zorientowane
aspektowo. Na razie dostarcza zbiór gotowych do użycia aspektów oraz
łatwy sposób tworzenia własnych aspektów. Aktualne możliwości są nadal
nieco ograniczone, ale wkrótce będzie dostępna bardziej wyczerpująca
metoda definiowania i używania bardziej złożonych aspektów.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1

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
