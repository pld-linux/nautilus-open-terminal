Summary:	Nautilus extension which allows you to open a terminal in arbitrary local folders
Summary(pl.UTF-8):	Rozszerzenie Nautilusa pozwalające otwierać terminal w lokalnych folderach
Name:		nautilus-open-terminal
Version:	0.20
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/nautilus-open-terminal/0.20/%{name}-%{version}.tar.xz
# Source0-md5:	e4c0900f295ea04aa821fafb509bc7b1
Patch0:		%{name}-am.patch
URL:		http://manny.cluecoder.org/packages/nautilus-open-terminal/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.16.1
BuildRequires:	gnome-desktop-devel >= 3.0.0
BuildRequires:	intltool >= 0.36.2
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 3.0.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.198
Requires(post,preun):	GConf2
Requires:	gnome-terminal
Requires:	nautilus >= 3.0.0
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allows you to open a terminal in arbitrary
local folders.

%description -l pl.UTF-8
Rozszerzenie Nautilusa pozwalające otwierać terminal w lokalnych
folderach.

%prep
%setup -q
%patch -P0 -p1

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-3.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install nautilus-open-terminal.schemas

%preun
%gconf_schema_uninstall nautilus-open-terminal.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/nautilus/extensions-3.0/libnautilus-open-terminal.so
%{_sysconfdir}/gconf/schemas/nautilus-open-terminal.schemas
