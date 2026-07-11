%global tl_name tabularborder
%global tl_revision 17885

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Remove excess space at left and right of tabular
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/tabularborder
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tabularborder.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The tabular environment is changed so that the outer \tabcolseps are
compensated and a \hline has the same length as the text. No @{} is
needed.

