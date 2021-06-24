import gzip
import os
import shutil
import tempfile

import psutil


def listRoots():
    disks = psutil.disk_partitions()
    return [ disk.mountpoint for disk in disks ]


def listChildren(path):
    return os.listdir(path)


def pathExists(path):
    return os.path.exists(path)


def pathIsFile(path):
    return os.path.isfile(path)


def pathIsDirectory(path):
    return os.path.isdir(path)


def pathIsLink(path):
    return os.path.islink(path)


def compressToTempPath(path):
    with open(path, 'rb') as inflated:
        compressedFile = tempfile.NamedTemporaryFile("r+b", prefix="deflate", suffix=".gz", delete=False)
        with gzip.open(compressedFile, 'wb') as deflated:
            shutil.copyfileobj(inflated, deflated)
            return compressedFile.name


def decompressToTempPath(path):
    with gzip.open(path, 'rb') as deflated:
        rawFile = tempfile.NamedTemporaryFile("w+b", prefix="inflate", suffix=".raw", delete=False)
        with open(rawFile.name, 'rb') as inflated:
            shutil.copyfileobj(deflated, inflated)
            return rawFile.name