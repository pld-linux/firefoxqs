Summary:	A KDE panel applet for quick access to Firefox
Summary(pl.UTF-8):	Aplet panelu KDE do szybkiego dostępu do Firefox
Name:		firefoxqs
Version:	0.1.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/mozillaqs/%{name}-%{version}.tar.bz2
# Source0-md5:	27f5ac663383f45abbbe1dade00ce023
URL:		http://mozillaqs.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	qt-devel >= 6:3.1
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	mozilla-firefox >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firefox Quickstarter is an small KDE utility that runs in the
SystemTray and runs a hidden instance of Firefox. You can execute
navigator program from Firefox Quickstarter.

%description -l pl.UTF-8
Firefox Quickstarter to niewielka, działająca w zasobniku systemowym
aplikacja KDE. Uruchamia ona ukrytą instancję Firefoksa. Możliwe jest
uruchomienie przeglądarki z poziomu Firefox QuickStartera.

%prep
%setup -q -n %{name}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop \
        $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}/%{name}ui.rc
%{_iconsdir}/hicolor/*/apps/%{name}.png
