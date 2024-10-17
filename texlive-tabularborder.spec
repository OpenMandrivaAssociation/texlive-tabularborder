Name:		texlive-tabularborder
Version:	17885
Release:	2
Summary:	Correct index entries for chemical compounds
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabularborder
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
