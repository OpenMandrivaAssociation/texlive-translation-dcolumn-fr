# revision 24345
# category Package
# catalog-ctan /info/translations/dcolumn/fr
# catalog-date 2011-10-20 17:00:28 +0200
# catalog-license lppl
# catalog-version undef
Name:		texlive-translation-dcolumn-fr
Version:	20111020
Release:	1
Summary:	French translation of the documentation of dcolumn
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/translations/dcolumn/fr
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-dcolumn-fr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/translation-dcolumn-fr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A French translation of the documentation of dcolumn.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/Copyright
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/README
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.dtx
%doc %{_texmfdistdir}/doc/latex/translation-dcolumn-fr/f-dcolumn.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
