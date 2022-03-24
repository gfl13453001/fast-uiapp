import setuptools  #导入工具包


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# 读写README.md 文件

setuptools.setup(
    name="uiapp",  #项目名称
    version="1.0.1", #项目版本
    author="guanfl", #开发者名称
    author_email="gfl13453001@163.com",  #邮箱
    description="轻量型APP自动化测试框架",  #描述
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gfl13453001/testframework.git", #github地址
    packages = setuptools.find_packages('src'),  # 包含所有src中的包
    package_dir = {'':'src'},   # 告诉distutils包都在src下

    classifiers=[
        # 3 - Alpha
        # 4 - Beta
        # 5 - Production/Stable
        "Development Status :: 4 - Beta",
        # "Programming Language :: Python :: 3",
        # 支持的python版本md
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ], #依赖环境

    # python 依赖版本
    python_requires='>=3.5',

    # Appium-Python-Client==0.49
    # certifi==2019.11.28



    # chardet==3.0.4
    # decorator==4.4.1
    # facebook-wda==0.4.2
    #
    # idna==2.8
    # Pillow==6.2.1
    # py==1.8.1
    # PyMySQL==0.9.3
    # pytesseract==0.3.1
    # python-dateutil==2.8.1
    # requests==2.22.0
    # retry==0.9.2
    # selenium==3.141.0
    # six==1.13.0
    # testdata==1.1.3
    # text-unidecode==1.3
    # urllib3==1.25.7


    install_requires = [], #第三方依赖包
    package_data={
            #任何包中含有.txt文件，都包含它
            '': ['*.py','*.py-tpl','*.json','*.html','*.pyc','*.xlsx',"*.*"],
            #包含demo包data文件夹中的 *.dat文件

        },
    keywords = '自动化测试 app python  unittest',

    # 命令參數 tank命令会自动执行指定文件
    # entry_points={
    #         'console_scripts': [
    #             # 命令 = 包.模块.方法
    #             'tank=tank.bin.tank_admin:main'
    #         ],
    #     },

)









# 执行python setup.py bdist_egg即可打包一个test的包了。



# name 包名
# version 版本号
# packages 所包含的其他包

# python setup.py install 包测试安装
#

# packages = find_packages('src'),  # 包含所有src中的包
#     package_dir = {'':'src'},   # 告诉distutils包都在src下

# 使用find_packages()
# 对于简单工程来说，手动增加packages参数很容易，刚刚我们用到了这个函数，
# 它默认在和setup.py同一目录下搜索各个含有init.py的包。
# 其实我们可以将包统一放在一个src目录中，另外，这个包内可能还有aaa.txt文件和data数据文件夹。


# 使用entry_points
#
# 一个字典，从entry point组名映射道一个表示entry point的字符串或字符串列表。
# Entry points是用来支持动态发现服务和插件的，也用来支持自动生成脚本。

#
# 这种方法中包内所有文件指的是受版本控制（CVS/SVN/GIT等）的文件，或者通过MANIFEST.in声明的
#
# from setuptools import setup, find_packages
# setup(
#     ...
#     include_package_data = True
# )

# 包含一部分，排除一部分
# from setuptools import setup, find_packages
#
# setup(
#     ...
# packages = find_packages('src'),
#            package_dir = {'': 'src'},
#
#                          include_package_data = True,
#
#                                                 # 排除所有 README.txt
#                                                 exclude_package_data = {'': ['README.txt']},
# )


