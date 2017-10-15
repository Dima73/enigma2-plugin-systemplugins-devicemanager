# for localized messages
from . import _

from HddSetup import HddSetup
from HddMount import HddFastRemove
from Plugins.Plugin import PluginDescriptor
import os

def supportExtFat():
	if not os.path.isfile("/sbin/mkexfatfs"):
		arch = os.popen("uname -m").read()
		if 'mips' in arch:
			os.system("cp /usr/lib/enigma2/python/Plugins/SystemPlugins/DeviceManager/bin/mips/mkexfatfs /sbin/mkexfatfs && chmod 755 /sbin/mkexfatfs && ln /sbin/mkexfatfs /sbin/mkfs.exfat")
			os.system("cp /usr/lib/enigma2/python/Plugins/SystemPlugins/DeviceManager/bin/mips/exfatfsck /sbin/exfatfsck && chmod 755 /sbin/exfatfsck")
		elif 'armv7l' in arch:
			os.system("cp /usr/lib/enigma2/python/Plugins/SystemPlugins/DeviceManager/bin/armv7l/mkexfatfs /sbin/mkexfatfs && chmod 755 /sbin/mkexfatfs && ln /sbin/mkexfatfs /sbin/mkfs.exfat")
			os.system("cp /usr/lib/enigma2/python/Plugins/SystemPlugins/DeviceManager/bin/armv7l/exfatfsck /sbin/exfatfsck && chmod 755 /sbin/exfatfsck")
		elif 'sh4' in arch:
			os.system("cp /usr/lib/enigma2/python/Plugins/SystemPlugins/DeviceManager/bin/sh4/mkexfatfs /sbin/mkexfatfs && chmod 755 /sbin/mkexfatfs && ln /sbin/mkexfatfs /sbin/mkfs.exfat")
			os.system("cp /usr/lib/enigma2/python/Plugins/SystemPlugins/DeviceManager/bin/sh4/exfatfsck /sbin/exfatfsck && chmod 755 /sbin/exfatfsck")
	if "exfat-fuse" in open("/etc/filesystems").read():
		pass
	else:
		os.system("echo exfat-fuse >> /etc/filesystems && opkg update && opkg install fuse-exfat")

def deviceManagerMain(session, **kwargs):
	supportExtFat()
	session.open(HddSetup)

def deviceManagerSetup(menuid, **kwargs):
	if menuid != "system":
		return []
	return [(_("Device Manager"), deviceManagerMain, "device_manager", None)]

def deviceManagerFastRemove(session, **kwargs):
	session.open(HddFastRemove)


def Plugins(**kwargs):
	return [PluginDescriptor(name = _("Device Manager"), description = _("Format/Partition your Devices and manage Mountpoints"), where = PluginDescriptor.WHERE_MENU, fnc = deviceManagerSetup),
			PluginDescriptor(name = _("Device Manager - Fast Mounted Remove"), description = _("Quick and safe remove for your mounted devices "), where = PluginDescriptor.WHERE_EXTENSIONSMENU, fnc = deviceManagerFastRemove)]
