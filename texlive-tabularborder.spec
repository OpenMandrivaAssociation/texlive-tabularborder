# revision 17885
# category Package
# catalog-ctan /macros/latex/contrib/tabularborder
# catalog-date 2010-04-29 12:40:52 +0200
# catalog-license lppl1.2
# catalog-version 1.0a
Name:		texlive-tabularborder
Version:	1.0a
Release:	10
Summary:	Correct index entries for chemical compounds
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tabularborder
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tabular environment is changed so that the outer
\tabcolseps are compensated and a \hline has the same length as
the text. No @{} is needed.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tabularborder/tabularborder.sty
%doc %{_texmfdistdir}/doc/latex/tabularborder/tabularborder.pdf
#- source
%doc %{_texmfdistdir}/source/latex/tabularborder/tabularborder.dtx
%doc %{_texmfdistdir}/source/latex/tabularborder/tabularborder.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-2
+ Revision: 756438
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0a-1
+ Revision: 719645
- texlive-tabularborder
- texlive-tabularborder
- texlive-tabularborder

