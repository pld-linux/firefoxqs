Summary:	A KDE panel applet for quick access to Firefox
Summary(pl):	Aplet panelu KDE do szybkiego dostêpu do Firefox
Name:		firefoxqs
Version:	0.1
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://dl.sourceforge.net/mozillaqs/%{name}-%{version}.tar.bz2
# Source0-md5:	9ead843ef6838eb48f782c8da5ae4dc5
URL:		http://mozillaqs.sourceforge.net/
BuildRequires:	kdelibs-devel >= 3.1
BuildRequires:	qt-devel >= 3.1
Requires:	mozilla-firefox >= 1.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Firefox Quickstarter is an small KDE utility that runs in the
SystemTray and runs a hidden instance of Firefox. You can execute
navigator program from Firefox Quickstarter.

%description -l pl
Firefox Quickstarter to niewielka, dzia³aj±ca w zasobniku systemowym
aplikacja KDE. Uruchamia ona ukryt± instancjê Firefoxa. Mo¿liwe jest
uruchomienie przegl±darki z poziomu Firefox QuickStarter.

%prep
%setup -q -n %{name}

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_datadir}/applnk/Utilities/*.desktop \
        $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%dir %{_datadir}/apps/%{name}
%{_datadir}/apps/%{name}/%{name}ui.rc
%{_iconsdir}/hicolor/*/apps/%{name}.png
%dir %{_docdir}/HTML/en/%{name}
%{_docdir}/HTML/en/%{name}/*
