import setuptools  #导入工具包


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
# 读写README.md 文件

setuptools.setup(
    name="fast-uiapp",  #项目名称
    version="1.0.3", #项目版本
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



    install_requires = [], #第三方依赖包
    package_data={
            #任何包中含有.txt文件，都包含它
            '': ['*.py','*.py-tpl','*.json','*.html','*.pyc','*.xlsx',"*.*"],
            #包含demo包data文件夹中的 *.dat文件

        },
    keywords = '自动化测试 app python  unittest',


)

