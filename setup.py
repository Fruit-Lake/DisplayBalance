from setuptools import setup, find_packages

setup(
    name="displaybalance",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        # 项目依赖将在这里列出
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "black>=22.3.0",
            "flake8>=4.0.0",
            "mypy>=0.950",
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="一个用于显示余额的Python项目",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/DisplayBalance",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
) 