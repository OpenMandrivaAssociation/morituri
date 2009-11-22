Name:           morituri
Version:        0.1.0
Release:        %mkrel 1
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
%configure --sysconfdir=%{_sysconfdir}

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
#%{_mandir}/man1/rip.1*
%{py_puresitedir}/morituri
%{_sysconfdir}/bash_completion.d/rip
