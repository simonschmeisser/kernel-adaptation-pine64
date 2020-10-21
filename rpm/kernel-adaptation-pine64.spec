# Device details
%define device pine64

# Kernel target architecture
%define kernel_arch arm64

# Crossbuild toolchain to use
%define crossbuild aarch64

# RPM target architecture, remove to leave it unaffected
# You should have a good reason to change the target architecture
# (like building on aarch64 targeting an armv7hl repository)
%define device_target_cpu armv7hl

# Defconfig to pick-up
%define defconfig config-sailfishos-allwinner.aarch64

# Linux kernel source directory
%define source_directory linux/

# Build modules
%define build_modules 1

# Build Image
%define build_Image 1

# Build uImage
##define build_uImage 1

# Build zImage
##define build_zImage 1

# Build and pick-up the following devicetrees
%define devicetrees allwinner/sun50i-a64-pinephone-1.0.dtb allwinner/sun50i-a64-pinephone-1.1.dtb allwinner/sun50i-a64-pinephone-1.2.dtb allwinner/sun50i-a64-pinetab.dtb

Patch0:  0002-dts-add-pinetab-dev-old-display-panel.patch
Patch1:  0007-dts-pinetab-make-audio-routing-consistent-with-pinep.patch
Patch2:  0008-pinetab-bluetooth.patch

%prep
cd linux/
%patch0 -p1
%patch1 -p1
%patch2 -p1
cd ..

%include kernel-adaptation-simplified/kernel-adaptation-simplified.inc
