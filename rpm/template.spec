Name:           ros-indigo-cob-common
Version:        0.6.4
Release:        0%{?dist}
Summary:        ROS cob_common package

Group:          Development/Libraries
License:        LGPL
URL:            http://ros.org/wiki/cob_common
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-indigo-cob-description
Requires:       ros-indigo-cob-msgs
Requires:       ros-indigo-cob-srvs
Requires:       ros-indigo-raw-description
BuildRequires:  ros-indigo-catkin

%description
The cob_common stack hosts common packages that are used within the Care-O-bot
repository. E.g. utility packages or common message and service definitions etc.
Also the urdf desciption of the robot is located in this stack.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Sat Aug 29 2015 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.4-0
- Autogenerated by Bloom

* Mon Dec 15 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.2-0
- Autogenerated by Bloom

* Wed Sep 24 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.1-0
- Autogenerated by Bloom

* Tue Sep 16 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.6.0-0
- Autogenerated by Bloom

* Wed Aug 27 2014 Florian Weisshardt <fmw@ipa.fhg.de> - 0.5.5-0
- Autogenerated by Bloom

