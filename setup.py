{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "from setuptools import setup, find_packages\n",
    "\n",
    "setup(\n",
    "    name=\"projectPapermill\",\n",
    "    version=\"0.1\",\n",
    "    url=\"https://github.com/my_username/papermill_timing.git\",\n",
    "    author=\"Prar\",\n",
    "    author_email=\"sprarthana.ps@gmail.com\",\n",
    "    description=\"A papermill engine that logs additional timing information about code.\",\n",
    "    packages=find_packages(\"./src\"),\n",
    "    package_dir={\"\": \"src\"},\n",
    "    install_requires=[\"papermill\", \"nbformat\"],\n",
    "    entry_points={\"papermill.engine\": [\"timer_engine=papermill_timing:TimingEngine\"]},\n",
    ")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.5.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
