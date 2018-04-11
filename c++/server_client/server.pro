# Set the version of this library
VERSION = 0.1.0

HEADERS += inc/server.h
SOURCES +=src/server/server.cpp
# where to place the stuff?
DESTDIR   = bin


# additional include paths
INCLUDEPATH += src/server
INCLUDEPATH += inc

# we are building a library here
TEMPLATE = app

CONFIG += QT

TARGET      = Server

