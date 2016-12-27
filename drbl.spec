Name: drbl
Version: 2.20.11
Release: alt1
BuildArch: noarch

Summary: DRBL (Diskless Remote Boot in Linux) is free software, open source solution to managing the deployment of the GNU/Linux operating system across many clients

License: GPL
Group: System/Configuration/Hardware
Url: http://drbl.org/

Packager: Sample Maintainer <samplemaintainer@altlinux.org>
%filter_from_requires /^\/.*/d
%filter_from_requires /^sysvinit.*/d
%filter_from_requires /^systemd.*/d
BuildPreReq: bash perl-base perl-Term-ANSIColor perl-Math-BigInt
Source: %name-%version.tar
Requires: bash perl-base perl-Term-ANSIColor perl-Math-BigInt


%description
DRBL (Diskless Remote Boot in Linux) is free software, open source
solution to managing the deployment of the GNU/Linux operating
system across many clients. Imagine the time required to install
GNU/Linux on 40, 30, or even 10 client machines individually! DRBL
allows for the configuration all of your client computers by
installing just one server (remember, not just any virtual private
server) machine.

DRBL provides a diskless or systemless environment for client
machines. It works on Debian, Ubuntu, Red Hat, Fedora, CentOS
and SuSE. DRBL uses distributed hardware resources and makes
it possible for clients to fully access local hardware. It
also includes Clonezilla, a partitioning and disk cloning utility
similar to True Image or Norton Ghost.

The features of DRBL:
  - Peacefully coexists with other OS
  - Simply install DRBL on a single server and all your clients
    are taken care of
  - Save on hardware, budget, and maintenance fees


%prep
%setup

%build

%make_build

%install
%makeinstall_std


%find_lang %name

%files -f %name.lang
/etc/drbl
/usr/bin/*
/usr/sbin/*
/usr/share/drbl
/usr/share/gdm/themes/drbl-gdm



%changelog
* Sun Dec 04 2016 Sample Maintainer <samplemaintainer@altlinux.org> 2.20.11-alt1
- initial build

