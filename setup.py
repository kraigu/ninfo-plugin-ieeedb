from setup tools import setup, find_packages

setup(name='ninfo-plugin-ieeedb',
      version='0.0.1',
      zip_safe = False,
      packages = find_packages(exclude = ["tests"]),
      include_package_data = True, 
      install_requires = [
          "ninfo>=0.1.11",
          "ouilookup",
      ],
      entry_points = {
          'ninfo.plugin': [
              'ieeedb = ninfo_plugin_ieeedb',
          ]
      }
)
