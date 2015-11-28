Summary:	Model-based Analysis for ChIP-Seq 
#Summary(pl.UTF-8):	-
Name:		MACS
Version:	1.4.1
Release:	1
License:	Artistic
Group:		Development/Languages/Python
# user and password are "publicly" visible on the web page (ROT13)
Source0:	http://macs:chipseq@liulab.dfci.harvard.edu/MACS/src/%{name}-%{version}.tar.gz
# Source0-md5:	0b6490e37265d485e387b8323e810d3d
URL:		http://liulab.dfci.harvard.edu/MACS/
BuildRequires:	python-distribute
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:		python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Next generation parallel sequencing technologies made chromatin
immunoprecipitation followed by sequencing (ChIP-Seq) a popular
strategy to study genome-wide protein-DNA interactions, while
creating challenges for analysis algorithms. We present Model-based
Analysis of ChIP-Seq (MACS) on short reads sequencers such as Genome
Analyzer (Illumina / Solexa). MACS empirically models the length of
the sequenced ChIP fragments, which tends to be shorter than
sonication or library construction size estimates, and uses it
to improve the spatial resolution of predicted binding sites.
MACS also uses a dynamic Poisson distribution to effectively capture
local biases in the genome sequence, allowing for more sensitive and
robust prediction. MACS compares favorably to existing ChIP-Seq
peak-finding algorithms, is publicly available open source, and can be
used for ChIP-Seq with or without control samples.

#%description -l pl.UTF-8

%prep
%setup -q

# fix #!/usr/bin/env python -> #!/usr/bin/python:
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' bin/* setup.py

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEW_IN_MACS14 README
%attr(755,root,root) %{_bindir}/*
%dir %{py_sitescriptdir}/MACS14
%dir %{py_sitescriptdir}/MACS14/IO
%{py_sitescriptdir}/MACS14/*.py[co]
%{py_sitescriptdir}/MACS14/IO/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/MACS-*.egg-info
%endif
