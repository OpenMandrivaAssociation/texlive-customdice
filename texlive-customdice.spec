Name:		texlive-customdice
Version:	64089
Release:	2
Summary:	Simple commands for drawing customisable dice
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/customdice
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/customdice.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/customdice.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/customdice.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The customdice package for LaTeX, LuaLaTeX and XeTeX that
provides functionality for drawing dice. The aim is to provide
highly-customisable but simple-to-use commands, allowing:
adding custom text to dice faces; control over colouring;
control over sizing.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/customdice
%{_texmfdistdir}/tex/latex/customdice
%doc %{_texmfdistdir}/doc/latex/customdice

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
