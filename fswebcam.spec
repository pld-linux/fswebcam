Summary:	Tiny and flexible webcam program
Name:		fswebcam
Version:	20140113
Release:	1
License:	GPL v2
Group:		Applications/Graphics
Source0:	http://www.firestorm.cx/fswebcam/files/%{name}-%{version}.tar.gz
# Source0-md5:	88e654edcf63504fa39f962c75d31361
URL:		http://www.firestorm.cx/fswebcam/
BuildRequires:	gd-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tiny and flexible webcam program for capturing images from a
V4L1/V4L2 device, and overlaying a caption or image.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL="install -p" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README LICENSE example.conf
%attr(755,root,root) %{_bindir}/fswebcam
%{_mandir}/man1/fswebcam.1*
