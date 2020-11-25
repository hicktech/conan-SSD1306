from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'ssd1306'
    version = '2.4.1'
    url = 'https://github.com/hicktech/conan-ssd1306'
    repo_url = 'https://github.com/adafruit/Adafruit_SSD1306.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src')
        self.copy('*.h*', dst='include')

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
