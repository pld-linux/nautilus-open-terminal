Summary:	Nautilus extension which allows you to open a terminal in arbitrary local folders
Summary(pl.UTF-8):	Rozszerzenie Nautilusa pozwalające otwierać terminal w lokalnych folderach
Name:		nautilus-open-terminal
Version:	0.8
Release:	1
License:	GPL v2+
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/nautilus-open-terminal/0.8/%{name}-%{version}.tar.bz2
# Source0-md5:	ce326bd02bc4b3719b613b60dd7c9a35
URL:		http://manny.cluecoder.org/packages/nautilus-open-terminal/
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel >= 1:2.6.0
BuildRequires:	gnome-desktop-devel >= 2.10.0
BuildRequires:	intltool >= 0.18
BuildRequires:	libtool
BuildRequires:	nautilus-devel >= 2.18.0
BuildRequires:	pkgconfig
Requires:	gnome-terminal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nautilus extension which allows you to open a terminal in arbitrary
local folders.

%description -l pl.UTF-8
Rozszerzenie Nautilusa pozwalające otwierać terminal w lokalnych
folderach.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/nautilus/extensions-1.0/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/nautilus/extensions-1.0/*.so
