import os
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

