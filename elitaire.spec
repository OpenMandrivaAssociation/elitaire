%define	name	elitaire
%define version 0.1
%define svnrel	41637
%define release %mkrel 2.r%{svnrel}.1

Summary: 	Enlightenment solitaire
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Graphics
URL: 		http://get-e.org/
Source: 	%{name}-%{version}-r%{svnrel}.tar.bz2
Patch0:		elitaire-0.1-gcc44.patch
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.050, ewl-devel >= 0.5.3.050
BuildRequires:	ecore-devel >= 0.9.9.050, edje-devel >= 0.5.0.050, edje >= 0.5.0.050
BuildRequires:	eet >= 1.1.0, esmart >= 0.9.0.050, esmart-devel >= 0.9.0.050
Buildrequires:	embryo >= 0.9.9.050
BuildRequires:  desktop-file-utils
Buildrequires:  gettext-devel

%description
Enlightenment solitaire

%prep
%setup -qn %{name}
%patch0 -p0

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# %lang(fr) /usr/share/locale/fr/LC_MESSAGES/elitaire.mo
%find_lang %{name}

mkdir -p %buildroot%{_datadir}/pixmaps
mkdir -p %buildroot%{_datadir}/applications
cp data/other/%name.png %buildroot%{_datadir}/pixmaps/%name.png
cp data/other/%name.desktop %buildroot%{_datadir}/applications/%name.desktop

%if %mdkversion < 200900
%post 
%{update_menus} 
%endif

%if %mdkversion < 200900
%postun 
%{clean_menus} 
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*
%{_datadir}/%name
%_datadir/pixmaps/*.png
%{_datadir}/applications/*

