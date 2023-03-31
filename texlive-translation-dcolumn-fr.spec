Name:		texlive-translation-dcolumn-fr
Version:	24345
Release:	2
Summary:	French translation of the documentation of dcolumn
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/dcolumn/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-dcolumn-fr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-dcolumn-fr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
A French translation of the documentation of dcolumn.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/Copyright
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/README
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.dtx
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
