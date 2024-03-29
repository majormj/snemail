import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sqltool",
    version="1.1.16",
    author="manji",
    author_email="pnsm@qq.com",                         # 作者邮箱
    description="发送邮件库",                            # 模块简介
    long_description=long_description,                  # 模块详细介绍
    long_description_content_type="text/markdown",      # 模块详细介绍格式
    url="https://github.com/majormj/sendmail",
    packages=setuptools.find_packages(),                # 自动找到项目中导入的模块

    # 模块相关的元数据（更多描述信息）
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    # 依赖模块
    install_requires=[
        # 'PyEmail',
    ],

    python_requires='>=3' ,                             # 运行的python版本
)