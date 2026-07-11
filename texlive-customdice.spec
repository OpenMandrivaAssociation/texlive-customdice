%global tl_name customdice
%global tl_revision 64089

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Simple commands for drawing customisable dice
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/customdice
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/customdice.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/customdice.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/customdice.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The customdice package for LaTeX, LuaLaTeX and XeTeX that provides
functionality for drawing dice. The aim is to provide highly-
customisable but simple-to-use commands, allowing: adding custom text to
dice faces; control over colouring; control over sizing.

