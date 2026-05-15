# FIXME split into several packages
%define major 5
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define plasmaver %(echo %{version} |cut -d. -f1-3)

#define git 20240222
%define gitbranch Plasma/6.6
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

#define libweather_major 1
#define libweather %mklibname plasmaweather %{libweather_major}

Name: sonic-workspace-addons
Version: 6.6.5
Release: %{?git:0.%{git}.}1
URL:     https://github.com/Sonic-DE/sonic-workspace-addons
# %if 0%{?git:1}
# Source0: https://invent.kde.org/plasma/kdeplasma-addons/-/archive/%{gitbranch}/kdeplasma-addons-%{gitbranchd}.tar.bz2#/kdeplasma-addons-%{git}.tar.bz2
# %else
Source0: %url/archive/%version/%name-%version.tar.gz
# %endif
Summary: SonicDE Add-Ons
License: GPL
Group: Graphical desktop/SonicDE
BuildRequires: cmake(ECM)
BuildRequires: cmake(KF6DNSSD)
BuildRequires: cmake(KF6DocTools)

# pending rename
# BuildRequires: cmake(KF6CoreAddons)
# BuildRequires: cmake(KF6KIO)
BuildRequires: %{_lib}SonicFrameworksCoreAddons-devel
BuildRequires: %{_lib}SonicFramworksIO-devel

BuildRequires: cmake(KF6DBusAddons)
BuildRequires: cmake(KF6ConfigWidgets)
BuildRequires: cmake(KF6IconThemes)

BuildRequires: cmake(KF6Solid)
BuildRequires: cmake(KF6KCMUtils)
BuildRequires: cmake(KF6Svg)

# pending rename
# BuildRequires: cmake(Plasma) >= 5.90.0
# BuildRequires: cmake(PlasmaQuick)
BuildRequires: %{_lib}SonicDE-devel

# pending rename
# BuildRequires: cmake(KF6Runner)
BuildRequires: %{_lib}SonicFrameworksRunner-devel

BuildRequires: cmake(KF6NewStuff)

# pending rename
# BuildRequires: cmake(PlasmaActivities)
BuildRequires: %{_lib}SonicDEActivities-devel

BuildRequires: cmake(KF6Declarative)
BuildRequires: cmake(KF6Holidays)
BuildRequires: cmake(KF6Purpose)
BuildRequires: cmake(KF6Notifications)
BuildRequires: cmake(Plasma5Support)
BuildRequires: cmake(KF6Sonnet)
BuildRequires: cmake(KF6UnitConversion)

# pending rename
# BuildRequires: cmake(KF6Auth)
BuildRequires: %{_lib}SonicFrameworksAuth-devel

#BuildRequires: cmake(LibTaskManager)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Gui)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6WebEngineCore)
BuildRequires: cmake(Qt6WebEngineWidgets)
BuildRequires: cmake(Qt6Positioning)
BuildRequires: cmake(Qt6Core5Compat)
BuildRequires: cmake(Qt6WebEngineQuick)
BuildRequires: pkgconfig(x11)
BuildRequires: pkgconfig(xcb)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-xkb)
BuildRequires: pkgconfig(xft)
BuildRequires: cmake(KF6NetworkManagerQt)
# Obsoletes: %{libweather} < %{EVRD}

Conflicts:     kdeplasma-addons

BuildSystem: cmake
BuildOption: -DBUILD_QCH:BOOL=ON
BuildOption: -DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

%description
%summary

%install -a
# (tpg) not needed
rm -rf	%{buildroot}%{_libdir}/libplasmapotdprovidercore.so \
	%{buildroot}%{_includedir} \
	%{buildroot}%{_libdir}/cmake/PlasmaPotdProvider \
	%{buildroot}%{_datadir}/kdevappwizard/templates/plasmapotdprovider.tar.bz2

%files -f %{name}.lang
%{_libdir}/libplasmapotdprovidercore.so*
%{_datadir}/qlogging-categories6/kdeplasma-addons.categories
%{_datadir}/knsrcfiles/comic.knsrc
%{_qtdir}/plugins/plasma/applets/*.so
%{_qtdir}/plugins/potd
%{_qtdir}/plugins/plasmacalendarplugins/astronomicalevents.so
%{_qtdir}/plugins/plasmacalendarplugins/astronomicalevents
%{_qtdir}/qml/org/kde/plasma/private/dict
%{_datadir}/icons/hicolor/scalable/apps/accessories-dictionary.svgz
%{_datadir}/plasma/plasmoids/org.kde.plasma.kickerdash
%{_datadir}/plasma/desktoptheme/default/widgets/timer.svgz
%{_datadir}/plasma/desktoptheme/default/weather/wind-arrows.svgz
%{_datadir}/plasma/wallpapers/org.kde.haenau
%{_datadir}/plasma/wallpapers/org.kde.hunyango
%{_datadir}/plasma/wallpapers/org.kde.potd
%{_datadir}/kwin/effects/cube
%{_datadir}/kwin/tabbox
%{_qtdir}/qml/org/kde/plasma/private/fifteenpuzzle
%{_qtdir}/qml/org/kde/plasmacalendar
%{_qtdir}/plugins/kf6/krunner/unitconverter.so
%{_qtdir}/plugins/kf6/krunner/krunner_charrunner.so
%{_qtdir}/plugins/kf6/krunner/krunner_dictionary.so
%{_qtdir}/plugins/kf6/krunner/krunner_katesessions.so
%{_qtdir}/plugins/kf6/krunner/krunner_konsoleprofiles.so
%{_qtdir}/plugins/kf6/krunner/krunner_spellcheck.so
%{_qtdir}/plugins/kf6/krunner/org.kde.datetime.so
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_charrunner.so
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_dictionary.so
%{_qtdir}/plugins/kf6/krunner/kcms/kcm_krunner_spellcheck.so
%{_qtdir}/plugins/kwin/effects/configs/kwin_cube_config.so
%{_qtdir}/qml/org/kde/plasma/wallpapers/potd
%{_qtdir}/plugins/plasmacalendarplugins/alternatecalendar.so
%{_qtdir}/plugins/plasmacalendarplugins/alternatecalendar
%{_qtdir}/qml/org/kde/plasma/private/profiles
%{_qtdir}/plugins/kf6/packagestructure/plasma_comic.so
%{_datadir}/knotifications6/plasma_applet_timer.notifyrc
%{_libdir}/libexec/kf6/kauth/kameleonhelper
%{_qtdir}/plugins/kf6/kded/kameleon.so
%{_qtdir}/qml/org/kde/plasma/private/alternatecalendarconfig
%{_datadir}/dbus-1/system-services/org.kde.kameleonhelper.service
%{_datadir}/dbus-1/system.d/org.kde.kameleonhelper.conf
%{_datadir}/polkit-1/actions/org.kde.kameleonhelper.policy
%{_qtdir}/plugins/kf6/krunner/krunner_colors.so
%{_datadir}/qlogging-categories6/kdeplasma-addons.renamecategories
%{_libdir}/libplasmaweatherdata.so*
%{_libdir}/libplasmaweatherion.so*
%{_qtdir}/plugins/plasma/weather_ions
%{_datadir}/plasma/weather/noaa_station_list.xml
%{_datadir}/kwin/scripts/virtualdesktopsonlyonprimary/contents/code/main.js
%{_datadir}/kwin/scripts/virtualdesktopsonlyonprimary/metadata.json
%{_datadir}/plasma/wallpapers/org.kde.tiled
