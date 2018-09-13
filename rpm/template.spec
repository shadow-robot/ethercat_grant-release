Name:           ros-melodic-ethercat-grant
Version:        0.2.3
Release:        0%{?dist}
Summary:        ROS ethercat_grant package

Group:          Development/Libraries
License:        BSD
URL:            http://www.shadowrobot.com/
Source0:        %{name}-%{version}.tar.gz

Requires:       libcap-devel
Requires:       ros-melodic-roscpp
BuildRequires:  libcap-devel
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-roscpp

%description
Makes it possible to run the ros_ethercat_loop without using sudo. Forked from
pr2-grant

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Thu Sep 13 2018 Shadow Robot's software team <software@shadowrobot.com> - 0.2.3-0
- Autogenerated by Bloom

