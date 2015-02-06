Name:           morituri
Version:        0.1.1
Release:        3
Summary:        CD ripper aiming for accuracy over speed
Source:         http://thomas.apestaart.org/download/morituri/%{name}-%{version}.tar.bz2
URL:            http://thomas.apestaart.org/morituri/trac
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch
BuildRequires:  python-gobject
BuildRequires:  gstreamer0.10-python

Requires:       cdparanoia
Requires:       cdrdao
Requires:       gstreamer0.10-plugins-good >= 0.10.16
Requires:       gstreamer0.10-python
Requires:       python-musicbrainz2
Requires:       python-pycdio
Requires:       python-pkg-resources

%description
Morituri is a CD ripper that aims for accuracy over speed. Its features 
are modeled to compare with Exact Audio Copy on Windows. It features
support for MusicBrainz for metadata lookup, support for AccurateRip
verification, detection of sample read offset of drives, the ability to
test and copy a rip, the ability to detect and rip Hidden Track One
Audio, templates for file and directory naming, and tagging using
GStreamer. Currently, it only supports lossless encoding and only has
a command line client.

%prep

%setup -q
%configure2_5x --sysconfdir=%{_sysconfdir}

%build

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README morituri.doap NEWS RELEASE ChangeLog
%{_bindir}/rip
%{_mandir}/man1/rip.1*
%{py_puresitedir}/morituri
%{_sysconfdir}/bash_completion.d/rip


%changelog
* Sat Apr 17 2010 Frederik Himpe <fhimpe@mandriva.org> 0.1.1-2mdv2010.1
+ Revision: 535787
- Update to new version 0.1.1

* Sun Nov 22 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1.0-2mdv2010.1
+ Revision: 468841
- fix morituri home page URL
- add missing python package to Requires:

* Sat Sep 26 2009 Frederik Himpe <fhimpe@mandriva.org> 0.1.0-1mdv2010.0
+ Revision: 449648
- Import package in Mandriva, based on upstream (Fedora) SRPM
- create morituri

