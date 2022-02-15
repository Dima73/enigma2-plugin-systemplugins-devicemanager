from distutils.core import setup
import setup_translate


setup(name='enigma2-plugin-systemplugins-devicemanager',
		version='1.2',
		author='Dimitrij openPLi',
		author_email='dima-73@inbox.lv',
		package_dir={'SystemPlugins.DeviceManager': 'src'},
		packages=['SystemPlugins.DeviceManager'],
		package_data={'SystemPlugins.DeviceManager': ['icons/*.png']},
		description='Device manager for storage devices (format/change partitions and type/fast & fixed mount and umount) ',
		cmdclass=setup_translate.cmdclass,
	)
